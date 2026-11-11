"""Generate the README's SVG cards (light and dark) from the content below.

Usage:  python scripts/cards.py
Writes: assets/cards/*.svg

Standard library only. Edit the text in CONTENT and re-run; the README
links to the files by name, so it doesn't need to change.
"""

import base64
import os
from html import escape

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "assets", "cards")

THEMES = {
    "dark": dict(bg="#0B1220", border="#1E293B", text="#E2E8F0", muted="#94A3B8",
                 pill="#111A2E", cyan="#22D3EE", teal="#2DD4BF", purple="#A78BFA", blue="#60A5FA"),
    "light": dict(bg="#F8FAFC", border="#E2E8F0", text="#0F172A", muted="#475569",
                  pill="#EEF2F7", cyan="#0891B2", teal="#0D9488", purple="#7C3AED", blue="#2563EB"),
}
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def wrap(text, size, width, bold=False):
    """Greedy word wrap using an average glyph width; deliberately conservative."""
    per = size * (0.56 if bold else 0.52)
    limit = max(1, int(width / per))
    lines, line = [], ""
    for word in text.split():
        test = f"{line} {word}".strip()
        if len(test) <= limit:
            line = test
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def text_block(x, y, lines, size, fill, leading, family=SANS, weight="400"):
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else leading}">{escape(l)}</tspan>' for i, l in enumerate(lines)
    )
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}">{spans}</text>')


def frame(w, h, c, title, body, accent):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="14" fill="{c["bg"]}" stroke="{c["border"]}" stroke-width="1.5"/>'
        f'{body}'
        f'<rect x="1" y="1" width="{w-2}" height="4" rx="2" fill="{c[accent]}" opacity="0.9"/>'
        f'</svg>\n'
    )


def pills(x, y, tags, c, max_x):
    out, cx, cy = [], x, y
    for t in tags:
        w = len(t) * 7.2 + 18
        if cx + w > max_x:
            cx, cy = x, cy + 30
        out.append(f'<rect x="{cx}" y="{cy}" width="{w:.0f}" height="22" rx="11" fill="{c["pill"]}" stroke="{c["border"]}"/>'
                   f'<text x="{cx + w/2:.0f}" y="{cy+15}" text-anchor="middle" font-family="{MONO}" '
                   f'font-size="12" fill="{c["muted"]}">{escape(t)}</text>')
        cx += w + 8
    return "".join(out)


def mark(kind, x, y, col):
    """Small geometric marks for the 'What I do' cards."""
    if kind == "square":
        return f'<rect x="{x}" y="{y}" width="14" height="14" rx="3" fill="none" stroke="{col}" stroke-width="2"/>'
    if kind == "hex":
        pts = " ".join(f"{x+7+8*dx:.1f},{y+7+8*dy:.1f}" for dx, dy in
                       [(0, -1), (0.87, -0.5), (0.87, 0.5), (0, 1), (-0.87, 0.5), (-0.87, -0.5)])
        return f'<polygon points="{pts}" fill="none" stroke="{col}" stroke-width="2"/>'
    if kind == "tri":
        return f'<polygon points="{x+7},{y} {x+15},{y+14} {x-1},{y+14}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>'
    return (f'<circle cx="{x+4}" cy="{y+7}" r="4" fill="none" stroke="{col}" stroke-width="2"/>'
            f'<circle cx="{x+13}" cy="{y+7}" r="4" fill="none" stroke="{col}" stroke-width="2"/>')


# ---------------------------------------------------------------- card types

def focus_card(d, c):
    w, h = 400, 132
    col = c[d["accent"]]
    body = (mark(d["mark"], 26, 28, col)
            + f'<text x="52" y="41" font-family="{SANS}" font-size="19" font-weight="700" fill="{c["text"]}">{escape(d["title"])}</text>'
            + text_block(26, 72, wrap(d["text"], 14.5, w - 52), 14.5, c["muted"], 21))
    return frame(w, h, c, f'{d["title"]}: {d["text"]}', body, d["accent"])


def project_card(d, c):
    w, h = 266, 384
    col = c[d["accent"]]
    desc = wrap(d["text"], 14, w - 44)
    body = (f'<text x="22" y="40" font-family="{MONO}" font-size="12" letter-spacing="1" fill="{col}">{escape(d["kicker"].upper())}</text>'
            + f'<text x="22" y="74" font-family="{SANS}" font-size="24" font-weight="700" fill="{c["text"]}">{escape(d["title"])}</text>'
            + text_block(22, 104, desc, 14, c["muted"], 20)
            + pills(22, 104 + 20 * len(desc) + 6, d["tags"], c, w - 18)
            + f'<line x1="22" y1="{h-52}" x2="{w-22}" y2="{h-52}" stroke="{c["border"]}" stroke-width="1.5"/>'
            + f'<text x="22" y="{h-24}" font-family="{SANS}" font-size="15" font-weight="700" fill="{col}">Live project ↗</text>')
    return frame(w, h, c, f'{d["title"]}: {d["text"]}', body, d["accent"])


def wide_card(d, c):
    """Open source card."""
    w = 400
    col = c[d["accent"]]
    desc = wrap(d["text"], 14, w - 44)
    tags_y = 104 + 20 * len(desc) + 6
    h = tags_y + 22 + 74
    body = (f'<text x="22" y="40" font-family="{MONO}" font-size="12" letter-spacing="1" fill="{col}">{escape(d["kicker"].upper())}</text>'
            + f'<text x="22" y="72" font-family="{SANS}" font-size="21" font-weight="700" fill="{c["text"]}">{escape(d["title"])}</text>'
            + text_block(22, 104, desc, 14, c["muted"], 20)
            + pills(22, tags_y, d["tags"], c, w - 18)
            + f'<line x1="22" y1="{h-52}" x2="{w-22}" y2="{h-52}" stroke="{c["border"]}" stroke-width="1.5"/>'
            + f'<text x="22" y="{h-24}" font-family="{SANS}" font-size="15" font-weight="700" fill="{col}">{escape(d["cta"])} ↗</text>')
    return frame(w, h, c, f'{d["title"]}: {d["text"]}', body, d["accent"])


def video_card(d, c):
    w, h, th = 400, 350, 225
    col = c[d["accent"]]
    with open(os.path.join(ROOT, d["thumb"]), "rb") as f:
        img = base64.b64encode(f.read()).decode()
    body = (f'<defs><clipPath id="thumb"><path d="M1 15 a14 14 0 0 1 14 -14 H{w-15} a14 14 0 0 1 14 14 V{th} H1 Z"/></clipPath></defs>'
            f'<image href="data:image/jpeg;base64,{img}" x="1" y="1" width="{w-2}" height="{th}" '
            f'preserveAspectRatio="xMidYMid slice" clip-path="url(#thumb)"/>'
            f'<circle cx="{w/2}" cy="{th/2}" r="28" fill="#0B1220" fill-opacity="0.72"/>'
            f'<polygon points="{w/2-9},{th/2-13} {w/2-9},{th/2+13} {w/2+14},{th/2}" fill="#FFFFFF"/>'
            f'<rect x="{w-64}" y="{th-34}" width="50" height="22" rx="6" fill="#0B1220" fill-opacity="0.78"/>'
            f'<text x="{w-39}" y="{th-18}" text-anchor="middle" font-family="{MONO}" font-size="12" fill="#FFFFFF">{d["duration"]}</text>'
            f'<text x="22" y="{th+30}" font-family="{MONO}" font-size="12" letter-spacing="1" fill="{col}">{escape(d["kicker"].upper())}</text>'
            + text_block(22, th + 56, wrap(d["title"], 17, w - 44, bold=True), 17, c["text"], 22, weight="700")
            + f'<text x="22" y="{h-22}" font-family="{SANS}" font-size="14" font-weight="700" fill="{col}">Watch video ↗</text>'
            + f'<text x="{w-22}" y="{h-22}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{c["muted"]}">{escape(d["meta"])}</text>')
    return frame(w, h, c, f'Video: {d["title"]}', body, d["accent"])


def article_card(d, c):
    w, h = 400, 128
    col = c[d["accent"]]
    body = (f'<text x="22" y="34" font-family="{MONO}" font-size="12" letter-spacing="1" fill="{col}">{escape(d["kicker"].upper())}</text>'
            + text_block(22, 60, wrap(d["title"], 16, w - 44, bold=True)[:2], 16, c["text"], 21, weight="700")
            + f'<text x="22" y="{h-20}" font-family="{SANS}" font-size="14" font-weight="700" fill="{col}">Read on DEV ↗</text>'
            + f'<text x="{w-22}" y="{h-20}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{c["muted"]}">{escape(d["meta"])}</text>')
    return frame(w, h, c, f'Article: {d["title"]}', body, d["accent"])


# ---------------------------------------------------------------- content

CONTENT = {
    "focus-build": (focus_card, dict(title="Build", mark="square", accent="cyan",
        text="Backend systems, APIs, developer tools, and products that solve real problems.")),
    "focus-blockchain": (focus_card, dict(title="Blockchain", mark="hex", accent="purple",
        text="Building on Solana, exploring smart contracts, payments, and developer infrastructure.")),
    "focus-teach": (focus_card, dict(title="Teach", mark="tri", accent="teal",
        text="Technical articles, tutorials, demos, workshops, and talks that help developers understand and build.")),
    "focus-community": (focus_card, dict(title="Community", mark="rings", accent="blue",
        text="Bringing developers together, sharing opportunities, and helping people grow through technology.")),

    "project-sovra": (project_card, dict(title="Sovra", kicker="personal finance", accent="purple",
        host="sovra-ecru.vercel.app",
        text="A money app that remembers your goals. Budgets, limits and past decisions live in a memory vault on Walrus, so its advice gets more personal over time instead of starting from zero.",
        tags=["TypeScript", "NestJS", "Sui", "Walrus"])),
    "project-stakesync": (project_card, dict(title="StakeSync", kicker="accountability", accent="cyan",
        host="usestakesync.xyz",
        text="Join a challenge, put something on the line, and prove you showed up. Progress is checked against GitHub, LeetCode, Solana activity and more. Running on Solana devnet with credits while in testing.",
        tags=["Solana", "TypeScript", "React"])),
    "project-blockrouter": (project_card, dict(title="BlockRouter", kicker="payments for AI", accent="teal",
        host="blockrouter.netlify.app",
        text="Self-custodial stablecoin payments for AI inference. Lock a USDC budget in an on-chain vault, use any OpenAI-compatible tool, and pay only for the tokens you use. Live on Solana devnet.",
        tags=["Solana", "Anchor", "Rust", "TypeScript"])),

    "oss-dsa": (wide_card, dict(title="DSA Solutions and Patterns", kicker="open source · learning", accent="teal",
        cta="View repository",
        text="Problems grouped by the pattern behind them, from two pointers to backtracking, with step-by-step explanations so you learn the idea and not just the answer. Open to contributions.",
        tags=["Python", "TypeScript", "Go", "Rust"])),

    "video-docker-1": (video_card, dict(title="What Docker is, and why companies use it",
        kicker="Docker series · part 1", accent="cyan", duration="2:22", meta="on X",
        thumb="assets/media/docker-part-1.jpg")),
    "video-docker-2": (video_card, dict(title="Docker, part 2: the concepts most tutorials skip",
        kicker="Docker series · part 2", accent="teal", duration="3:14", meta="on X",
        thumb="assets/media/docker-part-2.jpg")),

    "article-spl-mint": (article_card, dict(kicker="Solana · SPL token series", accent="purple", meta="part 1 of 3",
        title="Building an SPL Token: Creating the Mint")),
    "article-beyond-crud": (article_card, dict(kicker="Backend", accent="cyan", meta="5 min read",
        title="Beyond CRUD: 9 Backend Concepts Every Engineer Should Know")),
    "article-hackathons": (article_card, dict(kicker="Impact · hackathons", accent="teal", meta="3 min read",
        title="The Strategy Behind Winning Hackathons")),
    "article-first-opportunity": (article_card, dict(kicker="Career · community", accent="blue", meta="5 min read",
        title="How to Get Your First Opportunity Without Work Experience")),
    "article-fintech": (article_card, dict(kicker="Backend", accent="cyan", meta="4 min read",
        title="Backend Concepts I Understand Better Because of Fintech")),
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, (fn, data) in CONTENT.items():
        for theme, colors in THEMES.items():
            with open(os.path.join(OUT, f"{name}-{theme}.svg"), "w", encoding="utf-8") as f:
                f.write(fn(data, colors))
    print(f"wrote {len(CONTENT) * len(THEMES)} cards to {os.path.relpath(OUT, ROOT)}/")


if __name__ == "__main__":
    main()
