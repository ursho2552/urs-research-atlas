# Research Atlas

Research Atlas is a local-first, Git-backed project showcase tool for researchers.

It lets you run a local browser editor to add projects, tasks, progress updates, and images. The content is stored as YAML and image files in this repository. A build script then generates a static MkDocs website that can be published with GitLab Pages.

## Quick start

```bash
nix develop
python -m research_atlas.editor
```

Open the local address printed in the terminal, usually:

```text
http://127.0.0.1:8000
```

To build and preview the public site:

```bash
python -m research_atlas.build
mkdocs serve
```

## Publishing with GitLab Pages

Commit and push the repository to GitLab. The included `.gitlab-ci.yml` builds the static site and publishes it with GitLab Pages on the default branch.

```bash
git add .
git commit -m "Update Research Atlas"
git push
```

## What is stored where?

```text
content/projects/          Project YAML files
docs/assets/uploads/       Uploaded images
docs/                      Generated static website pages
research_atlas/            Local editor and build code
```

Do not manually edit generated pages unless you are experimenting. The preferred workflow is to edit content through the local editor and regenerate the site.
