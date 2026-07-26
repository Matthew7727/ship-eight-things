# -*- coding: utf-8 -*-
"""Generates the static site."""
import os, shutil
from projects import PROJECTS

import pathlib
OUT = str(pathlib.Path(__file__).resolve().parent.parent)  # repo root

# ─────────────────────────── shared shell ───────────────────────────

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800'
 '&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">')


def nav(active, depth):
    """depth 0 = root, 1 = inside /projects/"""
    up = "../" if depth else ""
    root = up + "index.html"
    out = ['<div class="group">Guide</div>']
    for anchor, label in [("how", "How this works"), ("rhythm", "The weekly rhythm"),
                          ("machine", "Your machine"), ("install", "Installing everything"),
                          ("github", "Git &amp; GitHub"), ("firstrepo", "Your first repo")]:
        cls = ' class="on"' if active == anchor else ''
        out.append(f'<a href="{root}#{anchor}"{cls}>{label}</a>')

    out.append('<div class="group">Projects</div>')
    for p in PROJECTS:
        cls = ' class="on"' if active == p["slug"] else ''
        href = f'{up}projects/{p["slug"]}.html'
        out.append(f'<a href="{href}"{cls}><span class="n">{p["num"]}</span>{p["title"]}</a>')

    out.append('<div class="group">Reference</div>')
    for anchor, label in [("stuck", "When you're stuck"), ("git-ref", "Git commands"),
                          ("errors", "Reading an error"), ("readme", "README template"),
                          ("ai", "Using AI"), ("mentor", "For the mentor")]:
        cls = ' class="on"' if active == anchor else ''
        out.append(f'<a href="{root}#{anchor}"{cls}>{label}</a>')
    return "\n    ".join(out)


def page(title, active, depth, body, subtitle="16 weeks &middot; 8 projects"):
    up = "../" if depth else ""
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
{FONTS}
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<button id="menu" aria-label="Open navigation">&#9776; Menu</button>
<div id="veil"></div>
<aside id="sidebar">
  <a class="brand" href="{up}index.html">
    <div class="mark">Aug &mdash; Nov 2026</div>
    <div class="bt">Ship Eight Things</div>
    <div class="sub">{subtitle}</div>
  </a>
  <nav id="nav">
    {nav(active, depth)}
  </nav>
</aside>
<main>
{body}
</main>
<script src="{up}assets/app.js"></script>
</body>
</html>
"""

# ─────────────────────────── project pages ───────────────────────────

def project_page(p, prev, nxt):
    s = []
    s.append(f'<a class="back" href="../index.html">&larr; All projects</a>')
    s.append('<div class="eyebrow">Project ' + p["num"] + ' &middot; ' + p["weeks"] + '</div>')
    s.append(f'<h2>{p["title"]}</h2>')
    s.append(f'<p class="lede">{p["summary"]}</p>')
    s.append(f'<div class="cmsg">{p["commit"]}</div>')
    s.append(p["intro"])

    # session jump list
    s.append('<div class="jump"><div class="jt">Sessions</div><ol>')
    for sess in p["sessions"]:
        s.append(f'<li><a href="#s{sess["n"]}">{sess["title"]}</a></li>')
    s.append('</ol></div>')

    for sess in p["sessions"]:
        s.append(f'<article class="session" id="s{sess["n"]}">')
        s.append(f'<div class="shead"><span class="snum">Session {sess["n"]}</span>'
                 f'<h3>{sess["title"]}</h3></div>')
        s.append(sess["teach"])
        s.append(f'<div class="sbuild"><b>Build this</b>{sess["build"]}</div>')
        s.append(f'<div class="scheck"><b>You should now be able to</b><p>{sess["check"]}</p></div>')
        s.append('</article>')

    s.append('<h3 class="sec">Traps to avoid</h3>')
    for t, d in p["traps"]:
        s.append(f'<div class="trap"><b>{t}</b><p>{d}</p></div>')

    s.append('<h3 class="sec">If you finish early</h3><ul class="stretch">')
    for x in p["stretch"]:
        s.append(f'<li>{x}</li>')
    s.append('</ul>')

    s.append(f'<div class="done big"><b>Definition of done</b>{p["done"]}</div>')

    s.append('<div class="pager">')
    if prev:
        s.append(f'<a class="pg" href="{prev["slug"]}.html"><span>&larr; Previous</span>'
                 f'<strong>{prev["num"]} &middot; {prev["title"]}</strong></a>')
    else:
        s.append('<a class="pg" href="../index.html#firstrepo"><span>&larr; Previous</span>'
                 '<strong>Setup &middot; Your first repo</strong></a>')
    if nxt:
        s.append(f'<a class="pg r" href="{nxt["slug"]}.html"><span>Next &rarr;</span>'
                 f'<strong>{nxt["num"]} &middot; {nxt["title"]}</strong></a>')
    else:
        s.append('<a class="pg r" href="../index.html#stuck"><span>Next &rarr;</span>'
                 '<strong>Reference &middot; When you\'re stuck</strong></a>')
    s.append('</div>')

    body = "<section>" + "\n".join(s) + "</section>"
    body = body.replace("{% raw %}", "").replace("{% endraw %}", "")
    return page(f'{p["num"]} {p["title"]} &mdash; Ship Eight Things', p["slug"], 1, body,
                subtitle=p["weeks"])

# ─────────────────────────── write ───────────────────────────

os.makedirs(f"{OUT}/projects", exist_ok=True)
os.makedirs(f"{OUT}/assets", exist_ok=True)

for i, p in enumerate(PROJECTS):
    prev = PROJECTS[i-1] if i > 0 else None
    nxt = PROJECTS[i+1] if i < len(PROJECTS)-1 else None
    with open(f'{OUT}/projects/{p["slug"]}.html', "w") as f:
        f.write(project_page(p, prev, nxt))

open(f"{OUT}/.nojekyll", "w").write("")
print("project pages written:", len(PROJECTS))

# ─────────────────────────── index ───────────────────────────
from index_content import INDEX_BODY

with open(f"{OUT}/index.html", "w") as f:
    f.write(page("Ship Eight Things — a four-month engineering guide", "how", 0, INDEX_BODY))

print("index written")
