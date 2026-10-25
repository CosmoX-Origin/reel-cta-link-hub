# Reel CTA Link Hub — Cosmox Origin

**The problem:** A reel says "Comment MOTION / COACH / LEADS and I'll send you the guide", but the guide lives in a DM draft, a local file, or nowhere at all. Commenters wait, the creator repeats the same DM, and some promises never get fulfilled.

**The solution:** One link for every reel comment CTA. A visitor searches the exact word from the reel and gets the resource instantly — view it on the page, copy the text, or open the plain file. No DM wait, no separate link per reel, no fake links.

## Use it

1. Open `index.html` (or the GitHub Pages site once enabled for this repo).
2. Type the comment word from the reel, for example `MOTION`.
3. Click **View resource** to read it, **Copy text** to copy it, or **Open file** for the plain Markdown version.

Put this hub's link in the Instagram bio. Every reel then only needs to name its word.

## Resources in this hub

| Comment word | Resource | Status |
|---|---|---|
| MOTION | Claude Motion Graphics: 10-Step Setup | Ready — `resources/MOTION.md` |
| COACH | Your Own AI Coach | Ready — `resources/COACH.md` |
| AUDIT | The Business Audit Prompt | Ready — `resources/AUDIT.md` |
| CLAUDE | Claude Starter Guide: 60-Minute AI Employee | Ready — `resources/CLAUDE.md` |
| LEADS | AI Closer Setup Checklist | Ready — `resources/LEADS.md` |
| SOLO | Run a 1-Person Company with AI | Ready — `resources/SOLO.md` |
| TEAM | Your 35 AI Team Add-ons | Ready — `resources/TEAM.md` |
| NUMBER | — | Coming soon (no verified resource yet, so no fake link) |

`resources.json` is the machine-readable manifest of the same list, so other tools can read the hub without scraping the page.

## Add a new CTA (2 minutes, for the creator)

1. Drop the resource file in `resources/`, for example `resources/NEWWORD.md`.
2. Add one entry to `resources.json`: word, title, description, status, file.
3. Rebuild `index.html` with `python3 build.py` (it embeds the resources) or add the entry to the page the same way.

**Rule that keeps this hub honest:** if a resource is not ready, its status stays `coming-soon`. Never link a word to a resource that does not exist.

## Run it locally

No build step, no backend, no database:

```bash
python3 build.py
# then open index.html in a browser
```

## Built by

Cosmox Origin — follow [@cosmox_origin](https://www.instagram.com/cosmox_origin) for AI workflows that actually work.
