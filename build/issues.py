# -*- coding: utf-8 -*-
"""Content of record for the web archive. Mirrors claude/weekend-pit-issue-NN.md.

Email-only sections (Reader's Pit, the poll, the PS/forward line) are deliberately
absent: the archive page is the evergreen half of the issue, not an email replica.
"""

PUB_DATE = "2026-08-21"

ISSUES = [
{
 "num": "01",
 "slug": "the-stall",
 "seo_title": "Why brisket and pork butt stall at 150°F — and three ways through",
 "h1": "The stall isn't stuck. It's sweating.",
 "description": "Big cuts flatline around 150°F internal for hours. It isn't melting fat or collagen — it's evaporative cooling. Here's the physics, the three honest ways through, and a pulled-pork timeline counted backward from Saturday dinner.",
 "standfirst": "Sometime around hour three on Saturday, your thermometer is going to stop moving — and stay stopped long enough to make you question the fire, the meat, and several of your life choices.",
 "answer": [
   "A stall is <b>evaporative cooling</b>, not a broken fire. Around <b>150°F</b> internal, moisture pushed to the surface of the meat evaporates fast enough that the cooling exactly cancels the heat of your pit, and the temperature flatlines — sometimes for hours.",
   "Three honest ways through: ride it out for the best bark, wrap at 150–160°F to stop the evaporation, or run the pit hotter. Pick one <em>before</em> you light the fire."
 ],
 "deep_heading": "Why the stall happens — and three honest ways through it",
 "deep": """
<p><em class="lead">The why.</em> Big cuts climb steadily to about 150°F internal, then flatline &mdash; sometimes for hours &mdash; before climbing again. For decades pitmasters blamed melting fat or dissolving collagen. Then physicist Greg Blonder actually tested it, and the answer turned out to be the same reason you don't overheat on a July run: evaporative cooling. Around 150°F, moisture pushed to the surface of the meat starts evaporating fast enough that the cooling exactly cancels the heat of your pit. Your pork butt is sweating. In Blonder's test rig the standoff held for about six hours before the surface dried out and the temperature moved again. Nothing is wrong. Nothing is broken. It's physics, holding the door.</p>

<h3>Ride it out</h3>
<p>Dry surface eventually wins. Deepest bark, longest cook, zero effort. The price is time you have to build in up front &mdash; pitmasters pad the schedule with buffer hours and let a long rest absorb the extra. Choose this when dinner is flexible.</p>

<h3>Wrap it &mdash; the Texas crutch</h3>
<p>Somewhere in the 150&ndash;160°F range, wrap the meat tight. No evaporation, no cooling, no stall. Foil is the full crutch: it braises the meat in its own juices, fastest through the stall, softest bark. Butcher paper is the compromise &mdash; it breathes a little, so it's slower than foil but kinder to bark. For pulled pork, use foil without guilt: the bark gets mixed in when you pull it anyway. Save the paper debate for brisket, where bark is the trophy.</p>

<h3>Run hotter</h3>
<p>The stall shrinks as pit temperature climbs, and approaching 300°F it can disappear entirely. Legitimate technique &mdash; but it trades away some of the low-and-slow margin for error, so it's the advanced lane, not the Saturday default.</p>

<div class="flag"><b>The one mistake everyone makes:</b> deciding mid-stall. It's 2pm, the butt has read 157°F for two hours, guests land at six, and panic starts negotiating &mdash; crank the pit, pull it early, google furiously with rib-rub thumbs. Every bad outcome starts there. The fix costs nothing: pick your stall plan before you light the fire.</div>

<p class="fence">&ldquo;It's not stuck &mdash; it's sweating. Wrap it and it can't sweat; wait it out and the bark's better.&rdquo;</p>
""",
 "cook_heading": "Pulled pork for a crowd — and a front-row seat to the stall",
 "cook_intro": "A bone-in pork butt is the best teacher in barbecue: cheap, forgiving, and it stalls just like a brisket without a brisket's consequences.",
 "timeline": [
   ("Thursday", "Buy an 8-lb bone-in pork butt (shoulder). While you're out: heavy-duty foil."),
   ("Friday, 8pm", "Trim the hard fat cap to ~¼\". Salt and rub all over. Fridge, uncovered, overnight."),
   ("Saturday, 4:15am", "Light the pit. Coffee."),
   ("4:45am", "Butt on, fat side down. Pit at <b>250°F</b> and hold it there."),
   ("~8:00am", "Internal hits ~150°F. The stall begins. You, unlike everyone else, smile."),
   ("At 160°F internal", "Wrap tight in two layers of foil, back on the pit."),
   ("~3:30–4:30pm", "Start probing. Pull at <b>195–205°F internal</b>, when the probe slides in everywhere like warm butter and the bone wiggles free."),
   ("Off the pit", "Rest, still wrapped, in a dry cooler with towels &mdash; <b>1 hour minimum</b>. Finishes early? That cooler hold keeps it hot for 3–4 hours, which is why this timeline can't really fail."),
 ],
 "finish": ("6:00pm", "Pull it, season the pile with a pinch more rub, serve."),
 "needs": "The butt, kosher salt, a simple rub (¼ cup coarse black pepper, 2 tbsp paprika, 1 tbsp garlic powder, 1 tbsp brown sugar &mdash; salt separately and generously), foil, a probe or instant-read thermometer, buns if you're civilized about it.",
 "rig": "The numbers above assume a pellet grill or any smoker that holds 250°F. On a kettle, set up two-zone with a full chimney plus 3–4 wood chunks, and plan to feed the fire roughly hourly &mdash; the butt doesn't care what it's cooked on, only that the pit holds steady.",
 "numbers": "Pit 250°F · wrap at 160°F internal · pull at 195–205°F internal · rest 1hr+ wrapped.",
 "safety": "USDA's safety floor for whole-cut pork is 145°F + 3-minute rest &mdash; you'll blow past it by lunch. Tenderness is the reason for the rest of the climb.",
 "find_heading": "ThermoWorks ThermoPop 2 — $39",
 "find": """
<p>Everything in this issue assumes you can actually read the meat's mind, and the reviewer consensus for doing that on a budget is the ThermoPop 2: 2&ndash;3 second reads, ±1°F by ThermoWorks' own spec, and a backlit screen that flips to stay readable in either hand &mdash; including at the 4:45am light.</p>
<p>The flaw, because there's always a flaw: the little probe cap is practically engineered to disappear into a junk drawer, and it's a beat slower than the Thermapen ONE ($74 on sale as we wrote this, usually ~$115) &mdash; the buy-once version for the cook who already knows this hobby is permanent. Start with the $39 one.</p>
""",
 "sources": [
   ("AmazingRibs — The Stall and the Texas Crutch", "https://amazingribs.com/technique-and-science/more-cooking-science/understanding-and-beating-barbecue-stall-bane-all-barbecue/"),
   ("SmokedBBQSource — Smoking Times &amp; Temperatures", "https://www.smokedbbqsource.com/smoking-times-temperatures/"),
   ("AmazingRibs — Food Temperature Guide", "https://amazingribs.com/technique-and-science/more-cooking-science/safe-serving-temperatures/"),
   ("foodsafety.gov — Safe Minimum Internal Temperatures", "https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures"),
 ],
},
{
 "num": "02",
 "slug": "3-2-1-ribs",
 "seo_title": "Is the 3-2-1 rib method actually good? An honest audit",
 "h1": "3-2-1 ribs: guideline, not gospel",
 "description": "The internet's favorite rib method, fact-checked. What 3-2-1 gets right, where it quietly ruins racks, why the bend test beats the clock — and St. Louis spares timed backward from Saturday dinner.",
 "standfirst": "Type &ldquo;how to smoke ribs&rdquo; and the internet answers in unison: 3-2-1. Tidy as a phone number, and about as related to what's happening inside the meat.",
 "answer": [
   "<b>3-2-1 is a recipe for fall-off-the-bone ribs, not a rule.</b> Three hours smoked, two wrapped, one to finish will reliably tenderize spare ribs &mdash; but two hours in foil pushes most racks past a clean bite, and baby backs get overrun entirely.",
   "Cook to feel instead: pick the rack up from one end with tongs and bounce it. Done ribs crack on the surface and threaten to break, usually around <b>190–200°F</b> between the bones. Published targets range 180–203°F, so the feel outranks the number."
 ],
 "deep_heading": "What 3-2-1 gets right, and where it goes wrong",
 "deep": """
<p><em class="lead">Why it's everywhere.</em> The 3-2-1 method promises what beginners want most: a clock instead of judgment. Smoke spares at 225&ndash;250°F for 3 hours, wrap them in foil for 2, unwrap for 1, sauce at the end &mdash; and you cannot serve tough ribs. That promise is real, and it's the honest reason the method spread: two hours of braising in foil will tenderize anything. The question the name never asks is whether it tenderizes too far.</p>

<p><em class="lead">What the evidence says.</em> Meathead Goldwyn, who has spent a couple of decades testing this stuff, doesn't wrap ribs at all and quotes a competition pitmaster flatly: two hours in foil is &ldquo;waaaay too long&rdquo; for pork ribs. His crutch testing caps a rib wrap at one hour before the texture slides toward mush. Even write-ups that teach 3-2-1 concede the bark softens and the meat lands at fall-off-the-bone &mdash; which sounds like a compliment and isn't. Competition judges score ribs that <em>tug</em> off the bone with a clean bite mark; meat that drops off has crossed from barbecue into pot roast's airspace. And baby backs, leaner and smaller, get overrun by the full schedule &mdash; even 3-2-1's defenders reroute them to 2-2-1.</p>

<h3>So when is 3-2-1 right?</h3>
<p>When fall-apart is genuinely what your table wants &mdash; and for plenty of tables it is. Feeding a crowd that reads any chew as &ldquo;tough&rdquo;? Big, meaty spare racks, foil, minimal added liquid, sugar in check, 225&ndash;250°F and not a degree over &mdash; 3-2-1 will hand you soft, sweet, crowd-pleasing ribs on schedule. That's a legitimate style choice. Just make it a choice, not a default you inherited from a search result.</p>

<div class="flag"><b>The one mistake everyone makes:</b> obeying the numbers in the name. Racks differ &mdash; weight, thickness, how the pit ran that day &mdash; and the clock doesn't know your rack. Cooks who trust &ldquo;2&rdquo; leave ribs in foil while the texture drives past done. The fix is the bend test: pick the slab up from one end with tongs and bounce it gently. Done ribs crack on the surface and threaten to break, and you'll typically read somewhere around 190&ndash;200°F between the bones. USDA's pork floor of 145°F passed hours ago &mdash; this extra climb is purely about tenderness.</div>

<p class="fence">&ldquo;3-2-1 isn't wrong &mdash; it's a recipe for fall-apart. If you want ribs that tug, put down the clock and pick up the rack.&rdquo;</p>
""",
 "cook_heading": "St. Louis spares, cooked to the bend — dinner at six",
 "cook_intro": "No wrap this week &mdash; ribs are thin enough that the stall barely bites. One afternoon, one fire, ribs with actual bark.",
 "timeline": [
   ("Thursday", "Buy two racks of St. Louis&ndash;cut spares (~3 lb each). Check the membrane's still on the back &mdash; you want to remove it yourself."),
   ("Saturday, 10:00am", "Peel the membrane (slide a butter knife under it at one bone, grip with a paper towel, pull). Rub both racks. No overnight needed."),
   ("10:45am", "Light the pit."),
   ("11:15am", "Racks on, meat side up, pit at <b>250°F</b> steady. Leave the lid shut."),
   ("4:15pm", "First bend test: tongs at one end, bounce. Cracking surface = closing time. Reading between bones ~<b>190–200°F internal</b>. Not there? Check again every 30 minutes."),
   ("4:45pm <em>(only if behind)</em>", "Nudge the pit to 275°F &mdash; heat shortens the wait; that's stall physics working for you."),
   ("Last 15 min", "Sauce, if saucing &mdash; it needs only that long to set. Glaze, don't drown."),
   ("~5:40pm", "Off. Rest under loose foil while the table gets set."),
 ],
 "finish": ("6:00pm", "Slice between the bones. Serve to people who think they don't like &ldquo;chewy&rdquo; ribs, and watch."),
 "needs": "Two St. Louis racks, the house rub (¼ cup coarse black pepper, 2 tbsp paprika, 1 tbsp garlic powder, 1 tbsp brown sugar &mdash; salt separately and generously), sauce if that's your politics, tongs, an instant-read.",
 "rig": "Running way behind at 4:30? One hour in foil, maximum &mdash; that's the ceiling before texture pays for it.",
 "numbers": "Pit 250°F · done by bend test, ~190–200°F internal between bones · sauce last 15 min.",
 "safety": "USDA's pork floor is 145°F, long since passed by the time ribs are tender. The climb past it is for texture, not safety.",
 "find_heading": "Cotton glove liners (under nitrile) — $2.99",
 "find": """
<p>The cheapest legitimate upgrade in barbecue: thin cotton liners worn under ordinary food-safe nitrile gloves. The cotton buffers the heat, the nitrile keeps things sanitary, and you can pull hot pork or lift a whole rack with your actual hands. Malcom Reed calls the combo &ldquo;the easiest, cheapest and most sanitary solution,&rdquo; and swapping a dirty nitrile layer for a clean one mid-cook takes ten seconds.</p>
<p>The honest limits: this is for hot <em>meat</em>, not fire &mdash; coals, chimneys and grates still demand real insulated gloves &mdash; and the nitrile layer is disposable, so you'll burn through a box over a season. Liners run about $2.99 direct from Lane's BBQ; pair with any food-safe nitrile box.</p>
""",
 "sources": [
   ("AmazingRibs — Last Meal Ribs", "https://amazingribs.com/best-barbecue-ribs-recipe/"),
   ("Destination BBQ — The 3-2-1 Method", "https://destination-bbq.com/glossary/3-2-1-method-for-ribs/"),
   ("ThermoWorks — Smoked Ribs Guide", "https://www.thermoworks.com/blogs/thermoblog/ribs"),
   ("foodsafety.gov — Safe Minimum Internal Temperatures", "https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures"),
 ],
},
{
 "num": "03",
 "slug": "chicken-skin",
 "seo_title": "Why smoked chicken skin comes out rubbery — and the one fix",
 "h1": "Chicken skin needs heat, not patience",
 "description": "Smoke a chicken at 250°F and the skin comes off the pit like a rubber glove. It isn't your smoker — it's that poultry wants the opposite of what brisket wants. The physics, the fix, and a spatchcock bird on the table by six.",
 "standfirst": "Everything you know about barbecue says low and slow. Then you smoke a chicken at 250°F, and the skin comes off the pit the exact texture of a rubber glove.",
 "answer": [
   "Smoke chicken at <b>300–350°F</b>, not 225–250°F. Crisp skin needs the fat underneath to render and the water inside it to leave, and both need real heat. At 250°F you cook the meat through without ever rendering the skin — so it stays flabby.",
   "Then spatchcock the bird so breast and thigh finish together, and temp them separately: <b>165°F</b> in the thickest part of the breast (the USDA minimum for all poultry) and <b>175°F+</b> in the thigh."
 ],
 "deep_heading": "Why low and slow ruins chicken skin",
 "deep": """
<p><em class="lead">The why.</em> Skin is fat and water held in a protein net. Crisp happens when the fat under it renders out and the water in it leaves &mdash; and both of those need real heat. At 250°F you're in the worst possible spot: hot enough to cook the meat through, too cool to render the fat or drive out the moisture. So the fat stays put, the water stays trapped, and what you serve is a cooked raincoat. The low-and-slow gospel works beautifully on brisket because you're melting collagen for ten hours. A chicken is done in ninety minutes and has no such project. Every hour you spend being patient with a bird is an hour its skin spends turning to latex.</p>

<h3>Run the pit hot</h3>
<p>300°F is the floor for decent skin; ThermoWorks cooks spatchcock chicken at exactly that, specifically to dodge &ldquo;the leathery skin endemic to this cooking method.&rdquo; Higher works too &mdash; 325&ndash;350°F is friendly territory, and a bird can take it.</p>

<h3>Or split the difference</h3>
<p>Want more smoke flavor than a hot pit gives? Smoke low for the first 30 minutes &mdash; smoke penetrates raw meat better than cooked &mdash; then ramp hard to 425°F to finish. You get the flavor of the low phase and the skin of the hot one.</p>

<h3>Dry the skin first</h3>
<p>Salt the bird uncovered in the fridge overnight; the air pulls surface moisture out, so the pit doesn't have to. Adding a little baking powder to the salt goes further &mdash; it raises the skin's pH so proteins brown faster, and it bubbles the surface into more surface area. This is why restaurant wings shatter and yours don't.</p>

<div class="flag"><b>The one mistake everyone makes:</b> treating the whole bird as one piece of meat. Breast and thigh want different endings &mdash; breast dries out past 165°F, while thighs stay tough there and only turn silky up around 175&ndash;185°F. Cook to one number and you're choosing which half to sacrifice. The fix is geometry, not skill: spatchcock the bird &mdash; cut out the backbone, press it flat &mdash; and the thighs sit exposed at the hot edges while the breast rides lower and cooler. Same pit, same clock, both halves right.</div>

<p>Temp them separately: <b>165°F in the thickest part of the breast</b> &mdash; that's the USDA safety number for all poultry and it's non-negotiable &mdash; and 175°F+ in the thigh. Carryover keeps climbing about 5°F after the bird comes off, so a breast pulled right at 165°F rests up, not down.</p>

<p class="fence">&ldquo;Chicken isn't brisket. Skin needs heat, and a flat bird cooks even.&rdquo;</p>
""",
 "cook_heading": "Spatchcock chicken, skin that actually crackles",
 "cook_intro": "Ninety minutes of cooking, one bird, no stall, no drama. This is the cook you'll repeat on a Tuesday.",
 "timeline": [
   ("Friday, 7pm", "Spatchcock: kitchen shears up both sides of the backbone, lift it out, flip the bird breast-up and press down hard until it cracks flat. Pat bone dry."),
   ("Friday, 7:15pm", "Salt it &mdash; 1 tsp kosher salt per pound &mdash; plus 1 tsp baking powder mixed in, worked over the skin. Uncovered on a rack in the fridge overnight. <b>This step is the skin.</b>"),
   ("Saturday, 3:45pm", "Bird out of the fridge. Rub under and over the skin if you're rubbing."),
   ("4:00pm", "Light the pit for <b>325°F</b>. Higher than feels right. That's the point."),
   ("4:30pm", "Bird on, skin side up, thighs toward the hotter edge. Lid shut."),
   ("~5:30pm", "Start temping. <b>Pull at 165°F in the thickest part of the breast</b> and 175°F+ in the thigh. Thigh lagging? Give it ten more minutes &mdash; the breast has carryover to spare."),
   ("Off the pit", "Rest 10 minutes, uncovered. Foil now would steam the skin you just spent 24 hours earning."),
 ],
 "finish": ("6:00pm", "Cut into quarters through the flattened bird. Serve."),
 "needs": "One 4–5 lb chicken, kosher salt, 1 tsp baking powder (aluminum-free tastes cleaner), your rub, kitchen shears, an instant-read.",
 "rig": "Any pit that holds 325°F. On a kettle, bank all the coals to one side and put the bird on the cool side, skin up &mdash; cover vents wide open, and rotate once at the halfway mark.",
 "numbers": "Pit 325°F · breast 165°F internal · thigh 175–185°F · rest 10 min uncovered · ~1.5 hours on the pit.",
 "safety": "165°F is the USDA minimum for all poultry, whole or in parts. Some professional cooks pull breast at 158°F and ride carryover up to safe; we print 165°F, because a number that reads as “pull poultry under temp” gets copied without the context around it.",
 "find_heading": "Kitchen shears that survive a backbone — from $19.99",
 "find": """
<p>Spatchcocking is a ten-second job with the right shears and a wrestling match with the wrong ones &mdash; the flimsy pair in your drawer will fold on a chicken's backbone and take a knuckle with it. Reviewed's testing put OXO's Good Grips poultry shears on top at about $30, for the spring-loaded tension and, more importantly, blades that come apart for cleaning &mdash; a real consideration for a tool you use exclusively on raw poultry.</p>
<p>Their budget pick, Gerior at $19.99, cuts just as willingly, and its flaw is exactly that: the blades don't separate and they're hand-wash only, so raw-chicken cleanup takes actual attention. Buy the cheap ones if you'll be diligent; buy the OXO if you know yourself.</p>
""",
 "sources": [
   ("ThermoWorks — Smoked Spatchcock Chicken, Alabama Style", "https://blog.thermoworks.com/spatchcock-chicken-alabama-style/"),
   ("ThermoWorks — Smoked Chicken Wings: a Thermal Trick for Crisp Skin", "https://blog.thermoworks.com/smoked-chicken-wings/"),
   ("AmazingRibs — Food Temperature Guide", "https://amazingribs.com/technique-and-science/more-cooking-science/safe-serving-temperatures/"),
   ("foodsafety.gov — Safe Minimum Internal Temperatures", "https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures"),
 ],
},
]

# ---------------------------------------------------------------------------
# Corrections log — rendered at /corrections/
#
# Append newest-first. Only substantive corrections belong here: a number, a
# claim, a source, or anything a reader could have acted on. Typos, formatting
# and broken links are fixed silently — logging those would bury the real ones.
#
# Each entry:
#   date    ISO date the correction was made
#   where   human name of the page or issue it affected, e.g. "Issue No. 02"
#   url     path on this site, or None if it only ever went out by email
#   what    what was wrong
#   now     what it says now
#   how     how we found out, e.g. "reader reply", "our own re-check"
# ---------------------------------------------------------------------------

CORRECTIONS = [
]
