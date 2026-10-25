# Claude Motion Graphics — The Exact 10-Step Setup

**Make broadcast-quality motion graphics with Claude Code.** No After Effects. No timeline scrubbing. Just a brief, notes, and iteration — like working with a designer who never sleeps.

This repo gives you the full setup guide from the [@cosmox_origin](https://www.instagram.com/cosmox_origin) reel, plus a working HTML motion-graphics template you can open in any browser.

---

## The 10-Step Setup

### 1. Open Claude Code, pick Opus 5.5
Motion design needs strong reasoning about timing, easing, and layout. Open Claude Code and select the strongest available model (Opus-class). Weaker models fumble easing curves and spatial composition.

### 2. Install the free video skill
Claude Code supports **skills** — reusable capability packs. Install a video/rendering skill so Claude can generate and assemble video (ffmpeg-based rendering, frame extraction, format conversion). Verify with: *"list your video capabilities."*

### 3. Add the 13 motion skills
Stack motion-specific skills on top: kinetic typography, easing libraries, SVG icon animation, particle systems, camera moves, transitions, lower-thirds, progress indicators, waveform sync, color grading LUTs, caption styling, loop engineering, and export presets. Each skill is a playbook Claude follows — together they cover the full motion-design vocabulary.

### 4. Test it with one line
Before any real project, run a one-line smoke test: *"Make a 3-second 9:16 clip: the word HELLO rises in with an ease-out, orange gradient, on dark."* If the output looks right, your pipeline works. If not, fix the toolchain now — not mid-project.

### 5. Give it a proper brief
Write briefs like a creative director, not a prompt engineer. Include: **format** (9:16, 1080×1920), **duration**, **audience**, **the one message**, **visual style** (dark premium + orange accents), **reference frames** if you have them, and **what to avoid** (no emojis, no stock-looking cards).

### 6. Give notes like you would to a designer
Iterate in plain language: *"the heading feels cramped, give it more air"*, *"make the badge pop half a second earlier"*, *"this transition is too harsh, soften it."* Claude revises the code, re-renders, and shows you the new version. Three to five note rounds is normal.

### 7. Turn 5 frames you love into MOTION.md
Screenshot 5 frames from motion work you admire. Describe each in `MOTION.md` at your project root: what moves, how fast, what easing, what the composition feels like. This becomes your **taste file** — Claude's reference for "what good looks like" in your style.

### 8. Make Claude read it before every build
Add one line to your project instructions: *"Read MOTION.md before generating any motion graphics."* This is the step that makes output look like **yours**, not generic AI slop. Skip it and every render looks like everyone else's.

### 9. Add Apple's motion rules, then ask for an audit
Append platform motion guidelines (Apple's Human Interface Guidelines motion section is the gold standard: consistent easing, purposeful movement, reduced-motion respect) to your instructions. Then ask: *"Audit this render against MOTION.md and Apple's motion rules. List violations."* Fix what it finds.

### 10. Use real components, not drawn ones
The difference between amateur and pro: real SVG icons, real brand marks in original colors, real product screenshots — never clip-art shapes pretending to be UI. Feed Claude actual assets and tell it to use them as-is.

---

## Try the template

`template.html` is a minimal working example of the style: dark premium background, kinetic headline, animated badge, 9:16.

1. Open `template.html` in Chrome.
2. Open DevTools → device toolbar → 1080×1920.
3. Screenshot or screen-record any frame.

To render video: screenshot frames at timestamps via Puppeteer (`node render.js` pattern) and assemble with ffmpeg. See the comments in `template.html`.

---

## Files

| File | What it is |
|---|---|
| `README.md` | This guide |
| `template.html` | Working 9:16 motion-graphics starter template |
| `fonts/` | Montserrat variable font (SIL Open Font License) |

## License

MIT — use it, remix it, ship client work with it.

---

Built by [CosmoX Origin](https://www.instagram.com/cosmox_origin) — AI systems that reduce cost, time & chaos.
