# -*- coding: utf-8 -*-
"""Self-hosts the site's Google Fonts (same families, same weights) for speed.

Latin fonts keep only their `latin` subset. The two Chinese families are
subset to exactly the characters used on the site, via Google's `text=`
parameter, so they weigh a few KB instead of megabytes.

Returns the @font-face CSS to inline in every page <head>.
"""
import hashlib
import re
import urllib.parse
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"

LATIN = [
    "family=Marcellus",
    "family=Marcellus+SC",
    "family=Montserrat:wght@400..600",
]
CJK = [
    "family=Noto+Serif+SC:wght@400;500",
    "family=Noto+Sans+SC:wght@400;500",
]


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def _blocks(css):
    """Yield (subset_comment, block_text) for each @font-face in a Google CSS response."""
    for m in re.finditer(r"(?:/\* (\S+) \*/\s*)?(@font-face\s*{[^}]*})", css):
        yield m.group(1), m.group(2)


def build(site_dir, chars):
    out_dir = Path(site_dir) / "assets" / "fonts"
    out_dir.mkdir(parents=True, exist_ok=True)
    text = "".join(sorted(set(chars)))
    tag = hashlib.md5(text.encode()).hexdigest()[:6]
    rules, preload = [], []

    def localise(block, name):
        url = re.search(r"url\((https://[^)]+)\)", block).group(1)
        dest = out_dir / name
        if not dest.exists():
            dest.write_bytes(_get(url))
        block = block.replace(url, f"__P__assets/fonts/{name}")
        return re.sub(r"font-display:\s*\w+", "font-display: swap", block)

    for fam in LATIN:
        css = _get(f"https://fonts.googleapis.com/css2?{fam}&display=swap").decode()
        for subset, block in _blocks(css):
            if subset not in (None, "latin"):
                continue
            family = re.search(r"font-family: '([^']+)'", block).group(1)
            weight = re.search(r"font-weight: ([\d ]+);", block).group(1).replace(" ", "-")
            name = f"{family.lower().replace(' ', '-')}-{weight}-latin.woff2"
            rules.append(localise(block, name))
            if family in ("Marcellus", "Montserrat"):
                preload.append(name)

    for fam in CJK:
        q = urllib.parse.quote(text)
        css = _get(f"https://fonts.googleapis.com/css2?{fam}&display=swap&text={q}").decode()
        for _, block in _blocks(css):
            family = re.search(r"font-family: '([^']+)'", block).group(1)
            weight = re.search(r"font-weight: (\d+);", block).group(1)
            name = f"{family.lower().replace(' ', '-')}-{weight}-{tag}.woff2"
            rules.append(localise(block, name))

    # drop stale subsets from earlier builds
    keep = {re.search(r"assets/fonts/([^)]+)", r).group(1) for r in rules}
    for f in out_dir.glob("*.woff2"):
        if f.name not in keep:
            f.unlink()
    return "\n".join(rules), preload
