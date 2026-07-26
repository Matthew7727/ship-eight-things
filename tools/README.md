# tools

Optional. The site is plain HTML — edit `index.html` and `projects/*.html` directly
and you never need to touch this.

These scripts generated the eight project pages from a single content file, which is
useful if you want to add a project or change something across every page at once
(the nav, the footer, the page shell).

```
projects.py        the eight projects as structured content
index_content.py   the index page body
build.py           renders both into HTML
```

To regenerate, from the repo root:

```
python3 tools/build.py
```

It overwrites `index.html` and everything in `projects/`, so commit before you run it.
`assets/style.css` and `assets/app.js` are hand-written and never touched by the build.
