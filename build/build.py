# -*- coding: utf-8 -*-
"""Render the archive pages. Run: python3 build/build.py  (from the repo root)"""
import json, os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shell import page, cta, SITE
from issues import ISSUES, PUB_DATE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def esc(s):
    """Strip tags then escape — for meta/JSON-LD values."""
    import re
    return html.escape(re.sub(r'<[^>]+>', '', s.replace('&mdash;', '—').replace('&ndash;', '–')
                              .replace('&ldquo;','“').replace('&rdquo;','”').replace('&amp;','&')),
                       quote=True)

def timeline_table(rows, finish):
    body = "\n".join(
        f'      <tr><th scope="row">{w}</th><td>{t}</td></tr>' for w, t in rows)
    fw, ft = finish
    return f"""  <div class="tablewrap">
  <table>
    <caption>Backward from Saturday 6:00pm dinner</caption>
    <thead><tr><th scope="col">When</th><th scope="col">What</th></tr></thead>
    <tbody>
{body}
      <tr class="finish"><th scope="row">{fw}</th><td>{ft}</td></tr>
    </tbody>
  </table>
  </div>"""

def issue_page(iss):
    path = f"/archive/{iss['slug']}/"
    answer = "\n    ".join(f"<p>{p}</p>" for p in iss["answer"])
    sources = "\n".join(
        f'    <li><a href="{u}" rel="nofollow">{l}</a></li>' for l, u in iss["sources"])

    body = f"""<div class="wrap narrow">
  <p class="crumb"><a href="/">The Weekend Pit</a> &nbsp;/&nbsp; <a href="/archive/">Archive</a> &nbsp;/&nbsp; Issue No. {iss['num']}</p>

  <header class="page">
    <div class="issueno">Issue No. {iss['num']} &middot; The Deep Smoke</div>
    <h1>{iss['h1']}</h1>
    <p class="standfirst">{iss['standfirst']}</p>
    <p class="byline">Published by <b>The Weekend Pit</b> &middot; Every temperature verified against USDA guidance and cross-checked against at least two credible sources &mdash; all named at the bottom of this page.</p>
  </header>

  <div class="answer">
    <div class="tag">The short answer</div>
    {answer}
  </div>

  <section>
    <div class="sectag">The Deep Smoke</div>
    <h2>{iss['deep_heading']}</h2>
{iss['deep']}
  </section>

  <section>
    <div class="sectag">This Weekend's Cook</div>
    <h2>{iss['cook_heading']}</h2>
    <p>{iss['cook_intro']}</p>
{timeline_table(iss['timeline'], iss['finish'])}
    <h3>You'll need</h3>
    <p>{iss['needs']}</p>
    <h3>The rig</h3>
    <p>{iss['rig']}</p>
    <h3>The numbers</h3>
    <p>{iss['numbers']}</p>
    <p class="tnote">{iss['safety']}</p>
  </section>

  <section>
    <div class="find">
      <div class="tag">Pit Find</div>
      <h3>{iss['find_heading']}</h3>
{iss['find']}
      <p class="disc">No affiliate link on this one &mdash; our affiliate accounts aren't live yet. When they are, every affiliate link on this site will say so.</p>
    </div>
  </section>
</div>

<div class="sources"><div class="wrap narrow">
  <h2>Sources</h2>
  <p class="sub">Every claim above traces to at least one of these, and every temperature to at least two.</p>
  <ul>
{sources}
  </ul>
  <p class="sub" style="margin-top:22px">Every number here also lives on the <a href="/temperatures/">temperature chart</a>, kept in one place and re-verified together.</p>
</div></div>

{cta("Get the next one on Thursday.", "One free email every Thursday at 7am: a technique explained properly, a recipe timed backward from Saturday dinner, and one piece of gear with its flaw named.")}"""

    ld = json.dumps({
      "@context": "https://schema.org",
      "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "The Weekend Pit", "item": f"{SITE}/"},
          {"@type": "ListItem", "position": 2, "name": "Archive", "item": f"{SITE}/archive/"},
          {"@type": "ListItem", "position": 3, "name": f"Issue No. {iss['num']}", "item": f"{SITE}{path}"}]},
        {"@type": "BlogPosting",
         "headline": esc(iss["seo_title"]),
         "alternativeHeadline": esc(iss["h1"]),
         "description": esc(iss["description"]),
         "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE}{path}"},
         "inLanguage": "en-US",
         "datePublished": PUB_DATE, "dateModified": PUB_DATE,
         "image": f"{SITE}/assets/og-image.png",
         "isPartOf": {"@type": "Blog", "name": "The Weekend Pit", "url": f"{SITE}/archive/"},
         "author": {"@type": "Organization", "name": "The Weekend Pit", "url": f"{SITE}/"},
         "publisher": {"@type": "Organization", "name": "The Weekend Pit", "url": f"{SITE}/",
                       "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/logo-stamp.svg"}},
         "citation": [{"@type": "CreativeWork", "name": esc(l), "url": u} for l, u in iss["sources"]]}
      ]}, indent=1, ensure_ascii=False)

    return path, page(path=path, depth=2, title=esc(iss["seo_title"]),
                      description=esc(iss["description"]), og_type="article",
                      body=body, jsonld=ld, current="archive")

def archive_index():
    path = "/archive/"
    items = "\n".join(f"""  <li>
    <div class="n">Issue No. {i['num']}</div>
    <h2><a href="/archive/{i['slug']}/">{i['h1']}</a></h2>
    <p>{esc(i['description'])}</p>
  </li>""" for i in ISSUES)

    body = f"""<div class="wrap narrow">
  <p class="crumb"><a href="/">The Weekend Pit</a> &nbsp;/&nbsp; Archive</p>
  <header class="page">
    <div class="issueno">The Archive</div>
    <h1>Every issue, still useful.</h1>
    <p class="standfirst">One technique explained properly, one recipe timed backward from Saturday dinner, and one piece of gear with its flaw named &mdash; every Thursday at 7am. Here's what's gone out so far.</p>
    <p class="byline">Reader's Pit, the weekly poll and the rest of the email live only in the email. What's kept here is the part that's still true in a year.</p>
  </header>

  <ul class="issues">
{items}
  </ul>

  <section style="padding-top:46px">
    <p>Looking for a number rather than a story? The <a href="/temperatures/">temperature chart</a> collects every safe temp and pull temp in one page, and the <a href="/assets/temperature-sheet.pdf">printable sheet</a> fits inside a cabinet door.</p>
  </section>
</div>

{cta("One email. One weekend. One great cook.", "Free, every Thursday at 7am. Unsubscribe anytime — no hard feelings at the fence line.")}"""

    ld = json.dumps({
      "@context": "https://schema.org",
      "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "The Weekend Pit", "item": f"{SITE}/"},
          {"@type": "ListItem", "position": 2, "name": "Archive", "item": f"{SITE}/archive/"}]},
        {"@type": "CollectionPage",
         "name": "The Weekend Pit — Archive",
         "description": "Every issue of The Weekend Pit: BBQ techniques explained properly, recipes timed backward from Saturday dinner, and gear reviews that name the flaw.",
         "url": f"{SITE}/archive/", "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": "The Weekend Pit", "url": f"{SITE}/"},
         "mainEntity": {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": n + 1, "url": f"{SITE}/archive/{i['slug']}/",
             "name": esc(i["h1"])} for n, i in enumerate(ISSUES)]}}
      ]}, indent=1, ensure_ascii=False)

    return path, page(path=path, depth=2,
                      title="The Weekend Pit — Archive",
                      description="Every issue of The Weekend Pit: the stall explained, the 3-2-1 rib method audited, and why smoked chicken skin goes rubbery. Techniques explained properly, with the sources named.",
                      og_type="website", body=body, jsonld=ld, current="archive")

def write(path, content):
    out = os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  {path:<32} {len(content):>7,} bytes")

if __name__ == "__main__":
    print("Building archive pages:")
    urls = []
    p, c = archive_index(); write(p, c); urls.append(p)
    for iss in ISSUES:
        p, c = issue_page(iss); write(p, c); urls.append(p)

    # sitemap
    entries = [("/", "weekly", "1.0"), ("/temperatures/", "monthly", "0.9"),
               ("/archive/", "weekly", "0.8")] + [(u, "yearly", "0.7") for u in urls if u != "/archive/"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, freq, pri in entries:
        sm += ["  <url>", f"    <loc>{SITE}{loc}</loc>", f"    <lastmod>{PUB_DATE}</lastmod>",
               f"    <changefreq>{freq}</changefreq>", f"    <priority>{pri}</priority>", "  </url>"]
    sm.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm) + "\n")
    print(f"  {'/sitemap.xml':<32} {len(entries)} urls")
