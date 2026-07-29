from __future__ import annotations

from pathlib import Path
import tempfile

from fastapi import FastAPI, Form, UploadFile, File, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import uvicorn
import shutil

from . import storage
from .build import main as build_site

app = FastAPI(title="Research Atlas Editor")

app.mount(
    "/assets",
    StaticFiles(directory=str(storage.DOCS / "assets")),
    name="assets",
)

templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "templates"))


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    projects = storage.list_projects()
    tasks = storage.all_tasks_with_project()
    open_tasks = [t for t in tasks if t.get("status") != "done"]
    urgent = sorted(open_tasks, key=lambda t: t.get("urgency", 0), reverse=True)[:8]
    return templates.TemplateResponse(
        request,    
        "dashboard.html",
        {
            "projects": projects,
            "tasks": tasks,
            "urgent": urgent,
            "statuses": storage.STATUSES,
            "task_statuses": storage.TASK_STATUSES,
            "priorities": storage.PRIORITIES,
        },
    )


@app.post("/projects")
def add_project(
    title: str = Form(...),
    summary: str = Form(""),
    area: str = Form("Research"),
    status: str = Form("active"),
    tags: str = Form(""),
):
    storage.create_project(title=title, summary=summary, area=area, status=status, tags=tags)
    return RedirectResponse("/", status_code=303)


@app.post("/projects/{project_id}/edit")
def edit_project(
    project_id: str,
    title: str = Form(...),
    summary: str = Form(""),
    area: str = Form("Research"),
    status: str = Form("active"),
    tags: str = Form(""),
):
    storage.update_project(
        project_id,
        title=title,
        summary=summary,
        area=area,
        status=status,
        tags=[t.strip() for t in tags.split(",") if t.strip()],
    )
    return RedirectResponse(f"/projects/{project_id}", status_code=303)


@app.get("/projects/{project_id}", response_class=HTMLResponse)
def project_detail(request: Request, project_id: str):
    project = storage.get_project(project_id)
    if project is None:
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse(
        request,
        "project.html",
        {
            "project": project,
            "statuses": storage.STATUSES,
            "task_statuses": storage.TASK_STATUSES,
            "priorities": storage.PRIORITIES,
        },
    )


@app.post("/projects/{project_id}/tasks")
def add_task(
    project_id: str,
    title: str = Form(...),
    priority: str = Form("medium"),
    due_date: str = Form(""),
    status: str = Form("todo"),
):
    storage.add_task(project_id, title=title, priority=priority, due_date=due_date, status=status)
    return RedirectResponse(f"/projects/{project_id}", status_code=303)


@app.post("/projects/{project_id}/tasks/{task_id}/status")
def set_task_status(project_id: str, task_id: str, status: str = Form(...)):
    storage.set_task_status(project_id, task_id, status)
    return RedirectResponse(f"/projects/{project_id}", status_code=303)



@app.post("/projects/{project_id}/images")
def add_image(project_id: str, caption: str = Form(""), image: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(image.file.read())
        tmp_path = Path(tmp.name)
    try:
        storage.save_uploaded_image(project_id, tmp_path, image.filename or "image.png", caption=caption)
    finally:
        tmp_path.unlink(missing_ok=True)
    return RedirectResponse(f"/projects/{project_id}", status_code=303)

@app.post("/projects/{project_id}/updates")
@app.post("/projects/{project_id}/updates")
def add_project_update(
    project_id: str,
    title: str = Form(...),
    text: str = Form(""),
    image: UploadFile | None = File(None),
    image_caption: str = Form(""),
):
    images = []

    if image is not None and image.filename:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(image.file.read())
            tmp_path = Path(tmp.name)

        try:
            ext = Path(image.filename).suffix.lower() or ".png"
            safe_name = f"{storage.now_string().replace(':', '').replace(' ', '-')}-{storage.slugify(Path(image.filename).stem)}{ext}"

            target_dir = storage.UPLOADS / project_id / "updates"
            target_dir.mkdir(parents=True, exist_ok=True)

            target = target_dir / safe_name
            shutil.copyfile(tmp_path, target)

            images.append({
                "path": f"assets/uploads/{project_id}/updates/{safe_name}",
                "caption": image_caption,
                "uploaded": storage.now_string(),
            })
        finally:
            tmp_path.unlink(missing_ok=True)

    storage.add_update(
        project_id=project_id,
        title=title,
        text=text,
        images=images,
    )

    return RedirectResponse(f"/projects/{project_id}", status_code=303)

@app.post("/projects/{project_id}/updates/{update_id}/edit")
def edit_project_update(
    project_id: str,
    update_id: str,
    title: str = Form(...),
    text: str = Form(""),
    image: UploadFile | None = File(None),
    image_caption: str = Form(""),
    keep_existing_image: str = Form("no"),
):
    project = storage.get_project(project_id)
    if project is None:
        return RedirectResponse("/", status_code=303)

    current_update = None
    for update in project.get("updates", []):
        if update.get("id") == update_id:
            current_update = update
            break

    if current_update is None:
        return RedirectResponse(f"/projects/{project_id}", status_code=303)

    images = current_update.get("images", [])

    if keep_existing_image != "yes":
        images = []

    if image is not None and image.filename:
        ext = Path(image.filename).suffix.lower() or ".png"
        safe_name = (
            f"{storage.now_string().replace(':', '').replace(' ', '-')}-"
            f"{storage.slugify(Path(image.filename).stem)}{ext}"
        )

        target_dir = storage.UPLOADS / project_id / "updates"
        target_dir.mkdir(parents=True, exist_ok=True)

        target = target_dir / safe_name

        with target.open("wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        images = [
            {
                "path": f"assets/uploads/{project_id}/updates/{safe_name}",
                "caption": image_caption,
                "uploaded": storage.now_string(),
            }
        ]
    else:
        # No new image uploaded: only update caption of existing image, if present.
        if images and image_caption:
            images[0]["caption"] = image_caption

    storage.update_progress_update(
        project_id=project_id,
        update_id=update_id,
        title=title,
        text=text,
        images=images,
    )

    return RedirectResponse(f"/projects/{project_id}", status_code=303)



@app.post("/build")
def build():
    build_site()
    return RedirectResponse("/", status_code=303)


def main() -> None:
    storage.ensure_dirs()
    print("Starting Research Atlas editor at http://127.0.0.1:8000")
    uvicorn.run("research_atlas.editor:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
