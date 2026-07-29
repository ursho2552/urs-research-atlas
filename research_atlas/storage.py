from __future__ import annotations

from datetime import datetime, date
from pathlib import Path
import re
import shutil
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
PROJECTS = CONTENT / "projects"
UPLOADS = ROOT / "docs" / "assets" / "uploads"
DOCS = ROOT / "docs"

STATUSES = ["active", "paused", "completed", "archived"]
TASK_STATUSES = ["todo", "in_progress", "done", "blocked"]
PRIORITIES = ["low", "medium", "high"]


def ensure_dirs() -> None:
    PROJECTS.mkdir(parents=True, exist_ok=True)
    UPLOADS.mkdir(parents=True, exist_ok=True)
    (DOCS / "projects").mkdir(parents=True, exist_ok=True)


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text or "item"


def now_string() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def project_path(project_id: str) -> Path:
    return PROJECTS / f"{project_id}.yml"


def load_project(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("tasks", [])
    data.setdefault("updates", [])
    data.setdefault("images", [])
    data.setdefault("tags", [])
    return data


def save_project(project: dict[str, Any]) -> None:
    ensure_dirs()
    path = project_path(project["id"])
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(project, f, sort_keys=False, allow_unicode=True)


def list_projects() -> list[dict[str, Any]]:
    ensure_dirs()
    projects = [load_project(p) for p in sorted(PROJECTS.glob("*.yml"))]
    return sorted(projects, key=lambda p: p.get("title", p.get("id", "")).lower())


def get_project(project_id: str) -> dict[str, Any] | None:
    path = project_path(project_id)
    if not path.exists():
        return None
    return load_project(path)


def create_project(title: str, summary: str, area: str, status: str = "active", tags: str = "") -> dict[str, Any]:
    ensure_dirs()
    base_id = slugify(title)
    project_id = base_id
    i = 2
    while project_path(project_id).exists():
        project_id = f"{base_id}-{i}"
        i += 1
    project = {
        "id": project_id,
        "title": title,
        "summary": summary,
        "area": area,
        "status": status,
        "created": now_string(),
        "updated": now_string(),
        "tags": [t.strip() for t in tags.split(",") if t.strip()],
        "links": {},
        "tasks": [],
        "updates": [],
        "images": [],
    }
    save_project(project)
    return project


def update_project(project_id: str, **fields: Any) -> dict[str, Any]:
    project = get_project(project_id)
    if project is None:
        raise ValueError(f"Project not found: {project_id}")
    for key, value in fields.items():
        if value is not None:
            project[key] = value
    project["updated"] = now_string()
    save_project(project)
    return project


def add_task(project_id: str, title: str, priority: str = "medium", due_date: str = "", status: str = "todo") -> dict[str, Any]:
    project = get_project(project_id)
    if project is None:
        raise ValueError(f"Project not found: {project_id}")
    task_id = f"{project_id}-{slugify(title)}"
    existing = {task.get("id") for task in project.get("tasks", [])}
    base = task_id
    i = 2
    while task_id in existing:
        task_id = f"{base}-{i}"
        i += 1
    project.setdefault("tasks", []).append({
        "id": task_id,
        "title": title,
        "status": status,
        "priority": priority,
        "due_date": due_date or "",
        "created": now_string(),
        "updated": now_string(),
    })
    project["updated"] = now_string()
    save_project(project)
    return project


def set_task_status(project_id: str, task_id: str, status: str) -> dict[str, Any]:
    project = get_project(project_id)
    if project is None:
        raise ValueError(f"Project not found: {project_id}")
    for task in project.get("tasks", []):
        if task.get("id") == task_id:
            task["status"] = status
            task["updated"] = now_string()
            if status == "done":
                task["completed"] = now_string()
            break
    project["updated"] = now_string()
    save_project(project)
    return project

def add_update(
    project_id: str,
    title: str,
    text: str,
    images: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    project = get_project(project_id)
    if project is None:
        raise ValueError(f"Project not found: {project_id}")

    update_id = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{slugify(title)}"

    update = {
        "id": update_id,
        "date": now_string(),
        "title": title,
        "text": text,
    }

    if images:
        update["images"] = images

    project.setdefault("updates", []).append(update)
    project["updated"] = now_string()
    save_project(project)
    return project


def save_uploaded_image(project_id: str, source_path: Path, filename: str, caption: str = "") -> dict[str, Any]:
    project = get_project(project_id)
    if project is None:
        raise ValueError(f"Project not found: {project_id}")
    ext = Path(filename).suffix.lower() or ".png"
    safe_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{slugify(Path(filename).stem)}{ext}"
    target_dir = UPLOADS / project_id
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / safe_name
    shutil.copyfile(source_path, target)
    rel = f"assets/uploads/{project_id}/{safe_name}"
    image = {
        "path": rel,
        "caption": caption,
        "uploaded": now_string(),
    }
    project.setdefault("images", []).append(image)
    project["updated"] = now_string()
    save_project(project)
    return project


def task_urgency(task: dict[str, Any]) -> int:
    if task.get("status") == "done":
        return -1
    score = 0
    priority = task.get("priority", "medium")
    score += {"high": 30, "medium": 15, "low": 5}.get(priority, 0)
    if task.get("status") == "in_progress":
        score += 10
    if task.get("status") == "blocked":
        score += 20
    due = task.get("due_date") or ""
    if due:
        try:
            d = date.fromisoformat(due)
            days = (d - date.today()).days
            if days < 0:
                score += 100
            elif days <= 3:
                score += 60
            elif days <= 7:
                score += 40
            elif days <= 14:
                score += 20
        except ValueError:
            pass
    return score

def save_update_image(
    project_id: str,
    update_id: str,
    source_path: Path,
    filename: str,
    caption: str = "",
) -> dict[str, Any]:
    ext = Path(filename).suffix.lower() or ".png"
    safe_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{slugify(Path(filename).stem)}{ext}"

    target_dir = UPLOADS / project_id / "updates" / update_id
    target_dir.mkdir(parents=True, exist_ok=True)

    target = target_dir / safe_name
    shutil.copyfile(source_path, target)

    return {
        "path": f"assets/uploads/{project_id}/updates/{update_id}/{safe_name}",
        "caption": caption,
        "uploaded": now_string(),
    }

def all_tasks_with_project() -> list[dict[str, Any]]:
    rows = []
    for project in list_projects():
        for task in project.get("tasks", []):
            row = dict(task)
            row["project_id"] = project["id"]
            row["project_title"] = project["title"]
            row["urgency"] = task_urgency(task)
            rows.append(row)
    return rows

def update_progress_update(
    project_id: str,
    update_id: str,
    title: str,
    text: str,
    images: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    project = get_project(project_id)
    if project is None:
        raise ValueError(f"Project not found: {project_id}")

    for update in project.get("updates", []):
        if update.get("id") == update_id:
            update["title"] = title
            update["text"] = text
            update["updated"] = now_string()

            if images is not None:
                update["images"] = images

            break
    else:
        raise ValueError(f"Update not found: {update_id}")

    project["updated"] = now_string()
    save_project(project)
    return project


def add_image_to_update(
    project_id: str,
    update_id: str,
    source_path: Path,
    filename: str,
    caption: str = "",
) -> dict[str, Any]:
    project = get_project(project_id)
    if project is None:
        raise ValueError(f"Project not found: {project_id}")

    update = None
    for candidate in project.get("updates", []):
        if candidate.get("id") == update_id:
            update = candidate
            break

    if update is None:
        raise ValueError(f"Update not found: {update_id}")

    ext = Path(filename).suffix.lower() or ".png"
    safe_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{slugify(Path(filename).stem)}{ext}"

    target_dir = UPLOADS / project_id / "updates"
    target_dir.mkdir(parents=True, exist_ok=True)

    target = target_dir / safe_name
    shutil.copyfile(source_path, target)

    image = {
        "path": f"assets/uploads/{project_id}/updates/{safe_name}",
        "caption": caption,
        "uploaded": now_string(),
    }

    update.setdefault("images", []).append(image)
    update["updated"] = now_string()
    project["updated"] = now_string()

    save_project(project)
    return project

