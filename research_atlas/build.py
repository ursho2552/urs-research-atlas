from __future__ import annotations

from pathlib import Path
from html import escape

from .storage import DOCS, ensure_dirs, list_projects, all_tasks_with_project, task_urgency


def badge(status: str) -> str:
    return f'<span class="ra-badge ra-badge-{escape(status)}">{escape(status.replace("_", " "))}</span>'


def progress(project: dict) -> tuple[int, int, int]:
    tasks = project.get("tasks", [])
    total = len(tasks)
    done = sum(1 for t in tasks if t.get("status") == "done")
    pct = round(done / total * 100) if total else 0
    return done, total, pct


def link_for_project(project_id: str) -> str:
    return f"projects/{project_id}/"


def render_project_card(project: dict) -> str:
    done, total, pct = progress(project)
    tags = "".join(f'<span class="ra-tag">{escape(tag)}</span>' for tag in project.get("tags", []))
    return f"""
<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>{escape(project.get('title', project['id']))}</h3>
      <p class="ra-muted">{escape(project.get('area', 'Research project'))}</p>
    </div>
    {badge(project.get('status', 'active'))}
  </div>
  <p>{escape(project.get('summary', ''))}</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: {pct}%"></div></div>
  <p class="ra-muted">{done} / {total} tasks completed</p>
  <div class="ra-tags">{tags}</div>
  <a class="ra-button" href="{link_for_project(project['id'])}">View project</a>
</div>
"""


def build_home(projects: list[dict]) -> None:
    active = [p for p in projects if p.get("status") == "active"]
    completed = [p for p in projects if p.get("status") == "completed"]
    tasks = all_tasks_with_project()
    open_tasks = [t for t in tasks if t.get("status") != "done"]
    done_tasks = [t for t in tasks if t.get("status") == "done"]
    urgent = sorted([t for t in open_tasks if t.get("urgency", 0) >= 0], key=lambda t: t.get("urgency", 0), reverse=True)[:5]

    project_cards = "\n".join(render_project_card(p) for p in projects)
    urgent_items = "\n".join(
        f"""
<div class="ra-list-item">
  <strong>{escape(t.get('title', 'Untitled task'))}</strong>
  <span>{escape(t.get('project_title', ''))} · {escape(t.get('priority', 'medium'))} · due {escape(t.get('due_date') or 'not set')}</span>
</div>
"""
        for t in urgent
    ) or '<p class="ra-muted">No open tasks yet.</p>'

    updates = []
    for p in projects:
        for u in p.get("updates", []):
            row = dict(u)
            row["project_title"] = p.get("title", p["id"])
            updates.append(row)
    updates = sorted(updates, key=lambda u: u.get("date", ""), reverse=True)[:4]
    update_items = "\n".join(
        f"""
<div class="ra-list-item">
  <strong>{escape(u.get('title', 'Update'))}</strong>
  <span>{escape(u.get('project_title', ''))} · {escape(u.get('date', ''))}</span>
</div>
"""
        for u in updates
    ) or '<p class="ra-muted">No progress updates yet.</p>'

    areas = sorted({p.get("area", "Research") for p in projects})
    area_items = "".join(f"<li>{escape(area)}</li>" for area in areas) or "<li>No areas yet</li>"

    content = f"""# Research Atlas

<div class="ra-page">

<section class="ra-hero">
  <p class="ra-eyebrow">Git-backed research showcase</p>
  <h1>Research Atlas</h1>
  <p>A local-first project showcase for researchers. Add projects, tasks, updates, and images with the local editor, then publish with GitLab Pages.</p>
  <div class="ra-actions">
    <a class="ra-button ra-button-primary" href="projects/">Explore projects</a>
    <a class="ra-button" href="todo/">View todo list</a>
    <a class="ra-button" href="gallery/">View gallery</a>
  </div>
</section>

<section class="ra-kpi-grid">
  <div class="ra-kpi-card"><span>Active projects</span><strong>{len(active)}</strong></div>
  <div class="ra-kpi-card"><span>Completed projects</span><strong>{len(completed)}</strong></div>
  <div class="ra-kpi-card"><span>Open tasks</span><strong>{len(open_tasks)}</strong></div>
  <div class="ra-kpi-card"><span>Done tasks</span><strong>{len(done_tasks)}</strong></div>
</section>

<section class="ra-dashboard">
  <aside class="ra-sidebar">
    <h2>Research areas</h2>
    <ul>{area_items}</ul>
  </aside>

  <main class="ra-main">
    <h2>Featured projects</h2>
    <div class="ra-project-grid">{project_cards}</div>
  </main>

  <aside class="ra-right">
    <div class="ra-panel">
      <h2>Most urgent tasks</h2>
      {urgent_items}
    </div>
    <div class="ra-panel">
      <h2>Recent updates</h2>
      {update_items}
    </div>
  </aside>
</section>

</div>
"""
    (DOCS / "index.md").write_text(content, encoding="utf-8")


def build_projects_index(projects: list[dict]) -> None:
    cards = "\n".join(render_project_card(p).replace(f'href="projects/{p["id"]}/"', f'href="{p["id"]}/"') for p in projects)
    content = f"""# Projects

<div class="ra-page ra-simple-page">
<p class="ra-lead">Browse the projects documented in this Research Atlas.</p>
<div class="ra-project-grid">{cards}</div>
</div>
"""
    (DOCS / "projects" / "index.md").write_text(content, encoding="utf-8")

def render_update(update: dict) -> str:
    update_images = "\n".join(
        f"<figure class='ra-figure'>"
        f"<img class='ra-lightbox-image' "
        f"src='../../{escape(img.get('path', ''))}' "
        f"alt='{escape(img.get('caption') or update.get('title', 'Update image'))}'>"
        f"<figcaption>{escape(img.get('caption', ''))}</figcaption>"
        f"</figure>"
        for img in update.get("images", [])
    )

    image_block = ""
    if update_images:
        image_block = f"""
<div class="ra-gallery-grid">
{update_images}
</div>
"""

    return f"""
### {escape(update.get('title', 'Update'))}

**{escape(update.get('date', ''))}**

{update.get('text', '')}

{image_block}
"""

def build_project_page(project: dict) -> None:
    done, total, pct = progress(project)
    tasks = project.get("tasks", [])
    task_rows = "\n".join(
        f"| {'✅' if t.get('status') == 'done' else '⬜'} | {escape(t.get('title', ''))} | {escape(t.get('status', ''))} | {escape(t.get('priority', ''))} | {escape(t.get('due_date') or '—')} |"
        for t in tasks
    ) or "| — | No tasks yet | — | — | — |"
    updates = "\n".join(
        render_update(u)
        for u in sorted(project.get("updates", []), key=lambda u: u.get("date", ""), reverse=True)
    ) or "No updates yet."

    tags = " ".join(f"`{tag}`" for tag in project.get("tags", []))

    content = f"""# {project.get('title', project['id'])}

<div class="ra-page ra-simple-page" markdown="1">

{badge(project.get('status', 'active'))}

**Area:** {project.get('area', 'Research')}  
**Updated:** {project.get('updated', '')}  
**Tags:** {tags or '—'}

## Summary

{project.get('summary', '')}

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: {pct}%"></div></div>

{done} / {total} tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
{task_rows}

## Updates

{updates}

</div>
"""
    (DOCS / "projects" / f"{project['id']}.md").write_text(content, encoding="utf-8")


def build_todo() -> None:
    tasks = [t for t in all_tasks_with_project() if t.get("status") != "done"]
    tasks = sorted(tasks, key=lambda t: t.get("urgency", 0), reverse=True)
    rows = "\n".join(
        f"| {escape(t.get('project_title', ''))} | {escape(t.get('title', ''))} | {escape(t.get('status', ''))} | {escape(t.get('priority', ''))} | {escape(t.get('due_date') or '—')} | {t.get('urgency', 0)} |"
        for t in tasks
    ) or "| — | No open tasks | — | — | — | — |"
    content = f"""# Todo

<div class="ra-page ra-simple-page" markdown="1">

This page is generated automatically from all project tasks and sorted by urgency.

| Project | Task | Status | Priority | Due date | Urgency |
| --- | --- | --- | --- | --- | ---: |
{rows}

</div>
"""
    (DOCS / "todo.md").write_text(content, encoding="utf-8")


def build_gallery(projects: list[dict]) -> None:
    figures = []
    for project in projects:
        for update in project.get("updates", []):
            for img in update.get("images", []):
                figures.append(
                    f"<figure class='ra-figure'>"
                    f"<img class='ra-lightbox-image' "
                    f"src='../{escape(img.get('path', ''))}' "
                    f"alt='{escape(img.get('caption') or update.get('title', 'Update image'))}'>"
                    f"<figcaption>"
                    f"<strong>{escape(project.get('title', ''))}</strong><br>"
                    f"{escape(update.get('title', 'Update'))} · {escape(update.get('date', ''))}<br>"
                    f"{escape(img.get('caption', ''))}"
                    f"</figcaption>"
                    f"</figure>"
                )

    content = f"""# Gallery

<div class="ra-page ra-simple-page">

<p class="ra-lead">Images and screenshots attached to project updates.</p>

<div class="ra-gallery-grid">
{''.join(figures) or '<p class="ra-muted">No update images uploaded yet.</p>'}
</div>

</div>
"""
    (DOCS / "gallery.md").write_text(content, encoding="utf-8")


def build_about() -> None:
    content = """# About

<div class="ra-page ra-simple-page" markdown="1">

Research Atlas is a local-first, Git-backed project showcase tool for researchers.

Use the local editor to maintain project descriptions, tasks, progress updates, and images. The static site is generated from repository content and can be published with GitLab Pages.

## Local workflow

```bash
python -m research_atlas.editor
python -m research_atlas.build
mkdocs serve
```

## Publishing workflow

```bash
git add .
git commit -m "Update Research Atlas"
git push
```

</div>
"""
    (DOCS / "about.md").write_text(content, encoding="utf-8")


def main() -> None:
    ensure_dirs()
    projects = list_projects()
    build_home(projects)
    build_projects_index(projects)
    for project in projects:
        build_project_page(project)
    build_todo()
    build_gallery(projects)
    build_about()
    print("Generated Research Atlas site content.")


if __name__ == "__main__":
    main()
