# Samuel Appiah Kubi — Portfolio

Static site built on the "homepage-3" template (same main.css / all.js, hero backgrounds unchanged).

- `index.html`: home page
- `projects/*.html`: one detail page per project
- `css/main.css`, `js/all.js`: the original template theme and scripts
- `css/portfolio.css`: additions (logo, warm section surfaces, project grid, project pages, footer, mobile timeline)
- `img/`: template hero backgrounds, your photo, venture logos, warm surfaces (`bg-warm-*.jpg`), footer night-lights image, illustrative EO graphics (`p-*.jpg`, `v-*.jpg`)
- `assets/Samuel-Appiah-Kubi-CV.pdf`: linked from "Download CV"

## Editing
- Home page text: `src/index.src.html`
- Project content (cards and detail pages): `src/projects.py`
- Then run `python3 src/build.py` to regenerate `index.html` and `projects/`.

## Deploy to GitHub Pages
Copy everything into your `portfolio` repo root (replacing the old files), commit and push.
