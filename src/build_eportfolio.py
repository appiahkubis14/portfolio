"""Builds eportfolio/index.html on its own, without touching any other page.

It takes the header, footer and fonts from the current index.html, so manual edits
to the home page are respected. Edit src/eportfolio.py, then run:
    python3 src/build_eportfolio.py
(Do not run src/build.py unless src/index.src.html has your latest home-page edits:
it regenerates index.html and every project page from the source files.)
"""
from pathlib import Path
import html, re, sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'src'))
from projects import PROJECTS  # noqa: E402
_ns = {'PHYSINSAR': None}
exec((ROOT / 'src' / 'flagships.py').read_text().replace('FLAGSHIPS = [', '_FL = ['), _ns)
from eportfolio import EPORTFOLIO, COURSES, SEMESTER  # noqa: E402
ALL = [p for p in [_ns.get('PYUNWRAP'), _ns.get('PSGNN')] if p] + PROJECTS
PBY = {p['slug']: p for p in ALL}
E = html.escape

ARROW = ('<svg class="icon" width="21" height="12" viewBox="0 0 21 12">'
         '<path fill-rule="evenodd" clip-rule="evenodd" d="M15 6.75L0 6.75L0 5.25L15 5.25V6.75Z"/>'
         '<path d="M21 5.99986L14.25 11.196L14.25 0.803711L21 5.99986Z"/></svg>')

home = (ROOT / 'index.html').read_text()

def rel(chunk):
    chunk = re.sub(r'href="#', 'href="../index.html#', chunk)
    chunk = re.sub(r'(src|href)="(img|assets|css|js|projects|expertise|eportfolio)/', r'\1="../\2/', chunk)
    return chunk

header = rel(home[home.find('<header'):home.find('</header>') + 9])
footer = rel(home[home.find('<footer'):home.find('</footer>') + 9])
head_fonts = home[home.find('<link rel="preconnect"'):home.find('<link media="all" rel="stylesheet" href="css/main.css">')]
favicon = re.search(r'<link rel="icon"[^>]*>', home).group(0)

PREV = ('<svg class="icon" width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M15 7.5C15 3.36 11.64 0 7.5 0S0 3.36 0 7.5 3.36 15 7.5 15 15 11.64 15 7.5Z" fill="#43B1E7"/>'
        '<path fill-rule="evenodd" clip-rule="evenodd" d="M8.18 4.14L5.14 7.16a.48.48 0 0 0 0 .68l3.04 3.02a.48.48 0 0 0 .68-.67L6.04 7.5l2.82-2.69a.48.48 0 0 0-.68-.67Z" fill="white"/></svg>')
NEXT = ('<svg class="icon" width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M0 7.5C0 3.36 3.36 0 7.5 0S15 3.36 15 7.5 11.64 15 7.5 15 0 11.64 0 7.5Z" fill="#43B1E7"/>'
        '<path fill-rule="evenodd" clip-rule="evenodd" d="M6.82 4.14l3.04 3.02a.48.48 0 0 1 0 .68l-3.04 3.02a.48.48 0 0 1-.68-.67L8.96 7.5 6.14 4.81a.48.48 0 0 1 .68-.67Z" fill="white"/></svg>')

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

# ---------------------------------------------------------------- ePortfolio page
def eportfolio_sidebar():
    return f"""
							<div class="widget xp-nav">
								<h4 class="widget__title">On this page</h4>
								<ul class="list list--border xp-nav__list">
									<li><a href="#programme">The programme</a></li>
									<li><a href="#trajectory">My path so far</a></li>
									<li><a href="#coursework">Coursework</a></li>
									<li><a href="#journey">Learning journey</a></li>
									<li><a href="#next">Next steps</a></li>
								</ul>
							</div>
							<div class="widget xp-cv">
								<h4 class="widget__title">The programme</h4>
								<p>Copernicus Master in Digital Earth, an Erasmus Mundus joint Master's degree.</p>
								<a href="https://www.plus.ac.at/geoinformatik/education/cde/?lang=en" target="_blank" rel="noopener" class="btn btn--outline-primary">Programme website {ARROW}</a>
							</div>
							<div class="widget xp-cv">
								<h4 class="widget__title">Full background</h4>
								<p>Experience, education, publications and certifications.</p>
								<a href="../assets/Samuel-Appiah-Kubi-CV.pdf" target="_blank" rel="noopener" class="btn btn--outline-primary">Download CV {ARROW}</a>
							</div>
							<div class="widget project-cta bg--gradient text--white">
								<h3 class="project-cta__title">Get in touch</h3>
								<p>Questions about my studies, research or a collaboration are welcome.</p>
								<a href="../index.html#contact" class="btn btn--white">Contact me {ARROW}</a>
							</div>"""

def course_html(c):
    meta = ' · '.join(x for x in (c.get('code', ''), (c['ects'] + ' ECTS') if c.get('ects') else '') if x)
    lines = f'<p>{E(c["what"])}</p>'
    if c.get('work'):
        link = f' <a href="{E(c["link"])}" target="_blank" rel="noopener">View the work</a>' if c.get('link') else ''
        lines += f'<p><strong>My work:</strong> {E(c["work"])}{link}</p>'
    if c.get('learned'):
        lines += f'<p><strong>What I learned:</strong> {E(c["learned"])}</p>'
    status = '' if (c.get('work') or c.get('learned')) else '<span class="ep-status">In progress</span>'
    return f"""
								<li class="xp-aud ep-course">
									<span class="tl-meta text--primary">{E(meta)}</span>{status}
									<h4 class="xp-aud__title">{E(c["title"])}</h4>
									{lines}
								</li>"""

def courses_html():
    if not COURSES:
        return '<div class="ep-empty"><p class="xp-note">Course entries are added here as each module finishes.</p></div>'
    total = sum(int(c['ects']) for c in COURSES if c.get('ects', '').isdigit())
    out = [f'<div class="ep-empty"><p class="xp-note">{E(SEMESTER)} · {len(COURSES)} courses · {total} ECTS. Reflections and links to my work are added as each course finishes.</p></div>']
    groups = []
    for c in COURSES:
        if c['group'] not in groups:
            groups.append(c['group'])
    for g in groups:
        items = ''.join(course_html(c) for c in COURSES if c['group'] == g)
        out.append(f'<h3 class="ep-group">{E(g)}</h3><ul class="xp-audience xp-audience--grid ep-courses">{items}</ul>')
    return ''.join(out)

def eportfolio_html():
    e = EPORTFOLIO
    prog = ''.join(f'<li class="xp-aud"><h4 class="xp-aud__title">{E(t)}</h4><p>{E(d)}</p></li>' for t, d in e['programme'])
    courses = courses_html()
    journey = ''.join(f'<p>{E(p)}</p>' for p in e['journey'])
    nxt = ''.join(f'<li class="xp-diff"><span class="xp-diff__num">{k}</span><h4 class="xp-diff__title">{E(t)}</h4><p>{E(d)}</p></li>' for k, (t, d) in enumerate(e['next'], 1))
    skills = ''.join(f'<li><span class="tag-list__link">{E(t)}</span></li>' for t in e['skills'])
    body = f"""
							<h4 class="headtitle">About this ePortfolio</h4>
							<p class="project-aim">{E(e["intro"])}</p>

							<div class="row mb--3 project-row" id="programme">
								<div class="col-12">
									<h3>The programme</h3>
									<ul class="xp-audience xp-audience--grid">{prog}</ul>
								</div>
							</div>

							<h4 class="headtitle" id="trajectory">My path so far</h4>
							<ol class="project-steps">{steps_html(e["trajectory"])}
							</ol>

							<h4 class="headtitle">Selected work</h4>
							<div class="xp-projects">{mini_cards(e["evidence"])}
							</div>

							<h4 class="headtitle" id="coursework">Coursework</h4>
							{courses}
							<div class="ep-gap"></div>

							<h4 class="headtitle" id="journey">Learning journey</h4>
							<div class="ep-journey">{journey}</div>
							<div class="ep-gap"></div>

							<h4 class="headtitle" id="next">Next steps</h4>
							<ul class="xp-diffs xp-diffs--wide">{nxt}</ul>

							<div class="row mb--3 project-row">
								<div class="col-12 xp-tools">
									<h3>Skills I am building</h3>
									<ul class="tag-list project-tags">{skills}</ul>
								</div>
							</div>"""
    return shell(e['title'], e['tagline'], e['img'], 'Copernicus Master in Digital Earth', 'ePortfolio', e['tagline'],
                 [('Home', '../index.html'), ('ePortfolio', '')], body, eportfolio_sidebar())

edir = ROOT / 'eportfolio'
edir.mkdir(exist_ok=True)
(edir / 'index.html').write_text(eportfolio_html())
print('wrote eportfolio/index.html')
