#!/usr/bin/env python3
"""
Build static HTML guide pages from content/guides/*.md.
Run from the web root (triedandmade/):
    python tools/build_guides.py

Idempotent: safe to re-run after any new guide is published.
Requires: pip install markdown
"""
import html
import os
import re
from datetime import date

try:
    import markdown as md_lib
except ImportError:
    raise SystemExit("Run:  pip install markdown")

BASE_URL   = "https://triedandmade.com"
GUIDES_SRC = "content/guides"
GUIDES_OUT = "guides"
SITEMAP    = "sitemap.xml"
ROBOTS     = "robots.txt"

# ── static HTML blocks (copied verbatim from guides/post/index.html + forum post) ──

INLINE_CSS = """\
.post-wrap{max-width:780px;margin:0 auto;padding:50px 2rem 80px}
.post-back{display:inline-flex;align-items:center;gap:6px;font-size:13px;color:var(--text-muted);margin-bottom:2rem;transition:color 0.2s}
.post-back:hover{color:var(--amber)}
.post-back::before{content:'←'}
.post-tag{font-size:11px;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:var(--amber);margin-bottom:12px}
.post-title{font-family:'Barlow Condensed',sans-serif;font-size:clamp(32px,5vw,52px);font-weight:800;line-height:1.1;margin-bottom:16px}
.post-meta{font-size:13px;color:var(--text-dim);margin-bottom:2rem;display:flex;gap:1.5rem}
.post-desc{font-size:17px;color:var(--text-muted);line-height:1.7;margin-bottom:2rem;padding-bottom:2rem;border-bottom:1px solid var(--border)}
.post-body{font-size:16px;line-height:1.8;color:var(--text)}
.post-body h1,.post-body h2,.post-body h3{font-family:'Barlow Condensed',sans-serif;font-weight:700;margin:2rem 0 0.75rem;color:var(--text)}
.post-body h1{font-size:32px}
.post-body h2{font-size:26px}
.post-body h3{font-size:20px}
.post-body p{margin-bottom:1.25rem}
.post-body ul,.post-body ol{margin:0 0 1.25rem 1.5rem}
.post-body li{margin-bottom:6px}
.post-body code{background:var(--surface2);padding:2px 6px;border-radius:4px;font-size:13px;font-family:monospace;color:var(--amber-light)}
.post-body pre{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:1.25rem;margin-bottom:1.25rem;overflow-x:auto}
.post-body pre code{background:none;padding:0;color:var(--text)}
.post-body blockquote{border-left:3px solid var(--amber);padding-left:1.25rem;margin-bottom:1.25rem;color:var(--text-muted);font-style:italic}
.post-body img{max-width:100%;border-radius:8px;margin:1rem 0;border:1px solid var(--border)}
.post-body a{color:var(--amber);text-decoration:underline;text-decoration-color:var(--amber-dim)}
.post-body hr{border:none;border-top:1px solid var(--border);margin:2rem 0}
.post-body strong{color:var(--text);font-weight:600}
.post-nav{display:flex;justify-content:flex-start;margin-top:3rem;padding-top:2rem;border-top:1px solid var(--border)}
.affiliate-notice{display:flex;align-items:flex-start;gap:10px;background:rgba(232,146,10,0.08);border:1px solid var(--amber-dim);border-radius:6px;padding:12px 16px;margin-bottom:2rem;font-size:13px;color:var(--text-muted);line-height:1.6}
.affiliate-notice span{font-size:16px;flex-shrink:0;margin-top:2px}
.affiliate-notice p{margin:0}
.affiliate-notice a{color:var(--amber)}
.more-guides{background:var(--surface);border-top:1px solid var(--border);padding:50px 2rem}
.more-guides-inner{max-width:780px;margin:0 auto}
.more-guides-inner h3{font-family:'Barlow Condensed',sans-serif;font-size:24px;font-weight:700;margin-bottom:1.25rem}
.more-guides-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1rem}
.more-guide-card{background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:1.25rem;transition:border-color 0.2s;display:block;text-decoration:none}
.more-guide-card:hover{border-color:var(--amber-dim)}
.more-guide-card .mg-tag{font-size:11px;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:var(--amber);margin-bottom:6px}
.more-guide-card h4{font-size:14px;font-weight:600;line-height:1.4;margin-bottom:6px;color:var(--text)}
.more-guide-card p{font-size:12px;color:var(--text-muted);line-height:1.5;margin:0}"""

NAV = """\
<nav>
  <a href="/" class="logo">Tried<span>&amp;</span>Made</a>
  <ul class="nav-links">
    <li><a href="/guides/" style="color:var(--amber)">Guides</a></li>
    <li><a href="/shop/">Shop Files</a></li>
    <li><a href="/about/">About</a></li>
    <li><a href="mailto:info@triedandmade.com">Contact</a></li>
  </ul>
  <a href="/guides/" class="nav-cta">Find a Fix</a>
  <button class="hamburger" id="hamburger" aria-label="Menu">&#9776;</button>
</nav>
<div class="nav-mobile" id="nav-mobile">
  <ul>
    <li><a href="/guides/">Guides</a></li>
    <li><a href="/shop/">Shop Files</a></li>
    <li><a href="/about/">About</a></li>
    <li><a href="mailto:info@triedandmade.com">Contact</a></li>
  </ul>
</div>
<script>(function(){document.getElementById('hamburger').addEventListener('click',function(){document.getElementById('nav-mobile').classList.toggle('open');});})();</script>"""

AFFILIATE = (
    '<div class="affiliate-notice"><span>&#9888;&#65039;</span>'
    '<p>This guide may contain affiliate links. If you purchase through these links '
    'I may earn a small commission at no extra cost to you. I only recommend products '
    'I have personally used. <a href="/terms/">Learn more</a></p></div>'
)

FOOTER = """\
<footer>
  <div class="footer-inner">
    <div class="footer-brand"><a href="/" class="logo">Tried<span>&amp;</span>Made</a><p>Real fixes for real makers. No fluff, no circles.</p></div>
    <div class="footer-col"><h4>Categories</h4><ul><li><a href="/guides/?cat=Laser Engraving">Laser Engraving</a></li><li><a href="/guides/?cat=3D Printing">3D Printing</a></li><li><a href="/guides/?cat=CNC Routing">CNC Routing</a></li><li><a href="/guides/?cat=Machining">Machining</a></li><li><a href="/guides/?cat=HVAC">HVAC</a></li></ul></div>
    <div class="footer-col"><h4>Site</h4><ul><li><a href="/">Home</a></li><li><a href="/shop/">Shop</a></li><li><a href="/about/">About</a></li></ul></div>
    <div class="footer-col"><h4>Contact</h4><ul><li><a href="mailto:info@triedandmade.com">info@triedandmade.com</a></li></ul></div>
  </div>
  <div class="footer-bottom"><p>&#169; 2026 TriedAndMade.com</p><span class="footer-email">info@triedandmade.com</span></div>
</footer>"""

GDPR = """\
<div id="gdpr-banner" style="display:none;position:fixed;bottom:0;left:0;right:0;z-index:9999;background:#1c1c1a;border-top:1px solid #2e2e2b;padding:16px 24px;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
  <p style="margin:0;font-size:13px;color:#8a8880;max-width:700px;line-height:1.6;">
    This site uses Cloudflare analytics (cookie-free) and may use essential cookies for security. By continuing to use this site you accept our
    <a href="/privacy/" style="color:#E8920A;">Privacy Policy</a>.
    <strong style="color:#e8e6df;">No advertising or tracking cookies are used.</strong>
  </p>
  <div style="display:flex;gap:10px;flex-shrink:0;">
    <button onclick="acceptGDPR()" style="background:#E8920A;color:#1a0e00;border:none;padding:8px 20px;border-radius:6px;font-size:13px;font-weight:600;cursor:pointer;">Accept</button>
    <button onclick="declineGDPR()" style="background:transparent;color:#8a8880;border:1px solid #2e2e2b;padding:8px 20px;border-radius:6px;font-size:13px;cursor:pointer;">Decline</button>
  </div>
</div>
<script>
function acceptGDPR(){localStorage.setItem('gdpr','accepted');document.getElementById('gdpr-banner').style.display='none';}
function declineGDPR(){localStorage.setItem('gdpr','declined');document.getElementById('gdpr-banner').style.display='none';}
(function(){if(!localStorage.getItem('gdpr')){var b=document.getElementById('gdpr-banner');b.style.display='flex';}})();
</script>"""


# ── helpers ──────────────────────────────────────────────────────────────────

def parse_frontmatter(text):
    m = re.match(r'^---\n([\s\S]*?)\n---\n?', text)
    if not m:
        return {}, text
    data = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            k, _, v = line.partition(':')
            k = k.strip()
            v = v.strip().strip('"\'')
            if k:
                data[k] = v
    return data, text[m.end():]


def load_guides():
    guides = []
    for fname in os.listdir(GUIDES_SRC):
        if not fname.endswith('.md'):
            continue
        slug = fname[:-3]
        with open(os.path.join(GUIDES_SRC, fname), encoding='utf-8') as f:
            raw = f.read()
        data, content = parse_frontmatter(raw)
        guides.append({'slug': slug, 'data': data, 'content': content})
    guides.sort(key=lambda g: g['data'].get('date', ''), reverse=True)
    return guides


def format_date(s):
    if not s:
        return ''
    try:
        y, mo, d = s.split('-')
        dt = date(int(y), int(mo), int(d))
        return dt.strftime('%B') + ' ' + str(dt.day) + ', ' + str(dt.year)
    except Exception:
        return s


def get_related(current, all_guides, max_count=4):
    cat = current['data'].get('category', '')
    same = [g for g in all_guides
            if g['slug'] != current['slug'] and g['data'].get('category') == cat]
    if len(same) >= 2:
        return same[:max_count]
    return [g for g in all_guides if g['slug'] != current['slug']][:max_count]


def render_more_guides(guides):
    if not guides:
        return ''
    cards = '\n'.join(
        '      <a href="/guides/{slug}/" class="more-guide-card">\n'
        '        <div class="mg-tag">{cat}</div>\n'
        '        <h4>{title}</h4>\n'
        '        <p>{desc}</p>\n'
        '      </a>'.format(
            slug=g['slug'],
            cat=html.escape(g['data'].get('category', 'Guide')),
            title=html.escape(g['data'].get('title', g['slug'])),
            desc=html.escape(g['data'].get('description', '')[:100]),
        )
        for g in guides
    )
    return (
        '\n<section class="more-guides">\n'
        '  <div class="more-guides-inner">\n'
        '    <h3>More Guides</h3>\n'
        '    <div class="more-guides-grid">\n'
        + cards + '\n'
        + '    </div>\n'
        '    <a href="/guides/" class="btn-secondary"'
        ' style="display:inline-block;margin-top:1.5rem">Browse all guides &#8594;</a>\n'
        '  </div>\n'
        '</section>'
    )


# ── page builder ─────────────────────────────────────────────────────────────

def build_page(guide, all_guides):
    data      = guide['data']
    slug      = guide['slug']
    title     = data.get('title', slug)
    desc      = data.get('description', '')
    category  = data.get('category', 'Guide')
    date_str  = data.get('date', '')
    tags_str  = data.get('tags', '')

    esc_title = html.escape(title, quote=True)
    esc_desc  = html.escape(desc,  quote=True)
    canonical = BASE_URL + '/guides/' + slug + '/'
    disp_date = format_date(date_str)

    body_html = md_lib.markdown(guide['content'], extensions=['extra'])

    related      = get_related(guide, all_guides)
    more_section = render_more_guides(related)

    meta_row = (
        '  <div class="post-meta">'
        '<span>' + html.escape(disp_date) + '</span>'
        + ('<span>' + html.escape(tags_str) + '</span>' if tags_str else '')
        + '</div>\n'
    )
    desc_para = (
        '  <p class="post-desc">' + html.escape(desc) + '</p>\n'
        if desc else ''
    )

    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>' + html.escape(title) + ' | TriedAndMade</title>\n'
        '<meta name="description" content="' + esc_desc + '">\n'
        '<link rel="canonical" href="' + canonical + '">\n'
        '<meta property="og:title" content="' + esc_title + '">\n'
        '<meta property="og:description" content="' + esc_desc + '">\n'
        '<meta property="og:type" content="article">\n'
        '<meta property="og:url" content="' + canonical + '">\n'
        '<link rel="stylesheet" href="/css/style.css">\n'
        '<style>\n' + INLINE_CSS + '\n</style>\n'
        '</head>\n<body>\n'
        + NAV + '\n\n'
        + '<div class="post-wrap">\n'
        '  <a href="/guides/" class="post-back">Back to all guides</a>\n'
        '  <div class="post-tag">' + html.escape(category) + '</div>\n'
        '  <h1 class="post-title">' + html.escape(title) + '</h1>\n'
        + meta_row
        + desc_para
        + '  ' + AFFILIATE + '\n'
        + '  <div class="post-body">' + body_html + '</div>\n'
        + '  <div class="post-nav">'
          '<a href="/guides/" class="btn-secondary">&#8592; Back to all guides</a>'
          '</div>\n'
        + '</div>\n'
        + more_section + '\n\n'
        + FOOTER + '\n\n'
        + GDPR + '\n'
        + '</body>\n</html>\n'
    )


# ── sitemap ───────────────────────────────────────────────────────────────────

def build_sitemap(guides):
    today = date.today().isoformat()
    pages = [
        (BASE_URL + '/',                                              today),
        (BASE_URL + '/guides/',                                       today),
        (BASE_URL + '/shop/',                                         today),
        (BASE_URL + '/about/',                                        today),
        (BASE_URL + '/forum/3d-print-settings-why-3dprintlogpro/',   '2026-05-28'),
        (BASE_URL + '/disclaimer/',                                   today),
        (BASE_URL + '/terms/',                                        today),
        (BASE_URL + '/privacy/',                                      today),
    ] + [
        (BASE_URL + '/guides/' + g['slug'] + '/', g['data'].get('date', today))
        for g in guides
    ]
    urls = '\n'.join(
        '  <url>\n'
        '    <loc>' + loc + '</loc>\n'
        '    <lastmod>' + lastmod + '</lastmod>\n'
        '  </url>'
        for loc, lastmod in pages
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls + '\n'
        + '</urlset>\n'
    )


def build_robots():
    return (
        'User-agent: *\n'
        'Allow: /\n'
        '\n'
        'Sitemap: https://triedandmade.com/sitemap.xml\n'
    )


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    guides = load_guides()
    print(f"Found {len(guides)} guide(s)")

    for guide in guides:
        slug    = guide['slug']
        out_dir = os.path.join(GUIDES_OUT, slug)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, 'index.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(build_page(guide, guides))
        print(f"  Built: guides/{slug}/index.html")

    with open(SITEMAP, 'w', encoding='utf-8') as f:
        f.write(build_sitemap(guides))
    print(f"  Built: {SITEMAP}")

    with open(ROBOTS, 'w', encoding='utf-8') as f:
        f.write(build_robots())
    print(f"  Built: {ROBOTS}")

    print("Done.")


if __name__ == '__main__':
    main()
