# -*- coding: utf-8 -*-
"""Render the archive pages. Run: python3 build/build.py  (from the repo root)"""
import json, os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shell import page, cta, SITE
from issues import ISSUES, PUB_DATE, CORRECTIONS

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


def about_page():
    path = "/about/"
    body = """<div class="wrap narrow">
  <p class="crumb"><a href="/">The Weekend Pit</a> &nbsp;/&nbsp; About</p>

  <header class="page">
    <div class="issueno">About</div>
    <h1>Every number here had to earn its place.</h1>
    <p class="standfirst">Barbecue advice is mostly confident men repeating each other. This is one email a week that tries to be something else: checked, sourced, and honest about what nobody actually knows.</p>
    <p class="byline">The Weekend Pit is a free email, every Thursday at 7am. It comes from a backyard, not a test kitchen.</p>
  </header>

  <div class="answer">
    <div class="tag">The short answer</div>
    <p>The Weekend Pit is a free weekly email for backyard smokers. Every temperature is checked against <b>USDA</b> guidance, every technique is cross-checked against at least <b>two</b> credible sources, and those sources get named on the page.</p>
    <p>Every gear review names a flaw. Where the experts genuinely disagree, we say so instead of picking a winner and pretending it was obvious.</p>
  </div>
</div>

<div class="wrap narrow">

<section>
  <div class="sectag">The rules</div>
  <h2>Four things that don&rsquo;t bend</h2>
  <ol class="rules">
    <li>
      <h3>Every temperature is checked against the USDA</h3>
      <p>Safety floors come from foodsafety.gov, not from memory and not from another blog. When our pull temperature sits above the safety minimum &mdash; which for brisket and pork butt it always does &mdash; we say which number is which and why. When a common practice sits <em>below</em> the USDA minimum, like tri-tip at 130&ndash;140&deg;F, we print both numbers and tell you plainly that you are choosing to depart from official guidance.</p>
    </li>
    <li>
      <h3>Two credible sources, named</h3>
      <p>No technique goes out on one source. Every claim traces to at least two, and they are listed at the bottom of the page so you can go read them yourself and decide we were wrong. Sources get a date, because a temperature guide from 2011 is not the same document it was.</p>
    </li>
    <li>
      <h3>Every gear review names a flaw</h3>
      <p>If we can&rsquo;t find something wrong with it, we haven&rsquo;t looked hard enough to recommend it. The flaw is the part that makes the praise worth reading. Budget picks get the same treatment as expensive ones &mdash; usually more, because the cheap thing is what most people should actually buy.</p>
    </li>
    <li>
      <h3>No invented testimonials. Ever.</h3>
      <p>There is no fake reader quote on this site, no invented subscriber count, no stock-photo pitmaster with a made-up name. When a real reader says something worth quoting, their name will be on it and they will have said yes. Until then, this space stays empty, which is its own kind of information.</p>
    </li>
  </ol>
</section>

<section>
  <div class="sectag">Where we disagree with everyone else</div>
  <h2>Saying &ldquo;nobody knows&rdquo; out loud</h2>
  <p>The most useful thing a barbecue writer can do is admit where the evidence runs out. Ribs are the clearest case: ThermoWorks says pull at 180&ndash;195&deg;F, AmazingRibs says around 203&deg;F, SmokedBBQSource says 180&ndash;185&deg;F. All three are careful, credible outfits. They disagree because ribs genuinely vary &mdash; by cut, by thickness, by how the pit ran that day.</p>
  <p>The tempting move is to pick one, state it with confidence, and look authoritative. We do the other thing: name the disagreement, explain why it exists, and teach the test that outlives all three numbers. You will find that pattern everywhere here. It is slower to read and it is the reason the advice holds up.</p>
  <p class="fence">&ldquo;If the sources disagree, that&rsquo;s the interesting part &mdash; not the part to hide.&rdquo;</p>
</section>

<section>
  <div class="sectag">Money</div>
  <h2>How this pays for itself, honestly</h2>
  <p>The email is free and always will be. It is reader-supported, which in practice means gear links: if you buy something through one, we earn a small commission at no extra cost to you.</p>
  <div class="flag"><b>Right now, there are none.</b> Our affiliate accounts aren&rsquo;t live yet, so every gear recommendation on this site currently earns us nothing. When that changes, every affiliate link will be labeled as one, inline, every time &mdash; not buried in a footer disclosure you were never going to read.</div>
  <p>If sponsorships happen later, they will be marked as sponsorships and they will not buy a recommendation. A sponsor can pay for space. Nobody can pay to be called good.</p>
</section>

<section>
  <div class="sectag">What lands Thursday</div>
  <h2>One email, four parts, about six minutes</h2>
  <p><b>The Deep Smoke</b> &mdash; one technique explained properly: the physics, the method, and the one mistake everyone makes.</p>
  <p><b>This Weekend&rsquo;s Cook</b> &mdash; one recipe with the timeline built backward from Saturday 6:00pm dinner, so Thursday-you knows what Saturday-you has to do.</p>
  <p><b>Pit Find</b> &mdash; one piece of gear, flaw named. Sometimes it&rsquo;s $12.</p>
  <p><b>Reader&rsquo;s Pit</b> &mdash; one reader&rsquo;s cook, and the one thing they&rsquo;d do differently.</p>
  <p class="sub" style="margin-top:22px">The first three live on this site afterward, in <a href="/archive/">the archive</a>. Reader&rsquo;s Pit stays in the email, where it belongs.</p>
</section>

<section>
  <div class="sectag">Corrections</div>
  <h2>When we get it wrong</h2>
  <p>We will. A page that has never been corrected is either very young or not being checked. If you find a number here that&rsquo;s wrong, reply to any issue and tell us &mdash; the correction goes in the next email <em>and</em> gets fixed on the page it came from, with the date it changed. Silently editing a mistake away is its own small dishonesty.</p>
  <p>Every correction we have made is logged, in public, on the <a href="/corrections/">corrections page</a> &mdash; including the fact that there aren&rsquo;t any yet.</p>
</section>

<section class="faq">
  <h2>Common questions</h2>

  <h3>Is The Weekend Pit free?</h3>
  <p>Yes, and it stays free. One email every Thursday at 7am, unsubscribe any time. There is no paywall and no upsell at the end of an issue.</p>

  <h3>Do you get paid to recommend gear?</h3>
  <p>Not currently &mdash; our affiliate accounts aren&rsquo;t live, so nothing on this site earns a commission today. When they are, every affiliate link will say so inline. No recommendation is ever paid for: a sponsor can buy space, not praise.</p>

  <h3>How do you verify the temperatures?</h3>
  <p>Safety minimums come from the USDA via foodsafety.gov. Cooking targets are cross-checked against at least two credible sources &mdash; typically AmazingRibs, SmokedBBQSource and ThermoWorks &mdash; and every source is named and dated on the page. Where they disagree, we print the disagreement rather than picking one.</p>

  <h3>Who writes it?</h3>
  <p>It comes from a backyard pit and a Thursday morning, not a content team or a test kitchen. That is deliberate: the point of this newsletter is that it answers the questions a person with one smoker and one Saturday actually has.</p>

  <h3>What&rsquo;s the free temperature sheet?</h3>
  <p>A one-page chart of every number that matters at the pit &mdash; USDA safety floors and real pull temps for brisket, butt, ribs and birds &mdash; sized to tape inside a cabinet door. It&rsquo;s free with no signup required. The <a href="/temperatures/">full chart is here</a>, and the <a href="/assets/temperature-sheet.pdf">printable PDF is here</a>.</p>

  <h3>How often does it come out?</h3>
  <p>Once a week, Thursday at 7am. Thursday because it gives you time to shop before the weekend; once a week because that is how often most people cook.</p>
</section>

</div>

""" + cta("Thursday, 7am. Bring coffee.",
          "One free email a week: a technique explained properly, a recipe timed backward from Saturday dinner, and one piece of gear with its flaw named.")

    ld = json.dumps({
      "@context": "https://schema.org",
      "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "The Weekend Pit", "item": f"{SITE}/"},
          {"@type": "ListItem", "position": 2, "name": "About", "item": f"{SITE}/about/"}]},
        {"@type": "AboutPage",
         "name": "About The Weekend Pit",
         "description": "How The Weekend Pit checks every number: USDA safety floors, two named sources per technique, a flaw named in every gear review, and no invented testimonials.",
         "url": f"{SITE}/about/", "inLanguage": "en-US",
         "dateModified": PUB_DATE,
         "isPartOf": {"@type": "WebSite", "name": "The Weekend Pit", "url": f"{SITE}/"},
         "about": {"@type": "Organization", "name": "The Weekend Pit", "url": f"{SITE}/",
                   "description": "A free weekly email for backyard smokers: one technique explained properly, one recipe timed backward from Saturday dinner, and one honest gear review \u2014 every Thursday at 7am.",
                   "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/logo-stamp.svg"},
                   "publishingPrinciples": f"{SITE}/about/"}},
        {"@type": "FAQPage", "mainEntity": [
          {"@type": "Question", "name": "Is The Weekend Pit free?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, and it stays free. One email every Thursday at 7am, unsubscribe any time. There is no paywall and no upsell."}},
          {"@type": "Question", "name": "Do you get paid to recommend gear?", "acceptedAnswer": {"@type": "Answer", "text": "Not currently \u2014 our affiliate accounts aren't live, so nothing on the site earns a commission today. When they are, every affiliate link will say so inline. No recommendation is ever paid for: a sponsor can buy space, not praise."}},
          {"@type": "Question", "name": "How do you verify the temperatures?", "acceptedAnswer": {"@type": "Answer", "text": "Safety minimums come from the USDA via foodsafety.gov. Cooking targets are cross-checked against at least two credible sources \u2014 typically AmazingRibs, SmokedBBQSource and ThermoWorks \u2014 and every source is named and dated on the page. Where they disagree, we print the disagreement rather than picking one."}},
          {"@type": "Question", "name": "Who writes The Weekend Pit?", "acceptedAnswer": {"@type": "Answer", "text": "It comes from a backyard pit and a Thursday morning, not a content team or a test kitchen \u2014 so it answers the questions a person with one smoker and one Saturday actually has."}},
          {"@type": "Question", "name": "How often does The Weekend Pit come out?", "acceptedAnswer": {"@type": "Answer", "text": "Once a week, Thursday at 7am. Thursday gives you time to shop before the weekend."}}]}
      ]}, indent=1, ensure_ascii=False)

    return path, page(path=path, depth=2,
                      title="About The Weekend Pit \u2014 how every number gets checked",
                      description="A free weekly email for backyard smokers. Every temperature checked against USDA guidance, every technique cross-checked against two named sources, a flaw named in every gear review, and no invented testimonials.",
                      og_type="website", body=body, jsonld=ld)


def corrections_page():
    path = "/corrections/"

    if CORRECTIONS:
        rows = "\n".join(f"""    <li>
      <div class="n">{c['date']} &middot; {c['where']}</div>
      <h2>{c['what']}</h2>
      <p><b>Now reads:</b> {c['now']}</p>
      <p class="sub">Found via {c['how']}.{(' <a href="' + c['url'] + '">See the page</a>.') if c.get('url') else ''}</p>
    </li>""" for c in CORRECTIONS)
        log = f'  <ul class="issues">\n{rows}\n  </ul>'
        count = f"{len(CORRECTIONS)} correction{'s' if len(CORRECTIONS) != 1 else ''} so far."
    else:
        log = """  <div class="flag"><b>Nothing yet.</b> No correction has been needed since the first issue was written. That is not a boast &mdash; it mostly means this newsletter is very young. The page exists so that when something does need fixing there is an obvious place for it, and so you can check whether we actually do what we say.</div>"""
        count = "No corrections yet."

    body = f"""<div class="wrap narrow">
  <p class="crumb"><a href="/">The Weekend Pit</a> &nbsp;/&nbsp; Corrections</p>

  <header class="page">
    <div class="issueno">Corrections</div>
    <h1>A page that has never been corrected is either very young or not being checked.</h1>
    <p class="standfirst">This one is very young. Here is every substantive correction we have made, what was wrong, and how we found out &mdash; newest first, so you can judge the habit rather than the promise.</p>
    <p class="byline">{count} Found something wrong? Reply to any issue and tell us.</p>
  </header>

  <div class="answer">
    <div class="tag">The short answer</div>
    <p>If we print something wrong, the correction goes <b>in the next email</b> and <b>on the page it came from</b>, dated, and it gets logged here.</p>
    <p>We don't quietly edit mistakes away. A number that changed without a note is indistinguishable from a number that was never wrong, and that difference is the whole point of this newsletter.</p>
  </div>
</div>

<div class="wrap narrow">

<section>
  <div class="sectag">The log</div>
  <h2>What we have gotten wrong</h2>
{log}
</section>

<section>
  <div class="sectag">The policy</div>
  <h2>What counts, and what happens</h2>
  <p><b>What gets logged here:</b> a temperature, a time, a price, a source, an attribution, or any claim a reader could have cooked by. If it could have changed what you did on Saturday, it belongs on this page.</p>
  <p><b>What gets fixed silently:</b> typos, broken links, formatting, and clumsy sentences. Logging those would bury the corrections that matter, which is its own way of hiding them.</p>
  <p><b>Where it goes:</b> the page itself is corrected and carries the date it changed; the next Thursday email says what changed and why; the entry lands here. Three places, because a correction only one person sees isn't a correction.</p>
  <p><b>How fast:</b> the page gets fixed as soon as we have checked it. The email correction goes out in the next issue &mdash; we don't send a separate email for it unless a number could hurt someone, in which case we do, immediately.</p>
</section>

<section>
  <div class="sectag">Telling us</div>
  <h2>How to report something</h2>
  <p>Reply to any issue of the newsletter. That reply goes to a real inbox that a person reads.</p>
  <p>You don't need to be certain, and you don't need to be polite about it. &ldquo;Your rib temp doesn't match ThermoWorks&rdquo; is a complete and useful message. If you have a source, send it &mdash; that is how we check, and it is how this gets settled quickly.</p>
  <p>If we look into it and decide the original was right, we'll tell you that too, and say why.</p>
</section>

<section class="faq">
  <h2>Common questions</h2>

  <h3>Why publish a corrections page at all?</h3>
  <p>Because a site with no corrections page is making an implicit claim &mdash; that it has never been wrong &mdash; that almost certainly isn't true. Publishing the mistakes is the only way the accuracy claims on the rest of the site mean anything. It also makes it costly for us to be sloppy, which is the actual mechanism.</p>

  <h3>Do you change old issues after they are sent?</h3>
  <p>The email that landed in your inbox can't be recalled, so the correction runs in the next one. The web version of the issue does get fixed, and it carries the date it changed so the two are never silently out of step.</p>

  <h3>What if a mistake could make someone sick?</h3>
  <p>Then it isn't waiting for Thursday. Any error in a food-safety number &mdash; a USDA minimum, a holding temperature, a poultry pull temp &mdash; gets corrected on the page immediately and sent as its own email. That is the one case where we will interrupt you.</p>
</section>

</div>

""" + cta("Thursday, 7am. Bring coffee.",
          "One free email a week: a technique explained properly, a recipe timed backward from Saturday dinner, and one piece of gear with its flaw named.")

    ld = json.dumps({
      "@context": "https://schema.org",
      "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "The Weekend Pit", "item": f"{SITE}/"},
          {"@type": "ListItem", "position": 2, "name": "Corrections", "item": f"{SITE}/corrections/"}]},
        {"@type": "WebPage",
         "name": "Corrections \u2014 The Weekend Pit",
         "description": "Every substantive correction The Weekend Pit has made, what was wrong, and how we found out. Corrections run in the next email and on the page itself, dated.",
         "url": f"{SITE}/corrections/", "inLanguage": "en-US",
         "dateModified": PUB_DATE,
         "isPartOf": {"@type": "WebSite", "name": "The Weekend Pit", "url": f"{SITE}/"},
         "publisher": {"@type": "Organization", "name": "The Weekend Pit", "url": f"{SITE}/",
                       "correctionsPolicy": f"{SITE}/corrections/",
                       "publishingPrinciples": f"{SITE}/about/"}},
        {"@type": "FAQPage", "mainEntity": [
          {"@type": "Question", "name": "Why publish a corrections page at all?", "acceptedAnswer": {"@type": "Answer", "text": "A site with no corrections page is making an implicit claim that it has never been wrong, which almost certainly isn't true. Publishing mistakes is the only way the accuracy claims on the rest of the site mean anything."}},
          {"@type": "Question", "name": "Do you change old issues after they are sent?", "acceptedAnswer": {"@type": "Answer", "text": "The email can't be recalled, so the correction runs in the next issue. The web version of the issue is fixed and carries the date it changed, so the two are never silently out of step."}},
          {"@type": "Question", "name": "What if a mistake could make someone sick?", "acceptedAnswer": {"@type": "Answer", "text": "Any error in a food-safety number \u2014 a USDA minimum, a holding temperature, a poultry pull temp \u2014 is corrected on the page immediately and sent as its own email rather than waiting for the next issue."}}]}
      ]}, indent=1, ensure_ascii=False)

    return path, page(path=path, depth=2,
                      title="Corrections \u2014 The Weekend Pit",
                      description="Every substantive correction we have made, what was wrong, and how we found out. Corrections run in the next email and on the page itself, dated \u2014 never edited away silently.",
                      og_type="website", body=body, jsonld=ld)

def write(path, content):
    out = os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  {path:<32} {len(content):>7,} bytes")

if __name__ == "__main__":
    print("Building archive pages:")
    urls = []
    p, c = about_page(); write(p, c)
    p, c = corrections_page(); write(p, c)
    p, c = archive_index(); write(p, c); urls.append(p)
    for iss in ISSUES:
        p, c = issue_page(iss); write(p, c); urls.append(p)

    # sitemap
    entries = [("/", "weekly", "1.0"), ("/temperatures/", "monthly", "0.9"),
               ("/archive/", "weekly", "0.8"), ("/about/", "monthly", "0.7"), ("/corrections/", "monthly", "0.6")
               ] + [(u, "yearly", "0.7") for u in urls if u != "/archive/"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, freq, pri in entries:
        sm += ["  <url>", f"    <loc>{SITE}{loc}</loc>", f"    <lastmod>{PUB_DATE}</lastmod>",
               f"    <changefreq>{freq}</changefreq>", f"    <priority>{pri}</priority>", "  </url>"]
    sm.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm) + "\n")
    print(f"  {'/sitemap.xml':<32} {len(entries)} urls")
