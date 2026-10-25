#!/usr/bin/env python3
"""Build the Reel CTA Link Hub from Abhishek's own verified DM/guide files.

Sources are read, never hand-copied, so the hub can never promise a
resource that does not exist. NUMBER has no verified file, so it is
listed as coming-soon with no fake link.
"""
import json
import re
from pathlib import Path

HOME = Path.home()
OUT = Path(__file__).resolve().parent
RES = OUT / "resources"
RES.mkdir(exist_ok=True)

DM = HOME / "workspace/goals/1m-revenue-by-dec-2026/dm-assets"
MOTION_SRC = HOME / "workspace/github-repos/claude-motion-graphics/README.md"
CLAUDE_SRC = HOME / "workspace/goals/daily-aiagently-slide-reels/hidden_files/claude-starter-guide-dm.md"

def read_text(path):
    return Path(path).read_text(encoding="utf-8").strip() + "\n"

def claude_guide():
    text = read_text(CLAUDE_SRC)
    m = re.search(r"```\n(.*?)\n```", text, re.S)
    return (m.group(1).strip() + "\n") if m else text

SPECS = [
    ("MOTION", "Claude Motion Graphics: 10-Step Setup",
     "Claude se broadcast-style motion graphics banane ka poora setup, plus ek working 9:16 starter template.",
     MOTION_SRC, "MOTION.md"),
    ("COACH", "Your Own AI Coach",
     "Claude Projects me apna personal AI coach banane ka 5-step setup.",
     DM / "coach-guide-dm.txt", "COACH.md"),
    ("AUDIT", "The Business Audit Prompt",
     "Business ko 6 areas me audit karne wala ruthless prompt, money leaks ke saath aur 30-day fix plan.",
     DM / "audit-prompt-dm.txt", "AUDIT.md"),
    ("CLAUDE", "Claude Starter Guide: 60-Minute AI Employee",
     "Claude ko sirf 60 minute me apna AI employee banane ka starter guide.",
     None, "CLAUDE.md"),
    ("LEADS", "AI Closer Setup Checklist",
     "Leads ko inbox me marne se rokne ka checklist: 60-second reply, Day 1-3-7 follow-up, zero-slip CRM.",
     DM / "leads-closer-checklist-dm.txt", "LEADS.md"),
    ("SOLO", "Run a 1-Person Company with AI",
     "Bina team ke AI employees ke saath 1-person company chalane ka poora guide.",
     DM / "solo-guide-dm.txt", "SOLO.md"),
    ("TEAM", "Your 35 AI Team Add-ons",
     "Claude Code ke liye 35 add-ons, har ek ke install command ke saath.",
     DM / "team-35-links-dm.txt", "TEAM.md"),
]

entries = []
for word, title, desc, src, fname in SPECS:
    if word == "CLAUDE":
        body = claude_guide()
    else:
        body = read_text(src)
    (RES / fname).write_text(body, encoding="utf-8")
    entries.append({"word": word, "title": title, "description": desc,
                    "status": "ready", "file": f"resources/{fname}", "body": body})

entries.append({"word": "NUMBER", "title": "Coming soon",
                "description": "Is word ka verified resource abhi hub me nahi hai, isliye yahan koi jhootha link nahi diya gaya hai.",
                "status": "coming-soon", "file": None, "body": ""})

manifest = [{k: v for k, v in e.items() if k != "body"} for e in entries]
(OUT / "resources.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

data_json = json.dumps(entries, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Reel CTA Link Hub | Cosmox Origin</title>
<meta name="description" content="One link for every Cosmox Origin reel comment CTA. Search the word from the reel and get the resource instantly, no DM wait.">
<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; background: #f4efe4; color: #111; }}
header {{ padding: 28px 20px 8px; max-width: 860px; margin: 0 auto; }}
h1 {{ font-size: 34px; line-height: 1.1; margin: 0 0 10px; }}
p.lead {{ font-size: 17px; line-height: 1.55; margin: 0 0 18px; color: #333; }}
.pill {{ display: inline-block; background: #111; color: #fff; border-radius: 999px; padding: 6px 12px; font-size: 13px; font-weight: 700; }}
.pill span {{ color: #ff7a1a; }}
main {{ max-width: 860px; margin: 0 auto; padding: 10px 20px 40px; }}
#search {{ width: 100%; padding: 14px 16px; font-size: 17px; border: 2px solid #111; border-radius: 12px; background: #fff; }}
.hint {{ color: #555; font-size: 14px; margin: 10px 2px 18px; }}
.card {{ background: #fff; border: 1px solid #ddd; border-radius: 16px; padding: 18px; margin-bottom: 14px; }}
.card h2 {{ margin: 0 0 6px; font-size: 20px; }}
.word {{ display: inline-block; background: #111; color: #fff; border-radius: 8px; padding: 5px 10px; font-weight: 800; letter-spacing: 1px; }}
.badge {{ float: right; font-size: 12px; font-weight: 700; padding: 5px 9px; border-radius: 999px; }}
.badge.ready {{ background: #e6f4ea; color: #137333; }}
.badge.soon {{ background: #fef3e2; color: #a15c00; }}
.card p {{ color: #444; line-height: 1.5; }}
button {{ cursor: pointer; border: 0; border-radius: 10px; padding: 10px 14px; font-size: 15px; font-weight: 700; }}
.btn-dark {{ background: #111; color: #fff; }}
.btn-line {{ background: #fff; color: #111; border: 2px solid #111; margin-left: 8px; }}
pre {{ display: none; white-space: pre-wrap; word-wrap: break-word; background: #f4efe4; border-radius: 12px; padding: 16px; font-size: 14px; line-height: 1.6; margin-top: 14px; }}
pre.open {{ display: block; }}
section.how {{ background: #111; color: #fff; border-radius: 16px; padding: 20px; margin-top: 26px; }}
section.how h2 {{ margin-top: 0; }}
section.how ol {{ line-height: 1.7; }}
section.how code {{ color: #ffb380; }}
footer {{ text-align: center; color: #666; font-size: 14px; padding-bottom: 30px; }}
a {{ color: #ff7a1a; }}
@media (max-width: 520px) {{ h1 {{ font-size: 28px; }} .btn-line {{ margin-left: 0; margin-top: 8px; }} }}
</style>
</head>
<body>
<header>
<span class="pill">COSMOX ORIGIN <span>&bull;</span> REEL RESOURCES</span>
<h1>Reel CTA Link Hub</h1>
<p class="lead">Reel par jo word comment karne ko kaha gaya tha, wahi word yahan search karo. Resource turant milega, DM ka wait nahi. Ek hi link, har reel ke liye.</p>
</header>
<main>
<input id="search" type="search" placeholder="Search the comment word, e.g. MOTION, COACH, LEADS" autocomplete="off">
<p class="hint" id="count"></p>
<div id="cards"></div>
<section class="how">
<h2>Creator ke liye: naya CTA 2 minute me add karo</h2>
<ol>
<li>Resource ki file <code>resources/</code> me daalo, jaise <code>resources/NEWWORD.md</code>.</li>
<li><code>resources.json</code> me ek entry add karo: word, title, description, status aur file.</li>
<li>Is page ko dobara build karo ya entry ko seedha index me daalo. Bio me sirf is hub ka link rakho, har reel ke liye alag link nahi.</li>
</ol>
<p>Rule: koi resource ready nahi hai to uska status <code>coming-soon</code> rakho. Jhootha link kabhi mat do.</p>
</section>
</main>
<footer>Built by Cosmox Origin &middot; Follow @cosmox_origin for AI workflows that actually work.</footer>
<script>
const RESOURCES = {data_json};
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
function render(filter) {{
  const q = (filter || "").trim().toLowerCase();
  const list = RESOURCES.filter(r => !q || r.word.toLowerCase().includes(q) || r.title.toLowerCase().includes(q) || r.description.toLowerCase().includes(q));
  document.getElementById("count").textContent = list.length + " of " + RESOURCES.length + " resources shown";
  document.getElementById("cards").innerHTML = list.map((r, i) => {{
    const idx = RESOURCES.indexOf(r);
    if (r.status !== "ready") {{
      return `<article class="card"><span class="badge soon">COMING SOON</span><span class="word">${{esc(r.word)}}</span><h2>${{esc(r.title)}}</h2><p>${{esc(r.description)}}</p></article>`;
    }}
    return `<article class="card"><span class="badge ready">READY</span><span class="word">${{esc(r.word)}}</span><h2>${{esc(r.title)}}</h2><p>${{esc(r.description)}}</p><button class="btn-dark" onclick="toggle(${{idx}})">View resource</button><button class="btn-line" onclick="copyRes(${{idx}}, this)">Copy text</button> <a href="${{esc(r.file)}}">Open file</a><pre id="pre-${{idx}}">${{esc(r.body)}}</pre></article>`;
  }}).join("") || "<p>No match. Try MOTION, COACH, AUDIT, CLAUDE, LEADS, SOLO or TEAM.</p>";
}}
function toggle(i) {{ document.getElementById("pre-" + i).classList.toggle("open"); }}
async function copyRes(i, btn) {{
  const text = RESOURCES[i].body;
  try {{ await navigator.clipboard.writeText(text); btn.textContent = "Copied"; }}
  catch (e) {{
    const ta = document.createElement("textarea"); ta.value = text; document.body.appendChild(ta); ta.select(); document.execCommand("copy"); ta.remove(); btn.textContent = "Copied";
  }}
  setTimeout(() => btn.textContent = "Copy text", 2000);
}}
document.getElementById("search").addEventListener("input", e => render(e.target.value));
render("");
</script>
</body>
</html>
"""
(OUT / "index.html").write_text(html, encoding="utf-8")
print(f"Built {len(entries)} entries, {sum(1 for e in entries if e['status']=='ready')} ready")
for e in manifest:
    print(e["word"], e["status"], e["file"])
