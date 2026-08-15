# theweekendpit.com

Static one-page site for The Weekend Pit newsletter. **No framework, no build step, no dependencies** — it's one HTML file plus assets. Deploys to Vercel as-is.

Deliberately not Next.js: this is a single landing page whose only job is to hand visitors to a beehiiv form. A build pipeline here would be maintenance with no payoff. If the merch page grows into something real (cart, inventory, checkout), revisit then.

## Structure

```
index.html                     everything — markup + inline CSS
assets/
  micro.svg                    nav mark (oxblood)
  micro-dark.svg               footer mark (bone on dark)
  logo-stamp.svg               full stamp, hero only (never below 80px)
  logo-stamp-dark.svg          full stamp for dark backgrounds
  favicon.svg / -16 / -32 / -180
  sheet-thumb.png              Temperature Sheet page-1 thumbnail
  temperature-sheet.pdf        the lead magnet
```

## Before it goes live — the one required edit

The signup form is a **placeholder**. It will not capture emails until it's replaced.

1. In beehiiv: **Grow → Subscribe Forms → Embed**, copy the embed code.
2. In `index.html`, find the two blocks marked `BEEHIIV EMBED GOES HERE` (hero and closer) and replace each `<form>…</form>` with the beehiiv embed.
3. Both forms must be replaced — there are exactly two.

Search for `REPLACE-WITH-YOUR-FORM-ID` to find them.

## Deploy (Vercel)

Same pattern as max-website: push to `main` deploys to production.

```bash
git init && git add -A && git commit -m "The Weekend Pit — landing page"
gh repo create theweekendpit-site --private --source=. --push
```

Then in Vercel: **Add New → Project → import the repo**. Framework preset **Other**, build command **empty**, output directory **empty** (it's static). Deploy.

## Domain (Namecheap → Vercel)

Domain is registered at Namecheap (order #211150780).

1. Vercel → Project → Settings → Domains → add `theweekendpit.com` and `www.theweekendpit.com`.
2. Vercel shows the required records. In Namecheap → Domain List → Manage → **Advanced DNS**, set:
   - `A` record, host `@` → the IP Vercel gives you (currently `76.76.21.21`, but **use whatever Vercel displays** — verify, don't trust this line)
   - `CNAME` record, host `www` → `cname.vercel-dns.com`
3. Delete Namecheap's default parking records (the CNAME `@` → `parkingpage` and any URL-redirect record), or the domain will keep resolving to the for-sale page.
4. Propagation is usually minutes; can take up to a few hours.

## If beehiiv also needs a subdomain

If the newsletter archive lives on beehiiv rather than here, give beehiiv `read.theweekendpit.com` (CNAME to the target beehiiv provides) and leave the root pointed at Vercel.

## Rollback

Vercel dashboard → Deployments → previous build → **Instant Rollback**. Seconds, no git needed.
