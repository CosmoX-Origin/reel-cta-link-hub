#!/usr/bin/env python3
"""Build the Reel CTA Link Hub from Abhishek's own verified DM/guide files.

Sources are read, never hand-copied, so the hub can never promise a
resource that does not exist. ENGINE is an original Cosmox guide written
for this hub, because no ENGINE checklist file existed.
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
     "Complete setup for creating broadcast-style motion graphics with Claude, plus a working 9:16 starter template (resources/motion-template.html).",
     "",
     "AI Tools", MOTION_SRC, "MOTION.md"),
    ("COACH", "Your Own AI Coach",
     "5-step setup to build your own personal AI coach in Claude Projects.",
     "",
     "AI Tools", DM / "coach-guide-dm.txt", "COACH.md"),
    ("AUDIT", "The Business Audit Prompt",
     "A ruthless prompt that audits a business across 6 areas, finds money leaks, and gives a 30-day fix plan.",
     "",
     "Business", DM / "audit-prompt-dm.txt", "AUDIT.md"),
    ("CLAUDE", "Claude Starter Guide: 60-Minute AI Employee",
     "Starter guide to turn Claude into your AI employee in just 60 minutes.",
     "",
     "AI Tools", None, "CLAUDE.md"),
    ("LEADS", "AI Closer Setup Checklist",
     "Checklist to stop leads dying in the inbox: 60-second reply, Day 1-3-7 follow-up, zero-slip CRM.",
     "",
     "Business", DM / "leads-closer-checklist-dm.txt", "LEADS.md"),
    ("SOLO", "Run a 1-Person Company with AI",
     "Complete guide to running a 1-person company with AI employees, without a team.",
     "",
     "Business", DM / "solo-guide-dm.txt", "SOLO.md"),
    ("TEAM", "Your 35 AI Team Add-ons",
     "35 add-ons for Claude Code, each with its install command.",
     "",
     "AI Tools", DM / "team-35-links-dm.txt", "TEAM.md"),
    ("SYSTEM", "One-Person Company Checklist: 5 Principles",
     "One-person company checklist based on 5 principles, for the SYSTEM word from the SOLO reel.",
     "",
     "Business", HOME / "workspace/content-watch/solo-playbook-dm.txt", "SYSTEM.md"),
    ("NUMBER", "Give Claude Its Own WhatsApp Number",
     "Exact setup to give Claude its own WhatsApp number: virtual number, skills, and messages in 11 lines.",
     "",
     "AI Tools", HOME / "workspace/content-watch/wa-number-dm.txt", "NUMBER.md"),
    ("ENGINE", "Content Machine Setup Checklist",
     "An AI workspace that plans, writes, and publishes content in just 30 minutes a day.",
     "",
     "Content", RES / "ENGINE.md", "ENGINE.md"),
]

entries = []
for word, title, desc, hindi, category, src, fname in SPECS:
    if word == "CLAUDE":
        body = claude_guide()
    else:
        body = read_text(src)
    (RES / fname).write_text(body, encoding="utf-8")
    entries.append({"word": word, "title": title, "description": desc,
                    "hindi": hindi, "category": category,
                    "status": "ready", "file": f"resources/{fname}", "body": body})

examples_data = {}
if (OUT / "examples.json").exists():
    examples_data = json.loads((OUT / "examples.json").read_text(encoding="utf-8"))
keywords_data = {}
if (OUT / "keywords.json").exists():
    keywords_data = json.loads((OUT / "keywords.json").read_text(encoding="utf-8"))
for e in entries:
    e["keywords"] = keywords_data.get("per_resource", {}).get(e["word"], [])
    e["examples"] = examples_data.get(e["word"], [])
site_topics = keywords_data.get("site_topics", [])
meta_kw = ", ".join(site_topics + [k for v in keywords_data.get("per_resource", {}).values() for k in v])

manifest = [{k: v for k, v in e.items() if k not in ("body", "keywords", "examples")} for e in entries]
(OUT / "resources.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

data_json = json.dumps(entries, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Reel CTA Link Hub | Cosmox Origin</title>
<meta name="description" content="One link for every Cosmox Origin reel comment CTA. Search the word from the reel and get the resource instantly, no DM wait.">
<meta name="keywords" content="{meta_kw}">
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
.hindi {{ font-size: 15px; color: #666; }}
.cat {{ display: inline-block; background: #ffe8d6; color: #7a3d00; border-radius: 999px; padding: 4px 10px; font-size: 12px; font-weight: 700; margin-left: 8px; }}
.catbtn {{ background: #fff; color: #111; border: 2px solid #111; margin: 0 6px 8px 0; }}
.catbtn.active {{ background: #111; color: #fff; }}
button {{ cursor: pointer; border: 0; border-radius: 10px; padding: 10px 14px; font-size: 15px; font-weight: 700; }}
.btn-dark {{ background: #111; color: #fff; }}
.btn-line {{ background: #fff; color: #111; border: 2px solid #111; margin-left: 8px; }}
.sections {{ display: none; margin-top: 14px; }}
.sections.open {{ display: block; }}
.sec {{ background: #f4efe4; border-radius: 12px; padding: 12px 14px; margin-bottom: 10px; }}
.sec pre {{ white-space: pre-wrap; word-wrap: break-word; font-size: 14px; line-height: 1.6; margin: 8px 0 0; }}
.sec button {{ font-size: 13px; padding: 6px 10px; }}
body.dark {{ background: #111; color: #eee; }}
body.dark .card, body.dark #search {{ background: #222; color: #eee; border-color: #444; }}
body.dark .card p, body.dark .hindi, body.dark p.lead {{ color: #ccc; }}
body.dark .sec {{ background: #333; }}
body.dark .catbtn {{ background: #222; color: #eee; border-color: #eee; }}
body.dark .catbtn.active {{ background: #ff7a1a; color: #111; border-color: #ff7a1a; }}
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
<button class="btn-line" style="float:right" onclick="toggleDark()" id="darkBtn">Dark mode</button>
<h1>Reel CTA Link Hub</h1>
<p class="lead">Search the exact word from the reel here. You will get the resource instantly, no DM wait. One link for every reel.</p>
</header>
<main>
<input id="search" type="search" placeholder="Search the comment word, e.g. MOTION, COACH, LEADS" autocomplete="off">
<div style="margin-top:12px">
<button class="catbtn active" onclick="setCat('All', this)">All</button>
<button class="catbtn" onclick="setCat('AI Tools', this)">AI Tools</button>
<button class="catbtn" onclick="setCat('Business', this)">Business</button>
<button class="catbtn" onclick="setCat('Content', this)">Content</button>
</div>
<p class="hint" id="count"></p>
<div id="cards"></div>
<section class="how">
<h2>For creators: add a new CTA in 2 minutes</h2>
<ol>
<li>Drop the resource file in <code>resources/</code>, for example <code>resources/NEWWORD.md</code>.</li>
<li>Add one entry to <code>resources.json</code>: word, title, description, status and file.</li>
<li>Rebuild this page or add the entry directly to the index. Keep only this hub's link in the bio, not a separate link for every reel.</li>
</ol>
<p>Rule: if a resource is not ready, keep its status as <code>coming-soon</code>. Never give a fake link.</p>
</section>
</main>
<footer>Built by Cosmox Origin &middot; Follow @cosmox_origin for AI workflows that actually work.<br>Follow Cosmox Origin: <a href="https://www.instagram.com/cosmox_origin">Instagram</a> &middot; <a href="https://www.facebook.com/profile.php?id=324872101219371">Facebook</a> &middot; <a href="https://cosmoxorigin.com">Website</a> &middot; <a href="https://github.com/CosmoX-Origin">GitHub</a><br><a href="INSTALL.md">Installation and usage guide</a> &middot; <a href="README.md">All resources</a></footer>
<script>
const RESOURCES = {data_json};
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
let currentCat = "All";
function sectionsHtml(body) {{
  return body.split(/\\n\\s*\\n/).filter(s => s.trim()).map(s => `<div class="sec"><button class="btn-line" onclick="copySection(this)">Copy section</button><pre>${{esc(s.trim())}}</pre></div>`).join("");
}}
function examplesHtml(exs) {{
  return (exs || []).map(x => `<div class="sec"><button class="btn-line" onclick="copyExample(this)">Copy example</button><strong>${{esc(x.title)}}</strong><pre>${{esc(x.text)}}</pre></div>`).join("");
}}
const TOTAL_EX = RESOURCES.reduce((a, r) => a + (r.examples || []).length, 0);
function render(filter) {{
  const q = (filter || "").trim().toLowerCase();
  const list = RESOURCES.filter(r => (currentCat === "All" || r.category === currentCat) && (!q || r.word.toLowerCase().includes(q) || r.title.toLowerCase().includes(q) || r.description.toLowerCase().includes(q) || (r.hindi || "").includes(q) || (r.keywords || []).join(" ").toLowerCase().includes(q) || (r.examples || []).some(x => (x.title + " " + x.text).toLowerCase().includes(q))));
  document.getElementById("count").textContent = list.length + " of " + RESOURCES.length + " resources shown · " + TOTAL_EX + " examples";
  document.getElementById("cards").innerHTML = list.map((r, i) => {{
    const idx = RESOURCES.indexOf(r);
    if (r.status !== "ready") {{
      return `<article class="card"><span class="badge soon">COMING SOON</span><span class="word">${{esc(r.word)}}</span><span class="cat">${{esc(r.category || "")}}</span><h2>${{esc(r.title)}}</h2><p>${{esc(r.description)}}</p></article>`;
    }}
    return `<article class="card"><span class="badge ready">READY</span><span class="word">${{esc(r.word)}}</span><span class="cat">${{esc(r.category || "")}}</span><h2>${{esc(r.title)}}</h2><p>${{esc(r.description)}}</p><p class="hindi">Keywords: ${{esc((r.keywords || []).join(", "))}}</p><button class="btn-dark" onclick="toggle(${{idx}})">View resource</button><button class="btn-line" onclick="copyRes(${{idx}}, this)">Copy text</button><button class="btn-line" onclick="shareRes(${{idx}}, this)">Share</button><button class="btn-line" onclick="toggleEx(${{idx}})">Examples (${{(r.examples || []).length}})</button> <a href="${{esc(r.file)}}">Open file</a><div class="sections" id="sec-${{idx}}">${{sectionsHtml(r.body)}}</div><div class="sections" id="ex-${{idx}}">${{examplesHtml(r.examples)}}</div></article>`;
  }}).join("") || "<p>No match. Try MOTION, COACH, AUDIT, CLAUDE, LEADS, SOLO, TEAM, SYSTEM, NUMBER or ENGINE.</p>";
}}
function toggle(i) {{ document.getElementById("sec-" + i).classList.toggle("open"); }}
function toggleEx(i) {{ document.getElementById("ex-" + i).classList.toggle("open"); }}
function copyExample(btn) {{ copyText(btn.parentElement.querySelector("pre").textContent, btn, "Copy example"); }}
async function copyText(text, btn, label) {{
  try {{ await navigator.clipboard.writeText(text); btn.textContent = "Copied"; }}
  catch (e) {{
    const ta = document.createElement("textarea"); ta.value = text; document.body.appendChild(ta); ta.select(); document.execCommand("copy"); ta.remove(); btn.textContent = "Copied";
  }}
  setTimeout(() => btn.textContent = label, 2000);
}}
function copyRes(i, btn) {{ copyText(RESOURCES[i].body, btn, "Copy text"); }}
function copySection(btn) {{ copyText(btn.nextElementSibling.textContent, btn, "Copy section"); }}
async function shareRes(i, btn) {{
  const text = "Reel CTA Link Hub - " + RESOURCES[i].word + ": " + RESOURCES[i].title + " https://github.com/CosmoX-Origin/reel-cta-link-hub";
  if (navigator.share) {{ try {{ await navigator.share({{title: "Reel CTA Link Hub", text: text}}); return; }} catch (e) {{}} }}
  copyText(text, btn, "Share");
}}
function setCat(cat, btn) {{
  currentCat = cat;
  document.querySelectorAll(".catbtn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");
  render(document.getElementById("search").value);
}}
function toggleDark() {{
  document.body.classList.toggle("dark");
  const dark = document.body.classList.contains("dark");
  document.getElementById("darkBtn").textContent = dark ? "Light mode" : "Dark mode";
  try {{ localStorage.setItem("cta-dark", dark ? "1" : "0"); }} catch (e) {{}}
}}
try {{ if (localStorage.getItem("cta-dark") === "1") {{ document.body.classList.add("dark"); document.getElementById("darkBtn").textContent = "Light mode"; }} }} catch (e) {{}}
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
