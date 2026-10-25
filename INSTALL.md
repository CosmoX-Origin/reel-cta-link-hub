# Installation and Usage Guide — Reel CTA Link Hub

**Short answer: there is nothing to install to read and use the guides.**
This is not an app, not a paid tool, and it needs no API key, no database,
and no backend. You only need a browser. Installation is only needed if you
want your own copy on your computer, or if you want to turn the MOTION
template into a video.

## Option 1: Use it right on GitHub (no installation, recommended for most people)

1. Open the repository: https://github.com/CosmoX-Origin/reel-cta-link-hub
2. In the README table, find your word, for example `MOTION`, `COACH`, or `LEADS`.
3. Click the file link, for example `resources/MOTION.md`.
4. Read it on GitHub, or click **Raw** and copy the whole text.
5. Paste it into Claude (or the tool the guide is about) and follow the steps.

You do **not** need a GitHub account or login to read and copy. Login is only
asked if you click Star, Fork, Download, or Edit.

> Note: on GitHub, `index.html` shows as code, not as a rendered page. That
> is normal GitHub behaviour. To use the search page as a real website,
> download it (Option 2 or 3) and open it locally, or wait for GitHub Pages
> to be enabled for this repository.

## Option 2: Download it (no git needed)

1. On the repository page, click the green **Code** button, then
   **Download ZIP**.
2. Unzip the folder on your computer or phone.
3. Open `index.html` in any browser (Chrome works best).
4. Type a word in the search box, for example `COACH`, click **View resource**
   to read it, or **Copy text** to copy it.

## Option 3: Clone it with git (for developers)

```bash
git clone https://github.com/CosmoX-Origin/reel-cta-link-hub.git
cd reel-cta-link-hub
# Open index.html in your browser, no server needed.
```

To rebuild the search page after adding a resource:

```bash
python3 build.py
# This re-embeds resources/*.md and resources.json into index.html.
```

Requirements for this option only: `git` and, for rebuilding, `python3`.
No other software is required.

## How to use a guide inside Claude (example)

Using `COACH` as an example:

1. Open `resources/COACH.md` and copy all of it.
2. Open https://claude.ai, go to **Projects**, then **New Project**,
   and name it `AI COACH`.
3. Paste the guide's Project Instructions where the guide tells you to.
4. Answer the guide's questions about your goal, fitness level, schedule,
   and equipment, in the project chat.

The same pattern works for the other guides: copy the file, paste it where
the guide says, then answer its questions. Each guide says exactly where
to paste and what to do next, so you do not need to guess.

## How to use the MOTION template (optional, for video makers)

The MOTION guide comes with a working template:

- File: `resources/motion-template.html`
- Font: `resources/fonts/montserrat-var.ttf` (already included, so the
  template looks right when opened from this folder)

To preview it:

1. Download or clone the repository (Option 2 or 3) so the template and its
   font stay in the same folder structure.
2. Open `resources/motion-template.html` in Chrome.
3. Set the browser viewport to 1080 x 1920 (DevTools device toolbar) to see
   the 9:16 frame.

To render it as video, follow the Puppeteer + ffmpeg steps written in the
comments at the top of `motion-template.html`. That step needs Node.js,
Puppeteer, and ffmpeg on your computer. It is optional: previewing and
screenshotting the template needs only a browser.

## Make your own hub (Fork)

1. On the repository page, click **Fork** (this step needs a GitHub login).
2. In your copy, add a file under `resources/` and an entry in
   `resources.json`, as described in [CONTRIBUTING.md](CONTRIBUTING.md).
3. Run `python3 build.py` and commit the updated `index.html`.

Your fork is a separate copy. Changes you make there never change the
original Cosmox Origin repository.

## Troubleshooting

| Problem | Fix |
|---|---|
| GitHub asks me to sign in | You clicked Star, Fork, Download, or Edit. For reading only, just open the file link directly, no sign-in needed. |
| `index.html` shows code on GitHub | Normal. GitHub does not render HTML files as pages. Download the repo and open `index.html` locally. |
| MOTION template looks wrong | Open it from the downloaded/cloned folder, not alone, so it can find `fonts/montserrat-var.ttf` next to it. |
| A word shows "coming soon" | That resource is not ready yet, and no fake link is given. Check back later, or use one of the ready guides. |

## What you need, in one line

- To read a guide: a browser, nothing else.
- To use a guide in Claude: a Claude account, nothing else.
- To clone or rebuild: git and python3, nothing else.
- To render MOTION as video: Node.js, Puppeteer, and ffmpeg, optional.
