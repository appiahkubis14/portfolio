"""Assemble index.html and projects/*.html.

Edit src/index.src.html for the home page and src/projects.py for project
content, then run:  python3 src/build.py
"""
from pathlib import Path
import html, re, sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'src'))
from projects import PROJECTS  # noqa: E402

E = html.escape
src = (ROOT / 'src' / 'index.src.html').read_text()

MARK = ('<g fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="28" cy="28" r="19"/>'
        '<ellipse cx="28" cy="28" rx="19" ry="7.5"/><path d="M28 9v38"/></g>'
        '<ellipse cx="28" cy="28" rx="27" ry="10" transform="rotate(-25 28 28)" fill="none" stroke="#43B1E7" stroke-width="1.8"/>'
        '<circle cx="51.5" cy="16.5" r="3.2" fill="#43B1E7"/>')
WORD = ('<text x="66" y="35.5" font-family="Roboto, Arial, sans-serif" font-size="20" font-weight="700" '
        'letter-spacing="3.2" fill="currentColor">APPIAH KUBI</text>')
TAG = ('<line x1="242" y1="13" x2="242" y2="43" stroke="currentColor" stroke-opacity=".45"/>'
       '<text font-family="Roboto, Arial, sans-serif" font-size="11.5" fill="currentColor" fill-opacity=".85">'
       '<tspan x="254" y="25">geospatial &amp;</tspan><tspan x="254" y="40">earth observation</tspan></text>')
LOGO_FULL = f'<svg class="site-logo" viewBox="0 0 364 56" role="img" aria-label="Samuel Appiah Kubi">{MARK}{WORD}{TAG}</svg>'
LOGO_SHORT = f'<svg class="site-logo" viewBox="0 0 234 56" role="img" aria-label="Samuel Appiah Kubi">{MARK}{WORD}</svg>'
ARROW = ('<svg class="icon" width="21" height="12" viewBox="0 0 21 12">'
         '<path fill-rule="evenodd" clip-rule="evenodd" d="M15 6.75L0 6.75L0 5.25L15 5.25V6.75Z"/>'
         '<path d="M21 5.99986L14.25 11.196L14.25 0.803711L21 5.99986Z"/></svg>')

def icon(body):
    return (f'<svg width="40" height="40" viewBox="0 0 40 40" fill="none" stroke="#1D40CA" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')

ICONS = {
    'ICON_SAR': icon('<rect x="14" y="8" width="8" height="6" rx="1" transform="rotate(-30 18 11)"/>'
                     '<path d="M6 6l7 4M23 15l7 4"/><path d="M14 22c2 4 6 6 10 6M10 24c3 6 9 9 15 9M18 20c1 2 3 3 5 3"/><path d="M4 36h32"/>'),
    'ICON_AI': icon('<rect x="10" y="10" width="20" height="20" rx="2"/><circle cx="20" cy="20" r="4"/>'
                    '<path d="M15 4v6M20 4v6M25 4v6M15 30v6M20 30v6M25 30v6M4 15h6M4 20h6M4 25h6M30 15h6M30 20h6M30 25h6"/>'),
    'ICON_DATA': icon('<path d="M20 5l15 7.5L20 20 5 12.5z"/><path d="M5 19.5L20 27l15-7.5"/><path d="M5 26.5L20 34l15-7.5"/>'),
    'ICON_CLOUD': icon('<path d="M12 24a7 7 0 0 1 1-13.9A9 9 0 0 1 30 12a6 6 0 0 1 0 12z"/>'
                       '<rect x="11" y="28" width="18" height="8" rx="1.5"/><path d="M15 32h.01M20 24v4"/>'),
    'ICON_LEAF': icon('<path d="M8 32C8 16 18 7 34 6c0 16-9 26-26 26z"/><path d="M8 32L24 16"/><path d="M14 26h6M18 22h5"/>'),
    'ICON_FIELD': icon('<rect x="14" y="6" width="12" height="9" rx="1.5"/><circle cx="20" cy="10.5" r="2"/>'
                       '<path d="M20 15v4M20 19L10 35M20 19l10 16M20 19v16"/>'),
}

CATS = {'systems': 'Systems & Backend', 'insar': 'InSAR', 'geoai': 'GeoAI', 'agri': 'Agriculture', 'env': 'Environment'}

# ---------------------------------------------------------------- home grid
def card_html(p):
    href = f'projects/{p["slug"]}.html'
    meta = ''.join(f'<span class="listing-meta__item text--primary">{E(t)}</span>' for t in p['tags'])
    return f'''						<article class="project-card" data-cats="{p["cls"]}">
							<div class="blog-post">
								<div class="blog-post__visual">
									<a href="{href}" class="blog-post__img sm" tabindex="-1" aria-hidden="true">
										<img src="img/{p["img"]}.jpg" alt="" loading="lazy">
									</a>
								</div>
								<div class="blog-post__content">
									<div class="listing-meta">{meta}</div>
									<h4 class="blog-post__title"><a href="{href}" class="project-card__link">{E(p["title"])}</a></h4>
									<span class="project-years">{E(p["years"])}</span>
									<div class="blog-post__description"><p>{E(p["card"])}</p></div>
									<span class="btn btn--link project-card__more">View case study</span>
								</div>
							</div>
						</article>'''

home = src.replace('{{LOGO_FULL}}', LOGO_FULL).replace('{{LOGO_SHORT}}', LOGO_SHORT).replace('{{ARROW}}', ARROW)
for k, v in ICONS.items():
    home = home.replace('{{' + k + '}}', v)
home = home.replace('{{PROJECTS}}', '\n'.join(card_html(p) for p in PROJECTS))
assert '{{' not in home, [l for l in home.splitlines() if '{{' in l][:3]
(ROOT / 'index.html').write_text(home)

# ---------------------------------------------------------------- detail pages
def rel(chunk):
    """Rewrite a chunk of the home page for use one folder down."""
    chunk = re.sub(r'href="#', 'href="../index.html#', chunk)
    chunk = re.sub(r'(src|href)="(img|assets|css|js)/', r'\1="../\2/', chunk)
    return chunk

header = rel(home[home.find('<header'):home.find('</header>') + 9])
footer = rel(home[home.find('<footer'):home.find('</footer>') + 9])
head_fonts = home[home.find('<link rel="preconnect"'):home.find('<link media="all" rel="stylesheet" href="css/main.css">')]
favicon = re.search(r'<link rel="icon"[^>]*>', home).group(0)

PREV = ('<svg class="icon" width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M15 7.5C15 3.36 11.64 0 7.5 0S0 3.36 0 7.5 3.36 15 7.5 15 15 11.64 15 7.5Z" fill="#1D40CA"/>'
        '<path fill-rule="evenodd" clip-rule="evenodd" d="M8.18 4.14L5.14 7.16a.48.48 0 0 0 0 .68l3.04 3.02a.48.48 0 0 0 .68-.67L6.04 7.5l2.82-2.69a.48.48 0 0 0-.68-.67Z" fill="white"/></svg>')
NEXT = ('<svg class="icon" width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M0 7.5C0 3.36 3.36 0 7.5 0S15 3.36 15 7.5 11.64 15 7.5 15 0 11.64 0 7.5Z" fill="#1D40CA"/>'
        '<path fill-rule="evenodd" clip-rule="evenodd" d="M6.82 4.14l3.04 3.02a.48.48 0 0 1 0 .68l-3.04 3.02a.48.48 0 0 1-.68-.67L8.96 7.5 6.14 4.81a.48.48 0 0 1 .68-.67Z" fill="white"/></svg>')

def related(p, n=3):
    mine = set(p['cls'].split())
    others = [q for q in PROJECTS if q is not p]
    others.sort(key=lambda q: -len(mine & set(q['cls'].split())))
    return others[:n]

def page_html(i, p):
    prev_p = PROJECTS[i - 1]; next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    tags = ''.join(f'<span class="listing-meta__item">{E(t)}</span>' for t in p['tags'])
    cats = ' · '.join(CATS[c] for c in p['cls'].split())
    metrics = ''.join(f'<li class="project-metric"><strong class="project-metric__value">{E(v)}</strong><span class="project-metric__label">{E(l)}</span></li>' for v, l in p['metrics'])
    steps = ''.join(f'''
								<li class="project-step">
									<span class="project-step__num">{k:02d}</span>
									<div class="project-step__body">
										<h4 class="project-step__title">{E(t)}</h4>
										<p>{E(d)}</p>
									</div>
								</li>''' for k, (t, d) in enumerate(p['approach'], 1))
    data = ''.join(f'<li><span class="tag-list__link">{E(d)}</span></li>' for d in p['data'])
    stack = ''.join(f'<li><span class="tag-list__link">{E(d)}</span></li>' for d in p['stack'])
    facts = [('Timeline', p['years']), ('Role', p['role'])]
    if p.get('location'): facts.append(('Location', p['location']))
    if p.get('status') and p['status'] != p['years']: facts.append(('Status', p['status']))
    facts.append(('Category', cats))
    facts_html = ''.join(f'<li class="project-facts__item"><span class="project-facts__label">{E(k)}</span><strong class="project-facts__value">{E(v)}</strong></li>' for k, v in facts)
    links_html = ''
    if p['links']:
        items = ''.join(f'<li><a href="{E(u)}" target="_blank" rel="noopener">{E(t)} <span aria-hidden="true">↗</span></a></li>' for t, u in p['links'])
        links_html = f'''
							<div class="widget">
								<h4 class="widget__title">Links</h4>
								<ul class="list list--border project-links">{items}</ul>
							</div>'''
    rel_html = ''.join(f'''
									<li>
										<div class="recent-post">
											<div class="recent-post__visual"><img src="../img/{q["img"]}.jpg" alt=""></div>
											<div class="recent-post__content">
												<div class="listing-meta"><span class="listing-meta__item text--primary">{E(q["tags"][0])}</span></div>
												<h4 class="recent-post__title"><a href="{q["slug"]}.html">{E(q["title"])}</a></h4>
											</div>
										</div>
									</li>''' for q in related(p))
    notes_html = ''
    if p.get('notes'):
        notes_html = f'''
							<div class="project-note">
								<h4 class="project-note__title">Status &amp; caveats</h4>
								<p>{E(p["notes"])}</p>
							</div>'''

    return f'''<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>{E(p["title"])} — Samuel Appiah Kubi</title>
	<meta name="description" content="{E(p["aim"])}">
	<meta name="author" content="Samuel Appiah Kubi">
	<meta property="og:title" content="{E(p["title"])} — Samuel Appiah Kubi">
	<meta property="og:description" content="{E(p["subtitle"])}">
	<meta property="og:image" content="../img/{p["img"]}-lg.jpg">
	<meta name="theme-color" content="#051c2c">
	{favicon}
	{head_fonts}<link media="all" rel="stylesheet" href="../css/main.css">
	<link media="all" rel="stylesheet" href="../css/portfolio.css">
</head>

<body class="page-project">
	<div class="wrapper wrapper--offset-0">
		{header}
		<main class="main">
			<section class="section-intro project-intro text--white">
				<div class="container">
					<div class="listing-meta">{tags}</div>
					<h1>{E(p["title"])}</h1>
					<h6 class="headtitle">{E(p["subtitle"])}</h6>
				</div>
				<div class="bg-stretch">
					<img src="../img/{p["img"]}-lg.jpg" alt="">
				</div>
			</section>
			<section class="section-breadcrumbs">
				<div class="container">
					<ul class="breadcrumbs">
						<li class="breadcrumbs__item"><a href="../index.html" class="breadcrumbs__link">Home</a></li>
						<li class="breadcrumbs__item"><a href="../index.html#projects" class="breadcrumbs__link">Projects</a></li>
						<li class="breadcrumbs__item current">{E(p["title"])}</li>
					</ul>
				</div>
			</section>
			<section class="section geo--topo project-body">
				<div class="container">
					<div class="main-wrapper">
						<div class="main-content">
							<h4 class="headtitle">Project aim</h4>
							<p class="project-aim">{E(p["aim"])}</p>
							<ul class="project-metrics">{metrics}</ul>

							<div class="row mb--3 project-row">
								<div class="col-6">
									<img class="project-figure" src="../img/{p["img"]}-lg.jpg" alt="Illustrative map for {E(p["title"])}">
									<span class="project-figure__caption">Illustrative graphic</span>
								</div>
								<div class="col-6">
									<h3>Overview</h3>
									<p>{E(p["overview"])}</p>
								</div>
							</div>

							<div class="row mb--3 project-row">
								<div class="col-6">
									<h3>The challenge</h3>
									<p>{E(p["challenge"])}</p>
								</div>
								<div class="col-6">
									<h3>Data &amp; inputs</h3>
									<ul class="tag-list project-tags">{data}</ul>
								</div>
							</div>

							<h4 class="headtitle">Approach</h4>
							<ol class="project-steps">{steps}
							</ol>

							<div class="row mb--3 project-row">
								<div class="col-6">
									<h3>Results</h3>
									<p>{E(p["results"])}</p>
								</div>
								<div class="col-6">
									<h3>Validation</h3>
									<p>{E(p["validation"])}</p>
								</div>
							</div>{notes_html}

							<hr class="divider">
							<ul class="post-pagination">
								<li class="post-pagination__item prev">
									<a href="{prev_p["slug"]}.html" class="post-pagination__link" data-title="{E(prev_p["title"])}">{PREV}
										Previous project
									</a>
								</li>
								<li class="post-pagination__item next">
									<a href="{next_p["slug"]}.html" class="post-pagination__link" data-title="{E(next_p["title"])}">{NEXT}
										Next project
									</a>
								</li>
							</ul>
						</div>
						<aside class="sidebar">
							<div class="widget project-facts">
								<h4 class="widget__title">Project facts</h4>
								<ul class="project-facts__list">{facts_html}</ul>
							</div>
							<div class="widget">
								<h4 class="widget__title">Tech stack</h4>
								<ul class="tag-list project-tags">{stack}</ul>
							</div>{links_html}
							<div class="widget">
								<h4 class="widget__title">Related projects</h4>
								<ul class="recent-list">{rel_html}
								</ul>
							</div>
							<div class="widget project-cta bg--gradient text--white">
								<h3 class="project-cta__title">Interested in this work?</h3>
								<p>Happy to talk about collaboration, data or code.</p>
								<a href="../index.html#contact" class="btn btn--white">
									Get In Touch
									{ARROW}
								</a>
							</div>
						</aside>
					</div>
				</div>
			</section>
		</main>
		{footer}
	</div>
	<script src="../js/all.js"></script>
	<script>
		document.querySelectorAll('.nav-drop a[href*="#"]').forEach(function (a) {{
			a.addEventListener('click', function () {{ document.body.classList.remove('nav-active'); }});
		}});
	</script>
</body>

</html>
'''

out_dir = ROOT / 'projects'
out_dir.mkdir(exist_ok=True)
for f in out_dir.glob('*.html'):
    f.unlink()
for i, p in enumerate(PROJECTS):
    (out_dir / f'{p["slug"]}.html').write_text(page_html(i, p))
print(f'wrote index.html + {len(PROJECTS)} project pages')
