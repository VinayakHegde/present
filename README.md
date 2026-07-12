# Interview Prep

One place to prepare for interviews, organized by topic instead of by company.

## Run

```sh
./serve.py            # http://localhost:8000 (any port: ./serve.py 9000)
```

`index.html` is an app shell: sidebar navigation + the selected page in an iframe,
with real path routing (e.g. `/system-design/stock-price-alerts`). The shell needs the
server because extensionless routes fall back to `index.html`.

Every content page is fully self-contained — to troubleshoot one, open the `.html`
file directly in a browser (or hit its real URL, e.g.
`http://localhost:8000/system-design/stock-price-alerts.html`).

## Structure

```
index.html                  app shell (nav, routing, theme toggle) — no content
serve.py                    static server with SPA fallback
behavioural/prep.html       about-me, AI & ways-of-working Q&A, checklists
behavioural/stories.html    story bank + competency mapping (synced from Notion)
behavioural/story/*.html    one page per story — Notion is the source of truth
system-design/*.html        system design write-ups
case-studies/*.html         project walkthroughs (one is a reveal.js deck)
technical/reference.html    technical reference (FE, AI engineering, infra, security)
pics/                       shared diagrams
```

## Deploying to GitHub Pages

Push the repo and enable Pages — no build step. Deep links work via `404.html`:
GitHub serves it for any path that isn't a real file, and it bounces the requested
route to the shell (`/?p=<route>`), which restores the URL with `replaceState`.
The shell auto-detects its base path, so both `username.github.io` and
`username.github.io/<repo>/` work. (`.nojekyll` disables Jekyll processing.)

Locally, `serve.py` plays the same fallback role — a plain
`python3 -m http.server` will 404 on refresh of pretty routes.

## Theming

Light/dark follows the system by default. The shell's toggle (top-left) cycles
auto → light → dark and persists to `localStorage` (`prep-theme`); standalone pages
read the same key, so they match.

## Adding a page

1. Create a self-contained `.html` under the right category folder (copy the theme
   head-script + palette block from any existing page).
2. Add one line to the `PAGES` array in `index.html`.
