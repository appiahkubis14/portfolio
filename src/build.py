"""Assemble index.html and projects/*.html.

Edit src/index.src.html for the home page and src/projects.py for project
content, then run:  python3 src/build.py
"""
from pathlib import Path
import html, re, sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'src'))
from projects import PROJECTS  # noqa: E402
from expertise import HUB, AREAS  # noqa: E402
from flagships import FLAGSHIPS  # noqa: E402
ALL = FLAGSHIPS + PROJECTS

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
    return (f'<svg width="40" height="40" viewBox="0 0 40 40" fill="none" stroke="#43B1E7" stroke-width="1.6" '
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
def flag_html(p):
    href = f'projects/{p["slug"]}.html'
    mets = ''.join(f'<li><strong>{E(v)}</strong><span>{E(l)}</span></li>' for v, l in p['metrics'][:3])
    return f'''						<article class="flagship">
							<a href="{href}" class="flagship__visual" tabindex="-1" aria-hidden="true"><img src="img/{p["img"]}-lg.jpg" alt="" loading="lazy"></a>
							<div class="flagship__body">
								<span class="flagship__badge">Flagship research · {E(p["tags"][1])}</span>
								<h3 class="flagship__title"><a href="{href}">{E(p["short"])}</a></h3>
								<p class="flagship__sub">{E(p["subtitle"])}</p>
								<p class="flagship__pitch">{E(p["pitch"])}</p>
								<ul class="flagship__metrics">{mets}</ul>
								<a href="{href}" class="btn btn--primary">Read the case study {ARROW}</a>
							</div>
						</article>'''
home = home.replace('{{FLAGSHIPS}}', '\n'.join(flag_html(p) for p in FLAGSHIPS))
home = home.replace('{{PROJECTS}}', '\n'.join(card_html(p) for p in PROJECTS))
assert '{{' not in home, [l for l in home.splitlines() if '{{' in l][:3]
(ROOT / 'index.html').write_text(home)

# ---------------------------------------------------------------- detail pages
def rel(chunk):
    """Rewrite a chunk of the home page for use one folder down."""
    chunk = re.sub(r'href="#', 'href="../index.html#', chunk)
    chunk = re.sub(r'(src|href)="(img|assets|css|js|projects|expertise)/', r'\1="../\2/', chunk)
    return chunk

header = rel(home[home.find('<header'):home.find('</header>') + 9])
footer = rel(home[home.find('<footer'):home.find('</footer>') + 9])
head_fonts = home[home.find('<link rel="preconnect"'):home.find('<link media="all" rel="stylesheet" href="css/main.css">')]
favicon = re.search(r'<link rel="icon"[^>]*>', home).group(0)

PREV = ('<svg class="icon" width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M15 7.5C15 3.36 11.64 0 7.5 0S0 3.36 0 7.5 3.36 15 7.5 15 15 11.64 15 7.5Z" fill="#43B1E7"/>'
        '<path fill-rule="evenodd" clip-rule="evenodd" d="M8.18 4.14L5.14 7.16a.48.48 0 0 0 0 .68l3.04 3.02a.48.48 0 0 0 .68-.67L6.04 7.5l2.82-2.69a.48.48 0 0 0-.68-.67Z" fill="white"/></svg>')
NEXT = ('<svg class="icon" width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M0 7.5C0 3.36 3.36 0 7.5 0S15 3.36 15 7.5 11.64 15 7.5 15 0 11.64 0 7.5Z" fill="#43B1E7"/>'
        '<path fill-rule="evenodd" clip-rule="evenodd" d="M6.82 4.14l3.04 3.02a.48.48 0 0 1 0 .68l-3.04 3.02a.48.48 0 0 1-.68-.67L8.96 7.5 6.14 4.81a.48.48 0 0 1 .68-.67Z" fill="white"/></svg>')

def related(p, n=3):
    mine = set(p['cls'].split())
    others = [q for q in ALL if q is not p]
    others.sort(key=lambda q: -len(mine & set(q['cls'].split())))
    return others[:n]

def page_html(i, p):
    prev_p = ALL[i - 1]; next_p = ALL[(i + 1) % len(ALL)]
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
    flag_top = flag_mid = flag_lim = ''
    if p.get('flagship'):
        inno = ''.join(f'<li class="xp-diff"><span class="xp-diff__num">{k}</span><h4 class="xp-diff__title">{E(t)}</h4><p>{E(d)}</p></li>' for k, (t, d) in enumerate(p['innovation'], 1))
        flag_top = f'''
							<p class="xp-why">{E(p["pitch"])}</p>
							<h4 class="headtitle">What is new</h4>
							<ul class="xp-diffs xp-diffs--wide">{inno}</ul>'''
        spec = ''.join(f'<tr><th scope="row">{E(k)}</th><td>{E(v)}</td></tr>' for k, v in p['spec'])
        b = p['benchmark']
        bh = ''.join(f'<th scope="col">{E(h)}</th>' for h in b['headers'])
        br = ''.join('<tr>' + ''.join((f'<th scope="row">{E(c)}</th>' if j == 0 else f'<td>{E(c)}</td>') for j, c in enumerate(r)) + '</tr>' for r in b['rows'])
        figs = ''.join(f'''
								<figure class="flag-fig">
									<a href="../img/{f}" target="_blank" rel="noopener"><img src="../img/{f}" alt="{E(cap)}" loading="lazy"></a>
									<figcaption><span class="flag-fig__src">{E(src)}</span>{E(cap)}</figcaption>
								</figure>''' for f, cap, src in p['figures'])
        flag_mid = f'''
							<h4 class="headtitle">Model &amp; training setup</h4>
							<div class="flag-table-wrap"><table class="flag-table flag-table--spec"><tbody>{spec}</tbody></table></div>

							<h4 class="headtitle">Benchmark</h4>
							<div class="flag-table-wrap"><table class="flag-table"><caption>{E(b["caption"])}</caption><thead><tr>{bh}</tr></thead><tbody>{br}</tbody></table></div>

							<h4 class="headtitle">Figures from the run</h4>
							<div class="flag-figs">{figs}
							</div>'''
        lim = ''.join(f'<li>{E(x)}</li>' for x in p['limitations'])
        flag_lim = f'''
							<div class="project-note">
								<h4 class="project-note__title">Limitations, stated plainly</h4>
								<ul class="flag-lim">{lim}</ul>
							</div>'''
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
							<ul class="project-metrics">{metrics}</ul>{flag_top}

							<div class="row mb--3 project-row">
								<div class="col-6">
									<img class="project-figure" src="../img/{p["img"]}-lg.jpg" alt="Illustrative map for {E(p["title"])}">
									<span class="project-figure__caption">{"Real run output: wrapped input and predicted cycle map" if p["slug"] == "pyunwrap" else "Illustrative graphic"}</span>
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
							</ol>{flag_mid}

							<div class="row mb--3 project-row">
								<div class="col-6">
									<h3>Results</h3>
									<p>{E(p["results"])}</p>
								</div>
								<div class="col-6">
									<h3>Validation</h3>
									<p>{E(p["validation"])}</p>
								</div>
							</div>{notes_html}{flag_lim}

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
for i, p in enumerate(ALL):
    (out_dir / f'{p["slug"]}.html').write_text(page_html(i, p))
print(f'wrote index.html + {len(ALL)} project pages')

# ---------------------------------------------------------------- expertise pages
PBY = {p['slug']: p for p in ALL}
CHECK = ('<svg class="xp-check" width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><circle cx="9" cy="9" r="9" fill="#43B1E7"/>'
         '<path d="M5 9.2l2.6 2.6L13 6.4" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def shell(title, desc, img, kicker, h1, sub, crumbs, body, sidebar):
    crumb_html = ''.join(f'<li class="breadcrumbs__item"><a href="{u}" class="breadcrumbs__link">{E(t)}</a></li>' for t, u in crumbs[:-1])
    crumb_html += f'<li class="breadcrumbs__item current">{E(crumbs[-1][0])}</li>'
    return f'''<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>{E(title)} — Samuel Appiah Kubi</title>
	<meta name="description" content="{E(desc)}">
	<meta name="author" content="Samuel Appiah Kubi">
	<meta property="og:title" content="{E(title)} — Samuel Appiah Kubi">
	<meta property="og:description" content="{E(desc)}">
	<meta property="og:image" content="../img/{img}.jpg">
	<meta name="theme-color" content="#051c2c">
	{favicon}
	{head_fonts}<link media="all" rel="stylesheet" href="../css/main.css">
	<link media="all" rel="stylesheet" href="../css/portfolio.css">
</head>

<body class="page-project page-expertise">
	<div class="wrapper wrapper--offset-0">
		{header}
		<main class="main">
			<section class="section-intro project-intro text--white">
				<div class="container">
					<div class="listing-meta"><span class="listing-meta__item">{E(kicker)}</span></div>
					<h1>{E(h1)}</h1>
					<h6 class="headtitle">{E(sub)}</h6>
				</div>
				<div class="bg-stretch"><img src="../img/{img}.jpg" alt=""></div>
			</section>
			<section class="section-breadcrumbs">
				<div class="container"><ul class="breadcrumbs">{crumb_html}</ul></div>
			</section>
			<section class="section geo--topo project-body">
				<div class="container">
					<div class="main-wrapper">
						<div class="main-content">{body}
						</div>
						<aside class="sidebar">{sidebar}
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

def sidebar_html(active):
    items = [('index', 'How I work')] + [(a['slug'], a['title']) for a in AREAS]
    nav = ''.join(f'<li class="{"is-active" if s == active else ""}"><a href="{s}.html">{E(t)}</a></li>' for s, t in items)
    return f'''
							<div class="widget xp-nav">
								<h4 class="widget__title">What I do</h4>
								<ul class="list list--border xp-nav__list">{nav}</ul>
							</div>
							<div class="widget project-cta bg--gradient text--white">
								<h3 class="project-cta__title">Have a problem like this?</h3>
								<p>Tell me the decision you need to make and the area you care about. I will reply within 24 hours.</p>
								<a href="../index.html#contact" class="btn btn--white">Start a Conversation {ARROW}</a>
							</div>
							<div class="widget xp-cv">
								<h4 class="widget__title">Full background</h4>
								<p>Experience, education, publications and certifications.</p>
								<a href="../assets/Samuel-Appiah-Kubi-CV.pdf" target="_blank" rel="noopener" class="btn btn--outline-primary">Download CV {ARROW}</a>
							</div>'''

def steps_html(steps):
    return ''.join(f'''
								<li class="project-step">
									<span class="project-step__num">{k:02d}</span>
									<div class="project-step__body">
										<h4 class="project-step__title">{E(t)}</h4>
										<p>{E(d)}</p>
									</div>
								</li>''' for k, (t, d) in enumerate(steps, 1))

def mini_cards(slugs):
    out = []
    for s in slugs:
        p = PBY[s]
        out.append(f'''
								<article class="project-card">
									<div class="blog-post">
										<div class="blog-post__visual"><a href="../projects/{s}.html" class="blog-post__img sm" tabindex="-1" aria-hidden="true"><img src="../img/{p["img"]}.jpg" alt="" loading="lazy"></a></div>
										<div class="blog-post__content">
											<div class="listing-meta"><span class="listing-meta__item text--primary">{E(p["tags"][0])}</span><span class="listing-meta__item text--primary">{E(p["tags"][1])}</span></div>
											<h4 class="blog-post__title"><a href="../projects/{s}.html" class="project-card__link">{E(p["title"])}</a></h4>
											<div class="blog-post__description"><p>{E(p["card"])}</p></div>
											<span class="btn btn--link project-card__more">View case study</span>
										</div>
									</div>
								</article>''')
    return ''.join(out)

def area_html(i, a):
    prev_a = AREAS[i - 1]; next_a = AREAS[(i + 1) % len(AREAS)]
    deliver = ''.join(f'<li>{CHECK}<span>{E(d)}</span></li>' for d in a['deliver'])
    audience = ''.join(f'<li class="xp-aud"><h4 class="xp-aud__title">{E(t)}</h4><p>{E(d)}</p></li>' for t, d in a['audience'])
    metrics = ''.join(f'<li class="project-metric"><strong class="project-metric__value">{E(v)}</strong><span class="project-metric__label">{E(l)}</span></li>' for v, l in a['evidence'])
    diff = ''.join(f'<li class="xp-diff"><span class="xp-diff__num">{k}</span><h4 class="xp-diff__title">{E(t)}</h4><p>{E(d)}</p></li>' for k, (t, d) in enumerate(a['different'], 1))
    tools = ''.join(f'<li><span class="tag-list__link">{E(t)}</span></li>' for t in a['tools'])
    faq = ''.join(f'''
								<div class="accordion__item bg--white">
									<h4 class="accordion__title">{E(q)}</h4>
									<div class="accordion__expanded"><p>{E(ans)}</p></div>
								</div>''' for q, ans in a['faq'])
    body = f'''
							<h4 class="headtitle">Overview</h4>
							<p class="project-aim">{E(a["lead"])}</p>

							<div class="row mb--3 project-row">
								<div class="col-6">
									<h3>What you get</h3>
									<ul class="xp-deliver">{deliver}</ul>
								</div>
								<div class="col-6">
									<h3>Who this helps</h3>
									<ul class="xp-audience">{audience}</ul>
								</div>
							</div>

							<h4 class="headtitle">How I approach it</h4>
							<ol class="project-steps">{steps_html(a["approach"])}
							</ol>

							<h4 class="headtitle">Evidence from my work</h4>
							<ul class="project-metrics">{metrics}</ul>
							<p class="xp-note">{E(a["evidence_note"])}</p>

							<h4 class="headtitle">Selected work</h4>
							<div class="xp-projects">{mini_cards(a["projects"])}
							</div>

							<h4 class="headtitle">What sets my work apart</h4>
							<ul class="xp-diffs">{diff}</ul>

							<div class="row mb--3 project-row">
								<div class="col-12 xp-tools">
									<h3>Tools &amp; standards</h3>
									<ul class="tag-list project-tags">{tools}</ul>
								</div>
							</div>

							<h4 class="headtitle">Common questions</h4>
							<div class="accordion xp-faq">{faq}
							</div>

							<hr class="divider">
							<ul class="post-pagination">
								<li class="post-pagination__item prev"><a href="{prev_a["slug"]}.html" class="post-pagination__link" data-title="{E(prev_a["title"])}">{PREV} Previous discipline</a></li>
								<li class="post-pagination__item next"><a href="{next_a["slug"]}.html" class="post-pagination__link" data-title="{E(next_a["title"])}">{NEXT} Next discipline</a></li>
							</ul>'''
    return shell(a['title'], a['tagline'], a['img'], 'What I do', a['title'], a['tagline'],
                 [('Home', '../index.html'), ('What I do', 'index.html'), (a['title'], '')], body, sidebar_html(a['slug']))

def hub_html():
    h = HUB
    cards = ''.join(f'''
								<li class="xp-area">
									<a href="{a["slug"]}.html" class="xp-area__link">
										<span class="xp-area__icon">{ICONS[a["icon"]]}</span>
										<h4 class="xp-area__title">{E(a["title"])}</h4>
										<p>{E(a["tagline"])}</p>
										<span class="btn btn--link">Explore</span>
									</a>
								</li>''' for a in AREAS)
    principles = ''.join(f'<li class="xp-diff"><span class="xp-diff__num">{k}</span><h4 class="xp-diff__title">{E(t)}</h4><p>{E(d)}</p></li>' for k, (t, d) in enumerate(h['principles'], 1))
    engage = ''.join(f'<li class="xp-aud"><h4 class="xp-aud__title">{E(t)}</h4><p>{E(d)}</p></li>' for t, d in h['engage'])
    body = f'''
							<h4 class="headtitle">What I do</h4>
							<p class="project-aim">{E(h["lead"])}</p>
							<p class="xp-why">{E(h["why"])}</p>

							<h4 class="headtitle">How I approach any problem</h4>
							<ol class="project-steps">{steps_html(h["process"])}
							</ol>

							<h4 class="headtitle">Six disciplines</h4>
							<ul class="xp-areas">{cards}
							</ul>

							<h4 class="headtitle">Principles I work by</h4>
							<ul class="xp-diffs xp-diffs--wide">{principles}</ul>

							<div class="row mb--3 project-row">
								<div class="col-12">
									<h3>Ways to work together</h3>
									<ul class="xp-audience xp-audience--grid">{engage}</ul>
								</div>
							</div>'''
    return shell(h['title'], h['tagline'], h['img'], 'How I work', h['title'], h['tagline'],
                 [('Home', '../index.html'), ('What I do', '')], body, sidebar_html('index'))

xdir = ROOT / 'expertise'
xdir.mkdir(exist_ok=True)
for f in xdir.glob('*.html'):
    f.unlink()
(xdir / 'index.html').write_text(hub_html())
for i, a in enumerate(AREAS):
    (xdir / f'{a["slug"]}.html').write_text(area_html(i, a))
print(f'wrote {len(AREAS) + 1} expertise pages')
