# Ship Eight Things

A four-month, project-based route into software engineering, written for a complete beginner
working evenings and weekends on a MacBook Neo or a Windows laptop using WSL.

**Live site:** https://matthew7727.github.io/ship-eight-things/

## What's in it

- **Setup** — macOS from a fresh machine, or Windows via WSL: terminal, Homebrew or apt, Python,
  VS Code, git, SSH keys, virtual environments, and the specific compromises an 8GB machine calls for.
- **Eight project guides** — six sessions each, with the new concepts taught as they come up,
  the traps that catch people, stretch goals, and a definition of done.
- **Reference** — a stuck protocol, git commands, how to read a traceback, a README template,
  and rules for using AI while you're still learning.
- **Mentor notes** — how to run the weekly pairing session without accidentally doing the work.

| # | Project | Weeks | Teaches |
|---|---------|-------|---------|
| 01 | Terminal toolkit | 1–2 | Variables, loops, functions, the commit loop |
| 02 | Expense tracker | 3–4 | Lists, dictionaries, files, JSON |
| 03 | Weather client | 5–6 | HTTP, APIs, secrets, error handling |
| 04 | Refactor & test | 7–8 | pytest, classes, modules, changing code safely |
| 05 | First web app | 9–10 | Flask, HTML, templates, forms |
| 06 | Database & deploy | 11–12 | SQL, injection, production config, deployment |
| 07 | Accounts & auth | 13–14 | Hashing, sessions, foreign keys, authorisation |
| 08 | Add a brain | 15–16 | Model APIs, structured output, graceful degradation |

## Structure

```
index.html                 setup guide, project index, reference
projects/*.html            the eight project guides
assets/style.css           all styling
assets/app.js              copy buttons, scrollspy, mobile nav
.nojekyll                  tells GitHub Pages to serve files as-is
```

No build step, no dependencies, no framework. Edit the HTML and push.

## Publishing

Pushed to `main`, then Settings → Pages → Source: `main` / root.
Give it a minute or two on the first deploy.
