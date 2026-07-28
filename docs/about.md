# About

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
