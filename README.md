# Samuel Appiah Kubi — Portfolio

Static site built on the "homepage-3" template (same main.css / all.js, hero backgrounds unchanged).
Accent colour: #43B1E7 (deep tone #146E9A for small text on light backgrounds).

- `index.html`: home page
- `projects/`: one page per project; `pyunwrap.html` and `ps-gnn.html` are the flagship case studies
- `expertise/`: "What I do" pages: `index.html` (How I work) + one page per discipline
- `css/main.css`, `js/all.js`: template theme (recoloured) and scripts; `css/portfolio.css`: additions
- `img/`: images; `fx-*` are figures and charts from your pyunwrap and ps-gnn runs
- `assets/Samuel-Appiah-Kubi-CV.pdf`: linked from "Download CV"

## Editing
Home page `src/index.src.html` · projects `src/projects.py` · flagships `src/flagships.py` · What I do `src/expertise.py`.
Then run `python3 src/build.py`.

## Deploy to GitHub Pages
Copy everything into your `portfolio` repo root (replacing the old files), commit and push.
