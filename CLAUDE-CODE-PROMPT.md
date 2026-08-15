# Paste this into Claude Code (on your PC)

Copy the block below, paste it into Claude Code, and let it drive. Put the unzipped
`theweekendpit-site` folder somewhere sensible first (e.g. `C:\Users\Claude\Projects\`).

---

```
I'm launching a newsletter site, The Weekend Pit, at theweekendpit.com. The site is
already built — it's a static one-page site (plain HTML + inline CSS, no framework,
no build step) sitting at C:\Users\Claude\Projects\theweekendpit-site. Read its
README.md first; it documents the structure and the one required edit.

Please do the following, and stop and ask me before anything irreversible:

1. Read README.md and index.html so you know what you're shipping.

2. Confirm the beehiiv embed status. The signup form is currently a PLACEHOLDER
   (search for REPLACE-WITH-YOUR-FORM-ID — there are exactly two occurrences, in the
   hero and in the closer). Ask me whether I have the beehiiv embed code yet:
     - If I do, replace BOTH <form> blocks with it.
     - If I don't, deploy anyway but tell me clearly that the site cannot capture a
       single email until it's swapped in, and remind me it's the last step.

3. Initialize git, commit, and create a private GitHub repo named
   theweekendpit-site under my account, then push to main.

4. Walk me through connecting it in Vercel — framework preset "Other", empty build
   command, empty output directory (it's static). Tell me exactly what to click.
   I'll do the Vercel account steps myself.

5. Once it's deployed, give me the Vercel preview/production URL and verify the page
   actually renders — fetch it and check the title and the hero headline.

6. Then help me point the domain. It's registered at Namecheap (order #211150780).
   Tell me the exact DNS records to set in Namecheap → Advanced DNS based on what
   Vercel actually displays — do not assume the IP from the README, read it off
   Vercel. Also make sure I delete Namecheap's default parking records, or the domain
   will keep resolving to the GoDaddy-style for-sale page.

7. After DNS propagates, fetch https://theweekendpit.com and confirm it serves the
   real site over HTTPS.

Notes:
- Do not add a framework, a build step, or dependencies. It's intentionally static.
- Do not commit any secrets; there are none in this project and it should stay that way.
- Brand rule that matters if you touch the markup: the full circular stamp logo is
  never used below 80px — the small "micro" mark is for anything smaller. The nav and
  footer already use the micro mark correctly.
```

---

## What you'll need to do yourself (Claude Code can't)

- Log into GitHub / Vercel / Namecheap — any credentials are yours to enter.
- Click **Deploy** in Vercel and approve the domain add.
- Create the beehiiv account and copy the embed code out of it.

Everything else it can handle.
