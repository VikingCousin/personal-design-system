#!/usr/bin/env python3
"""
PDS Brand-Kit-Generator · Core 1.1.0

Erzeugt aus EINER Quelle (brand-kit.json + Token-Dateien eines Projekts):
  dist/brand.css            CSS-Variablen aus den Tokens (minimaler CSS-Adapter)
  dist/BRAND-KIT.html       visuelles Brand Portal
  dist/BRAND-KIT.pdf        Druckfassung derselben HTML-Datei (A4)
  dist/channels/*           Kanal-Ausgaben aus den Core-Startern (HTML + PNG/PDF)
  dist/QA-REPORT.md         Prüfbericht

Aufruf (aus dem Repository-Wurzelverzeichnis):
  python3 core/brand-kit/generator/build_brand_kit.py projects/<name>/brand-kit/brand-kit.json
Optionen: --no-export (ohne PDF/PNG), --chrome <pfad>

Nur Python-Standardbibliothek. PDF/PNG brauchen Chrome oder Chromium (headless).
Exit-Code 0 = keine Fehler, 1 = QA-Fehler (Ausgaben werden trotzdem erzeugt und markiert).
"""
import argparse
import datetime
import html
import json
import math
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

GEN_VERSION = "1.1.0"
HERE = Path(__file__).resolve().parent
CORE = HERE.parent.parent
CONTRACT = CORE / "tokens" / "contract.tokens.json"
STARTERS = HERE / "starters"

ITEM_STATUS = {"OPEN", "ARBEITSFREIGABE", "ENTSCHIEDEN"}
KIT_STATUS = {"ENTWURF", "FREIGEGEBEN"}
LABEL = {"OPEN": "OFFEN", "ARBEITSFREIGABE": "Arbeitsfreigabe", "ENTSCHIEDEN": "Freigegeben"}
REQUIRED_SECTIONS = ["identity", "logos", "colors", "typography", "layout", "imagery", "voice", "ui", "do_dont", "channels"]
CHANNELS = {
    # Kanal: (Starter-Datei, Export-Art)
    "website": ("website.html", "html"),
    "instagram_post": ("instagram-post.html", "png"),
    "instagram_story": ("instagram-story.html", "png"),
    "pinterest_pin": ("pinterest-pin.html", "png"),
    "linkedin_post": ("linkedin-post.html", "png"),
    "linkedin_carousel": ("linkedin-carousel.html", "pdf"),
    "newsletter": ("newsletter.html", "html"),
    "presentation": ("presentation.html", "pdf"),
    "document": ("document-offer.html", "pdf"),
}
CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome",
]


# ───────────────────────── Bericht ─────────────────────────
class Report:
    def __init__(self):
        self.errors, self.warnings, self.passed, self.open_items = [], [], [], []

    def err(self, msg): self.errors.append(msg)
    def warn(self, msg): self.warnings.append(msg)
    def ok(self, msg): self.passed.append(msg)
    def open(self, where, what): self.open_items.append((where, what))


# ───────────────────────── Tokens ─────────────────────────
def deep_merge(a, b):
    for k, v in b.items():
        if isinstance(v, dict) and isinstance(a.get(k), dict):
            deep_merge(a[k], v)
        else:
            a[k] = v
    return a


def flatten(tree, prefix="", inherited_type=None, out=None):
    out = {} if out is None else out
    t = tree.get("$type", inherited_type) if isinstance(tree, dict) else inherited_type
    for k, v in tree.items():
        if k.startswith("$") or not isinstance(v, dict):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if "$value" in v:
            out[path] = {"value": v["$value"], "type": v.get("$type", t), "ext": v.get("$extensions", {})}
        else:
            flatten(v, path, v.get("$type", t), out)
    return out


REF = re.compile(r"^\{([^}]+)\}$")


def resolve(path, flat, seen=None):
    seen = seen or set()
    if path in seen:
        raise ValueError(f"Zirkulärer Verweis bei {path}")
    if path not in flat:
        raise KeyError(path)
    seen.add(path)
    val = flat[path]["value"]

    def res(v):
        if isinstance(v, str) and REF.match(v):
            return resolve(REF.match(v).group(1), flat, set(seen))
        if isinstance(v, dict):
            return {k: res(x) for k, x in v.items()}
        if isinstance(v, list):
            return [res(x) for x in v]
        return v
    return res(val)


def contract_required():
    req, opt = [], []

    def walk(node, prefix=""):
        for k, v in node.items():
            if k.startswith("$") or not isinstance(v, dict):
                continue
            p = f"{prefix}.{k}" if prefix else k
            if "$type" in v and not any(isinstance(x, dict) and not kk.startswith("$") for kk, x in v.items()):
                (req if v.get("$extensions", {}).get("pds", {}).get("required") else opt).append(p)
            else:
                walk(v, p)
    walk(json.loads(CONTRACT.read_text(encoding="utf-8")))
    return req, opt


# ───────────────────────── Farbe ─────────────────────────
HEX = re.compile(r"^#([0-9a-fA-F]{6})$")


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(h):
    r, g, b = (_lin(c) for c in hex_rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def oklch(h):
    r, g, b = (_lin(c) for c in hex_rgb(h))
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (x ** (1 / 3) for x in (l, m, s))
    L = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    A = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    B = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    C = math.hypot(A, B)
    H = math.degrees(math.atan2(B, A)) % 360 if C > 1e-4 else 0
    return f"oklch({L:.3f} {C:.3f} {H:.1f})"


# ───────────────────────── Hilfen ─────────────────────────
def esc(x):
    return html.escape(str(x), quote=True)


def get_path(obj, dotted):
    cur = obj
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        elif isinstance(cur, list) and part.isdigit() and int(part) < len(cur):
            cur = cur[int(part)]
        else:
            return None
    return cur


def css_var(path):
    return "--" + path.replace(".", "-")


DEMO = False  # wird in main() gesetzt; Demo-Kits zeigen nie eine reale Freigabe


def badge(status):
    s = status if status in ITEM_STATUS else "OPEN"
    suffix = " (Demo)" if DEMO and s == "ENTSCHIEDEN" else ""
    return f'<span class="st st-{s.lower()}">{LABEL[s]}{suffix}</span>'


def find_chrome(explicit):
    for c in ([explicit] if explicit else []) + [os.environ.get("CHROME_PATH", "")] + CHROME_CANDIDATES:
        if not c:
            continue
        p = shutil.which(c) or (c if Path(c).exists() else None)
        if p:
            return p
    return None


def chrome(chrome_bin, args):
    base = [chrome_bin, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--hide-scrollbars",
            "--virtual-time-budget=8000", "--no-first-run", "--no-default-browser-check"]
    try:
        return subprocess.run(base + args, capture_output=True, text=True, timeout=90)
    except subprocess.TimeoutExpired as e:
        return subprocess.CompletedProcess(e.cmd, 124, "", "Zeitüberschreitung (90 s)")


def chrome_export(chrome_bin, args, out):
    """Export mit einem zweiten Versuch (z. B. wenn eine andere Chrome-Instanz stört)."""
    r = None
    for _ in range(2):
        r = chrome(chrome_bin, args)
        if Path(out).exists() and Path(out).stat().st_size > 0:
            return r
    return r


def pdf_local_paths(path):
    """Zählt file://-Links und absolute lokale Pfade in einem PDF (roh und in entpackten Streams)."""
    import zlib
    data = Path(path).read_bytes()
    blobs = [data]
    for m in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", data, re.S):
        try:
            blobs.append(zlib.decompress(m.group(1)))
        except Exception:
            pass
    rx = re.compile(rb"file://|/Users/|/home/|[A-Z]:\\\\Users")
    return sum(len(rx.findall(b)) for b in blobs)


def pdf_pages(path):
    data = Path(path).read_bytes()
    return len(re.findall(rb"/Type\s*/Page[^s]", data))


# ───────────────────────── Validierung ─────────────────────────
def validate(kit, kit_dir, flat, rep):
    meta = kit.get("meta", {})
    for k in ("project", "name", "version", "status", "core_version", "updated"):
        if not meta.get(k):
            rep.err(f"meta.{k} fehlt")
    if meta.get("status") not in KIT_STATUS:
        rep.err(f"meta.status muss ENTWURF oder FREIGEGEBEN sein, ist {meta.get('status')!r}")
    if not isinstance(meta.get("demo", False), bool):
        rep.err("meta.demo muss true oder false sein")

    for sec in REQUIRED_SECTIONS:
        if sec not in kit:
            rep.err(f"Abschnitt '{sec}' fehlt")

    # Status aller Abschnitte und Einträge
    def check_status(where, node):
        st = node.get("status") if isinstance(node, dict) else None
        if st not in ITEM_STATUS:
            rep.err(f"{where}: Status fehlt oder ungültig ({st!r}); erlaubt: OPEN, ARBEITSFREIGABE, ENTSCHIEDEN")
            return "OPEN"
        if st != "ENTSCHIEDEN":
            rep.open(where, LABEL[st])
        return st

    statuses = []
    for sec in ("identity", "typography", "layout", "voice", "ui"):
        if isinstance(kit.get(sec), dict):
            statuses.append(check_status(sec, kit[sec]))
    for sec in ("photography", "icons", "illustration"):
        node = get_path(kit, f"imagery.{sec}")
        if isinstance(node, dict):
            statuses.append(check_status(f"imagery.{sec}", node))
    for i, item in enumerate(kit.get("logos", [])):
        statuses.append(check_status(f"logos.{item.get('id', i)}", item))
    for i, item in enumerate(kit.get("colors", [])):
        statuses.append(check_status(f"colors.{item.get('token', i)}", item))
    for i, item in enumerate(kit.get("do_dont", [])):
        statuses.append(check_status(f"do_dont.{i}", item))
    for i, fam in enumerate(get_path(kit, "typography.families") or []):
        statuses.append(check_status(f"typography.families.{fam.get('token', i)}", fam))
        if fam.get("license_status") not in ITEM_STATUS:
            rep.err(f"typography.families.{fam.get('token', i)}: license_status fehlt")
        elif fam["license_status"] != "ENTSCHIEDEN":
            rep.open(f"Lizenz {fam.get('name', '?')}", LABEL[fam["license_status"]])
            statuses.append("OPEN")
    for ch, node in (kit.get("channels") or {}).items():
        if ch not in CHANNELS:
            rep.err(f"channels.{ch}: unbekannter Kanal; erlaubt: {', '.join(CHANNELS)}")
            continue
        statuses.append(check_status(f"channels.{ch}", node))

    # Freigabe nur ohne offene Punkte
    if meta.get("status") == "FREIGEGEBEN":
        if any(s != "ENTSCHIEDEN" for s in statuses):
            rep.err("Kit ist als FREIGEGEBEN markiert, enthält aber Punkte, die nicht ENTSCHIEDEN sind. Freigabe ist so nicht zulässig.")
        if not meta.get("approved_by") or not meta.get("approved_at"):
            rep.err("FREIGEGEBEN ohne meta.approved_by / meta.approved_at")
        if meta.get("demo"):
            rep.err("Ein Demo-Kit darf nie FREIGEGEBEN sein")

    # Token-Vertrag
    req, _ = contract_required()
    missing = [p for p in req if p not in flat]
    if missing:
        (rep.err if meta.get("status") == "FREIGEGEBEN" else rep.warn)(
            f"{len(missing)} Pflicht-Tokens fehlen: {', '.join(missing[:12])}{' …' if len(missing) > 12 else ''}")
    else:
        rep.ok(f"Token-Vertrag vollständig ({len(req)} Pflicht-Tokens)")
    unresolved = []
    for p in flat:
        try:
            resolve(p, flat)
        except (KeyError, ValueError) as e:
            unresolved.append(f"{p} → {e}")
    if unresolved:
        rep.err(f"Nicht auflösbare Token-Verweise: {'; '.join(unresolved[:8])}")
    else:
        rep.ok(f"Alle {len(flat)} Tokens auflösbar")

    # Farben
    for c in kit.get("colors", []):
        t = c.get("token")
        if t not in flat:
            rep.err(f"colors: Token {t} existiert nicht in den Token-Dateien")
            continue
        v = resolve(t, flat)
        if not (isinstance(v, str) and HEX.match(v)):
            rep.err(f"colors: {t} ist keine HEX-Farbe ({v!r})")
    # Kontraste
    fails = 0
    for pair in kit.get("contrast_pairs", []):
        try:
            fg, bg = resolve(pair["fg"], flat), resolve(pair["bg"], flat)
            ratio = contrast(fg, bg)
            pair["_ratio"] = ratio
            if ratio + 1e-9 < pair.get("min", 4.5):
                fails += 1
                rep.err(f"Kontrast {pair['fg']} auf {pair['bg']}: {ratio:.2f}:1 < {pair.get('min', 4.5)}:1")
        except KeyError as e:
            rep.err(f"Kontrastpaar mit unbekanntem Token {e}")
    if kit.get("contrast_pairs") and not fails:
        rep.ok(f"Alle {len(kit['contrast_pairs'])} Kontrastpaare bestanden")
    if not kit.get("contrast_pairs"):
        rep.warn("Keine Kontrastpaare definiert")

    # Typografie
    for fam in get_path(kit, "typography.families") or []:
        if fam.get("token") not in flat:
            rep.err(f"typography: {fam.get('token')} existiert nicht in den Token-Dateien")
    for s in get_path(kit, "typography.styles") or []:
        if s not in flat:
            rep.err(f"typography.styles: {s} existiert nicht")

    # Logos und Assets
    for lg in kit.get("logos", []):
        f = lg.get("file")
        exists = bool(f) and (kit_dir / f).exists()
        lg["_exists"] = exists
        if not exists:
            if lg.get("status") == "ENTSCHIEDEN":
                rep.err(f"Logo {lg.get('id')}: als freigegeben markiert, Datei fehlt ({f})")
            else:
                rep.open(f"Logo-Datei {lg.get('id')}", "fehlt")
    if not any(lg.get("status") == "ENTSCHIEDEN" for lg in kit.get("logos", [])):
        rep.warn("Kein freigegebenes Logo vorhanden")


# ───────────────────────── brand.css ─────────────────────────
def build_css(flat, flat_dark, kit):
    lines = ["/* Erzeugt vom PDS Brand-Kit-Generator aus den Token-Dateien. Nicht von Hand bearbeiten. */"]
    for fam in get_path(kit, "typography.families") or []:
        if fam.get("css_url"):
            lines.append(f'@import url("{fam["css_url"]}");')
    lines.append(":root {")
    composites = {}
    for p in sorted(flat):
        v = resolve(p, flat)
        if isinstance(v, dict):
            composites[p] = v
            continue
        if isinstance(v, list):
            v = f"cubic-bezier({', '.join(str(x) for x in v)})" if len(v) == 4 else ", ".join(map(str, v))
        lines.append(f"  {css_var(p)}: {v};")
    lines.append("}")
    if flat_dark:
        lines.append('[data-theme="dark"] {')
        for p in sorted(flat_dark):
            v = resolve(p, {**flat, **flat_dark})
            if not isinstance(v, (dict, list)):
                lines.append(f"  {css_var(p)}: {v};")
        lines.append("}")
    for p, v in composites.items():
        props = {"fontFamily": "font-family", "fontSize": "font-size", "fontWeight": "font-weight",
                 "lineHeight": "line-height", "letterSpacing": "letter-spacing"}
        body = " ".join(f"{props[k]}: {x};" for k, x in v.items() if k in props)
        lines.append(f".pds-{p.replace('.', '-')} {{ {body} }}")
    return "\n".join(lines) + "\n"


# ───────────────────────── Platzhalter ─────────────────────────
PH = re.compile(r"\{\{\s*([a-z_]+):?([^}]*)\}\}")


def fill(template, kit, kit_dir, flat, rep, where, rel_to_dist):
    def logo_tag(key, cls="logo"):
        lg = next((l for l in kit.get("logos", []) if l.get("id") == key or l.get("variant") == key), None)
        if not lg or not lg.get("_exists"):
            rep.open(f"{where}: Logo '{key}'", "fehlt")
            return f'<span class="pds-open">[OFFEN: Logo {esc(key)}]</span>'
        if lg.get("status") != "ENTSCHIEDEN":
            rep.open(f"{where}: Logo '{key}'", LABEL.get(lg.get("status"), "OFFEN"))
        return f'<img class="{cls}" src="{esc(rel_to_dist)}assets/{esc(Path(lg["file"]).name)}" alt="{esc(lg.get("alt", kit["meta"]["name"]))}">'

    def sub(m):
        kind, arg = m.group(1), m.group(2).strip()
        if kind == "kit":
            v = get_path(kit, arg)
            if v in (None, "", []):
                rep.open(f"{where}: {arg}", "Inhalt fehlt")
                return f'<span class="pds-open">[OFFEN: {esc(arg)}]</span>'
            return esc(v)
        if kind == "token":
            try:
                v = resolve(arg, flat)
            except KeyError:
                rep.err(f"{where}: unbekanntes Token {arg}")
                return "inherit"
            if isinstance(v, (dict, list)):
                return ""
            # einfache Anführungszeichen: gültig in style-Attributen und in <style>-Blöcken
            return html.escape(str(v), quote=False).replace('"', "'")
        if kind == "opt":
            v = get_path(kit, arg)
            return esc(v) if v not in (None, "", []) else ""
        if kind == "logo":
            return logo_tag(arg or "primary")
        if kind == "css":
            return f'<link rel="stylesheet" href="{esc(rel_to_dist)}brand.css">'
        if kind == "demo_banner":
            return ('<div class="pds-demo-banner">DEMO · fiktive Beispielmarke · keine reale, freigegebene Marke</div>'
                    if kit["meta"].get("demo") else "")
        if kind == "kit_status":
            return esc(kit["meta"]["status"]) + (" · DEMO" if kit["meta"].get("demo") else "")
        rep.err(f"{where}: unbekannter Platzhalter {m.group(0)}")
        return ""
    return PH.sub(sub, template)


# ───────────────────────── Brand-Kit-HTML ─────────────────────────
PORTAL_CSS = """
:root{--c-ink:#16181d;--c-ink-2:#4f5561;--c-line:#dfe2e7;--c-soft:#f5f6f8;--c-bg:#fff;--c-open:#8a4b00;--c-open-bg:#fff4e0;--c-ok:#1f6b3a;--c-ok-bg:#e7f5ec;--c-wip:#3c4fb0;--c-wip-bg:#eceffd}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--c-bg);color:var(--c-ink);font:16px/1.55 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif}
a{color:inherit}:focus-visible{outline:3px solid var(--c-wip);outline-offset:2px}
.skip{position:absolute;left:-9999px}.skip:focus{left:16px;top:16px;background:#fff;padding:8px 12px;z-index:10}
.layout{display:grid;grid-template-columns:240px minmax(0,1fr);min-height:100vh}
nav.side{position:sticky;top:0;height:100vh;overflow:auto;border-right:1px solid var(--c-line);padding:28px 20px;background:var(--c-soft)}
nav.side .kit{font-weight:700;margin:0 0 4px}nav.side .ver{font-size:13px;color:var(--c-ink-2);margin:0 0 20px}
nav.side ul{list-style:none;margin:0;padding:0}nav.side li a{display:block;padding:7px 10px;border-radius:6px;text-decoration:none;font-size:15px}
nav.side li a:hover{background:#e9ebef}
main{padding:40px clamp(16px,4vw,56px) 80px;max-width:1100px;min-width:0}
code{overflow-wrap:anywhere}.card{min-width:0}
section{padding:32px 0;border-top:1px solid var(--c-line)}section:first-of-type{border-top:0}
h1{font-size:34px;line-height:1.1;margin:0 0 8px}h2{font-size:24px;margin:0 0 16px}h3{font-size:17px;margin:20px 0 8px}
.muted{color:var(--c-ink-2)}.small{font-size:14px}
.st{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.04em;padding:2px 8px;border-radius:999px;vertical-align:middle;border:1px solid}
.st-open{color:var(--c-open);background:var(--c-open-bg);border-color:#e7b56a}.st-open::before{content:"○ "}
.st-arbeitsfreigabe{color:var(--c-wip);background:var(--c-wip-bg);border-color:#aab5ef}.st-arbeitsfreigabe::before{content:"◐ "}
.st-entschieden{color:var(--c-ok);background:var(--c-ok-bg);border-color:#9bd0ad}.st-entschieden::before{content:"● "}
.statusbar{display:flex;flex-wrap:wrap;gap:12px;align-items:center;padding:14px 16px;border-radius:10px;background:var(--c-soft);margin:16px 0}
.statusbar.draft{background:var(--c-open-bg)}.statusbar.fail{background:#fde8e8}
.pds-demo-banner{background:#16181d;color:#fff;font-weight:700;letter-spacing:.06em;text-align:center;padding:10px 16px;font-size:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,220px),1fr));gap:16px}
.card{border:1px solid var(--c-line);border-radius:10px;padding:16px;background:#fff}
.swatch{height:96px;border-radius:8px;border:1px solid rgba(0,0,0,.08);margin-bottom:12px}
.codes{font:13px/1.6 ui-monospace,Menlo,monospace;display:grid;grid-template-columns:auto 1fr auto;gap:2px 8px;align-items:center}
.copy{font:12px -apple-system,sans-serif;border:1px solid var(--c-line);background:#fff;border-radius:6px;padding:4px 8px;min-height:28px;cursor:pointer}
table{border-collapse:collapse;width:100%;font-size:15px}td code{font-size:13px}th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--c-line);vertical-align:top}
th{font-size:13px;color:var(--c-ink-2);font-weight:600}
.logo-tile{display:flex;align-items:center;justify-content:center;height:140px;border-radius:8px;padding:16px;margin-bottom:10px}
.logo-tile img{max-width:100%;max-height:100%}
.pds-open{display:inline-block;color:var(--c-open);background:var(--c-open-bg);border:1px dashed #d69a45;border-radius:6px;padding:2px 8px;font-size:13px}
.specimen{border-bottom:1px solid var(--c-line);padding:14px 0}.specimen .meta{font:12px ui-monospace,Menlo,monospace;color:var(--c-ink-2)}
.space-bar{height:14px;background:var(--color-brand-primary,#888);border-radius:3px}
.dodont{display:grid;grid-template-columns:1fr 1fr;gap:12px}.do,.dont{border-radius:8px;padding:12px 14px}
.do{background:var(--c-ok-bg)}.do::before{content:"✓ Do · ";font-weight:700}.dont{background:#fde8e8}.dont::before{content:"✕ Don't · ";font-weight:700}
.thumb{width:100%;border:1px solid var(--c-line);border-radius:8px;background:var(--c-soft)}
.ui-row{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:8px 0 16px}
footer{font-size:13px;color:var(--c-ink-2);border-top:1px solid var(--c-line);padding-top:16px;margin-top:24px}
@media (max-width:860px){.layout{grid-template-columns:minmax(0,1fr)}table{display:block;overflow-x:auto}nav.side{position:static;height:auto;border-right:0;border-bottom:1px solid var(--c-line)}
 nav.side ul{display:flex;flex-wrap:wrap;gap:4px}.dodont{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@page{size:A4;margin:16mm 14mm}
@media print{nav.side,.copy,.skip{display:none!important}.layout{display:block}main{padding:0;max-width:none}
 section{break-before:page;border-top:0;padding-top:0}section:first-of-type{break-before:auto}
 .card,.specimen,tr,.dodont>div{break-inside:avoid}body{font-size:11pt}a{text-decoration:none}
 .codes{grid-template-columns:auto 1fr}td code,th code{font-size:9pt}
 body.is-demo section:first-of-type::before{display:none}
 body.is-demo section::before{content:"DEMO · fiktive Beispielmarke · keine reale, freigegebene Marke";display:block;font-size:8pt;font-weight:700;letter-spacing:.04em;color:var(--c-ink-2);border-bottom:1px solid var(--c-line);padding-bottom:2mm;margin-bottom:5mm}}
"""


def build_html(kit, kit_dir, flat, rep, qa_failed, channel_files):
    m = kit["meta"]
    fams = get_path(kit, "typography.families") or []
    out = []
    add = out.append
    nav = [("overview", "Übersicht"), ("identity", "Identität"), ("logos", "Logos"), ("colors", "Farben"),
           ("type", "Typografie"), ("layout", "Layout & Formen"), ("imagery", "Bildsprache & Icons"),
           ("voice", "Tonalität"), ("dodont", "Do & Don't"), ("ui", "UI-Elemente"), ("channels", "Kanäle"),
           ("open", "Offene Punkte")]
    add(f"""<!doctype html><html lang="{esc(m.get('language', 'de'))}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="generator" content="PDS Brand-Kit-Generator {GEN_VERSION}">
<title>Brand Kit · {esc(m['name'])} · v{esc(m['version'])}</title>
<link rel="stylesheet" href="brand.css"><style>{PORTAL_CSS}</style></head><body{' class="is-demo"' if m.get("demo") else ''}>
<a class="skip" href="#main">Zum Inhalt springen</a>""")
    if m.get("demo"):
        add('<div class="pds-demo-banner" role="note">DEMO · fiktive Beispielmarke · keine reale, freigegebene Marke</div>')
    add('<div class="layout"><nav class="side" aria-label="Brand-Kit-Navigation">')
    add(f'<p class="kit">{esc(m["name"])}</p><p class="ver">Brand Kit v{esc(m["version"])} · {esc(m["status"])}</p><ul>')
    for anchor, label in nav:
        add(f'<li><a href="#{anchor}">{label}</a></li>')
    add('</ul></nav><main id="main">')

    # Übersicht
    cls = "fail" if qa_failed else ("draft" if m["status"] != "FREIGEGEBEN" else "")
    add(f'<section id="overview"><p class="muted small">Brand Kit · erzeugt aus <code>brand-kit.json</code> und den Token-Dateien</p>'
        f'<h1>{esc(m["name"])}</h1><p class="muted">{esc(get_path(kit, "identity.one_liner") or "")}</p>'
        f'<div class="statusbar {cls}"><strong>Status: {esc(m["status"])}</strong>'
        f'<span>Version {esc(m["version"])}</span><span>Stand {esc(m["updated"])}</span>'
        f'<span>Core {esc(m["core_version"])}</span>'
        + (f'<span>Freigegeben von {esc(m.get("approved_by"))} am {esc(m.get("approved_at"))}</span>' if m["status"] == "FREIGEGEBEN" else
           f'<span>{len(rep.open_items)} offene Punkte, siehe <a href="#open">Offene Punkte</a></span>')
        + ('<span><strong>QA fehlgeschlagen</strong> (siehe QA-REPORT.md)</span>' if qa_failed else "")
        + '</div><p class="small muted">Legende: ' + badge("ENTSCHIEDEN") + " " + badge("ARBEITSFREIGABE") + " " + badge("OPEN")
        + ' · Nur als „Freigegeben“ markierte Inhalte dürfen in Produktion verwendet werden.</p></section>')

    # Identität
    idn = kit.get("identity", {})
    add(f'<section id="identity"><h2>Identität {badge(idn.get("status"))}</h2>')
    if idn.get("positioning"):
        add(f'<p>{esc(idn["positioning"])}</p>')
    if idn.get("values"):
        add('<h3>Markenwerte</h3><div class="grid">' + "".join(
            f'<div class="card"><strong>{esc(v.get("name", ""))}</strong><p class="small muted">{esc(v.get("description", ""))}</p></div>'
            for v in idn["values"]) + "</div>")
    pers = idn.get("personality", {})
    if pers:
        add('<h3>Persönlichkeit</h3><div class="dodont"><div class="do">' + esc(" · ".join(pers.get("is", []))) +
            '</div><div class="dont">' + esc(" · ".join(pers.get("is_not", []))) + "</div></div>")
    if idn.get("source"):
        add(f'<p class="small muted">Quelle: {esc(idn["source"])}</p>')
    add("</section>")

    # Logos
    add('<section id="logos"><h2>Logos</h2><div class="grid">')
    for lg in kit.get("logos", []):
        bg = "#16181d" if lg.get("background") == "dark" else "#f5f6f8"
        img = (f'<img src="assets/{esc(Path(lg["file"]).name)}" alt="{esc(lg.get("alt", lg.get("name", "")))}">'
               if lg.get("_exists") else f'<span class="pds-open">[OFFEN: Datei fehlt]</span>')
        ms = lg.get("min_size", {})
        add(f'<div class="card"><div class="logo-tile" style="background:{bg}">{img}</div>'
            f'<strong>{esc(lg.get("name", lg.get("id")))}</strong> {badge(lg.get("status"))}'
            f'<p class="small muted">Variante: {esc(lg.get("variant", "—"))} · Hintergrund: {esc(lg.get("background", "—"))}<br>'
            f'Mindestgröße: {esc(ms.get("digital_px", "—"))} px / {esc(ms.get("print_mm", "—"))} mm<br>'
            f'Schutzraum: {esc(lg.get("clear_space", "—"))}<br>Datei: <code>{esc(Path(lg["file"]).name if lg.get("file") else "—")}</code></p></div>')
    add("</div></section>")

    # Farben
    add('<section id="colors"><h2>Farben</h2><div class="grid">')
    for c in kit.get("colors", []):
        try:
            v = resolve(c["token"], flat)
        except KeyError:
            continue
        r, g, b = hex_rgb(v)
        pr = c.get("print") or {}
        codes = [("HEX", v), ("RGB", f"{r}, {g}, {b}"), ("OKLCH", oklch(v))] + [(k.upper(), x) for k, x in pr.items() if x]
        rows = "".join(f'<span>{k}</span><span>{esc(x)}</span><button class="copy" type="button" data-copy="{esc(x)}" aria-label="{k} {esc(x)} kopieren">Kopieren</button>' for k, x in codes)
        add(f'<div class="card"><div class="swatch" style="background:{v}"></div><strong>{esc(c.get("name", c["token"]))}</strong> {badge(c.get("status"))}'
            f'<p class="small muted"><code>{esc(c["token"])}</code><br>Rolle: {esc(c.get("role", "—"))}<br>{esc(c.get("usage", ""))}</p>'
            f'<div class="codes">{rows}</div>' + ('<p class="small muted">Druckwerte sind Näherungen und am Muster zu prüfen.</p>' if pr else "") + "</div>")
    add("</div>")
    if kit.get("contrast_pairs"):
        add('<h3>Kontrastpaare (WCAG)</h3><table><thead><tr><th>Text / Element</th><th>Hintergrund</th><th>Verhältnis</th><th>Soll</th><th>Ergebnis</th></tr></thead><tbody>')
        for p in kit["contrast_pairs"]:
            ratio = p.get("_ratio")
            okp = ratio is not None and ratio + 1e-9 >= p.get("min", 4.5)
            try:
                fg, bg = resolve(p["fg"], flat), resolve(p["bg"], flat)
                sample = f'<span style="color:{fg};background:{bg};padding:2px 8px;border-radius:4px">Aa</span> '
            except KeyError:
                sample = ""
            add(f'<tr><td>{sample}<code>{esc(p["fg"])}</code></td><td><code>{esc(p["bg"])}</code></td>'
                f'<td>{f"{ratio:.2f}:1" if ratio else "—"}</td><td>{p.get("min", 4.5)}:1</td><td>{"✓ bestanden" if okp else "✕ nicht bestanden"}</td></tr>')
        add("</tbody></table>")
    add("</section>")

    # Typografie
    typ = kit.get("typography", {})
    add(f'<section id="type"><h2>Typografie {badge(typ.get("status"))}</h2><table><thead><tr><th>Rolle</th><th>Schrift</th><th>Fallback</th><th>Lizenz</th></tr></thead><tbody>')
    for f in fams:
        add(f'<tr><td><code>{esc(f.get("token"))}</code></td><td>{esc(f.get("name"))} {badge(f.get("status"))}</td><td>{esc(f.get("fallback", "—"))}</td>'
            f'<td>{esc(f.get("license", "—"))} {badge(f.get("license_status"))}</td></tr>')
    add("</tbody></table><h3>Hierarchie</h3>")
    for s in typ.get("styles", []):
        try:
            v = resolve(s, flat)
        except KeyError:
            continue
        meta = " · ".join(str(v.get(k)) for k in ("fontSize", "lineHeight", "fontWeight") if isinstance(v, dict) and v.get(k))
        add(f'<div class="specimen"><div class="meta">{esc(s)} · {esc(meta)}</div><div class="pds-{s.replace(".", "-")}">{esc(typ.get("sample_text", "Beispieltext"))}</div></div>')
    add("</section>")

    # Layout
    lay = kit.get("layout", {})
    add(f'<section id="layout"><h2>Layout & Formen {badge(lay.get("status"))}</h2><p>{esc(lay.get("notes", ""))}</p><h3>Abstände</h3>')
    for t in lay.get("spacing_tokens", []):
        if t in flat:
            v = resolve(t, flat)
            add(f'<div class="specimen"><div class="meta">{esc(t)} · {esc(v)}</div><div class="space-bar" style="width:{esc(v)}"></div></div>')
    add('<h3>Radien</h3><div class="ui-row">')
    for t in lay.get("radius_tokens", []):
        if t in flat:
            v = resolve(t, flat)
            add(f'<div style="width:96px;height:64px;border:2px solid var(--color-border-strong,#888);border-radius:{esc(v)}" title="{esc(t)}"></div><span class="small"><code>{esc(t)}</code> {esc(v)}</span>')
    add("</div></section>")

    # Bildsprache
    add('<section id="imagery"><h2>Bildsprache & Icons</h2>')
    for key, label in (("photography", "Fotografie"), ("icons", "Icons"), ("illustration", "Illustration")):
        node = get_path(kit, f"imagery.{key}")
        if not node:
            continue
        add(f'<h3>{label} {badge(node.get("status"))}</h3><p>{esc(node.get("description", ""))}</p>')
        if node.get("do") or node.get("dont"):
            add('<div class="dodont"><div class="do">' + esc(" · ".join(node.get("do", []))) + '</div><div class="dont">' + esc(" · ".join(node.get("dont", []))) + "</div></div>")
    add("</section>")

    # Voice
    vo = kit.get("voice", {})
    add(f'<section id="voice"><h2>Tonalität {badge(vo.get("status"))}</h2><p>{esc(vo.get("summary", ""))}</p>')
    if vo.get("address_rule"):
        add(f'<p><strong>Anrede:</strong> {esc(vo["address_rule"])}</p>')
    if vo.get("principles"):
        add("<ul>" + "".join(f"<li>{esc(p)}</li>" for p in vo["principles"]) + "</ul>")
    if vo.get("words_use") or vo.get("words_avoid"):
        add('<div class="dodont"><div class="do">' + esc(", ".join(vo.get("words_use", []))) + '</div><div class="dont">' + esc(", ".join(vo.get("words_avoid", []))) + "</div></div>")
    for ex in vo.get("examples", []):
        add(f'<h3>{esc(ex.get("context", "Beispiel"))}</h3><div class="dodont"><div class="do">{esc(ex.get("do", ""))}</div><div class="dont">{esc(ex.get("dont", ""))}</div></div>')
    if vo.get("source"):
        add(f'<p class="small muted">Quelle: {esc(vo["source"])}</p>')
    add("</section>")

    # Do/Don't
    add('<section id="dodont"><h2>Do & Don\'t</h2>')
    for d in kit.get("do_dont", []):
        add(f'<h3>{esc(d.get("topic", ""))} {badge(d.get("status"))}</h3><div class="dodont"><div class="do">{esc(d.get("do", ""))}</div><div class="dont">{esc(d.get("dont", ""))}</div></div>')
    add("</section>")

    # UI
    ui = kit.get("ui", {})
    add(f'''<section id="ui"><h2>UI-Elemente {badge(ui.get("status"))}</h2><p class="muted small">Gerendert mit <code>brand.css</code>. Verhalten und Zustände: <code>core/components/</code>.</p>
<div class="ui-row">
 <button type="button" style="font:600 16px var(--font-family-body);background:var(--color-action-primary-bg);color:var(--color-action-primary-text);border:0;border-radius:var(--radius-control);padding:12px 20px;min-height:44px">{esc(ui.get("primary_label", "Hauptaktion"))}</button>
 <button type="button" style="font:600 16px var(--font-family-body);background:var(--color-action-secondary-bg);color:var(--color-action-secondary-text);border:1.5px solid var(--color-action-secondary-border);border-radius:var(--radius-control);padding:12px 20px;min-height:44px">{esc(ui.get("secondary_label", "Nebenaktion"))}</button>
 <a href="#ui" style="color:var(--color-text-link);font-family:var(--font-family-body)">Textlink</a></div>
<div class="grid">
 <div style="background:var(--color-bg-surface);border:1px solid var(--color-border-default);border-radius:var(--radius-container);padding:var(--space-inset-md);font-family:var(--font-family-body);color:var(--color-text-primary)">
  <div class="pds-text-heading-sm">Karte</div><p style="color:var(--color-text-secondary)">Fläche, Rahmen und Radius aus den Tokens.</p></div>
 <div style="font-family:var(--font-family-body)"><label for="demo-in" style="display:block;font-weight:600;margin-bottom:6px;color:var(--color-text-primary)">Eingabefeld</label>
  <input id="demo-in" placeholder="Beispiel" style="width:100%;min-height:44px;padding:8px 12px;border:1.5px solid var(--color-border-strong);border-radius:var(--radius-control);font:16px var(--font-family-body)"></div>
 <div role="note" style="background:var(--color-feedback-success-bg);color:var(--color-feedback-success-text);border:1px solid var(--color-feedback-success-border);border-radius:var(--radius-container);padding:12px 14px;font-family:var(--font-family-body)">✓ Erfolg: gespeichert.</div>
 <div role="note" style="background:var(--color-feedback-error-bg);color:var(--color-feedback-error-text);border:1px solid var(--color-feedback-error-border);border-radius:var(--radius-container);padding:12px 14px;font-family:var(--font-family-body)">✕ Fehler: Bitte Datum ergänzen.</div>
</div></section>''')

    # Kanäle
    add('<section id="channels"><h2>Kanäle</h2><table><thead><tr><th>Kanal</th><th>Status</th><th>Logo</th><th>CTA</th><th>Regeln</th><th>Ausgabe</th></tr></thead><tbody>')
    for ch, node in (kit.get("channels") or {}).items():
        if ch not in CHANNELS:
            continue
        files = channel_files.get(ch, [])
        links = " · ".join(f'<a href="{esc(f)}">{esc(Path(f).name)}</a>' for f in files) or "—"
        add(f'<tr><td><strong>{esc(ch)}</strong></td><td>{badge(node.get("status"))}</td><td>{esc(node.get("logo", "—"))}</td>'
            f'<td>{esc(node.get("cta_style", "—"))}</td><td class="small">{esc(node.get("notes", ""))}</td><td class="small">{links}</td></tr>')
    add('</tbody></table><p class="small muted">Kanalregeln: <code>core/templates/cross-channel.md</code>. Plattformmaße und rechtliche Pflichten vor jeder Produktion aktuell prüfen.</p>')
    thumbs = [f for ch in channel_files for f in channel_files[ch] if f.endswith(".png")]
    if thumbs:
        add('<div class="grid">' + "".join(f'<img class="thumb" src="{esc(t)}" alt="Vorschau {esc(Path(t).stem)}">' for t in thumbs) + "</div>")
    add("</section>")

    # Offene Punkte
    add('<section id="open"><h2>Offene Punkte</h2>')
    if rep.open_items:
        add("<p>Diese Punkte sind nicht freigegeben und dürfen nicht als freigegeben verwendet werden.</p><table><thead><tr><th>Bereich</th><th>Status</th></tr></thead><tbody>")
        for w, s in rep.open_items:
            add(f'<tr><td>{esc(w)}</td><td><span class="pds-open">{esc(s)}</span></td></tr>')
        add("</tbody></table>")
    else:
        add("<p>Keine offenen Punkte.</p>")
    add(f'<footer>Brand Kit {esc(m["name"])} · v{esc(m["version"])} · {esc(m["status"])} · Core {esc(m["core_version"])} · '
        f'erzeugt am {datetime.date.today().isoformat()} mit PDS Brand-Kit-Generator {GEN_VERSION}</footer></section>')

    add("""</main></div><script>
document.querySelectorAll('.copy').forEach(function(b){b.addEventListener('click',function(){var t=b.getAttribute('data-copy');
function done(){var o=b.textContent;b.textContent='Kopiert';setTimeout(function(){b.textContent=o},1200)}
if(navigator.clipboard){navigator.clipboard.writeText(t).then(done,function(){})}else{var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy');done()}catch(e){}a.remove()}})});
</script></body></html>""")
    return "\n".join(out)


# ───────────────────────── Konsistenz ─────────────────────────
def consistency(files, flat, rep):
    allowed = {resolve(p, flat).lower() for p in flat if isinstance(resolve(p, flat), str) and HEX.match(resolve(p, flat))}
    fams = set()
    for p in flat:
        if p.startswith("font.family"):
            v = resolve(p, flat)
            fams.add(v.split(",")[0].strip().strip('"\'').lower())
    hexre = re.compile(r"#[0-9a-fA-F]{6}\b")
    famre = re.compile(r"font-family\s*:\s*([^;}<]+)")
    bad = 0
    for f in files:
        txt = Path(f).read_text(encoding="utf-8")
        foreign = sorted({h.lower() for h in hexre.findall(txt)} - allowed)
        if foreign:
            bad += 1
            rep.err(f"Konsistenz: {Path(f).name} enthält Farben außerhalb der Tokens: {', '.join(foreign[:6])}")
        for fm in famre.findall(txt):
            first = html.unescape(fm).split(",")[0].strip().strip('"\'').strip().lower()
            if first.startswith("var(") or first in fams or first in ("inherit", "ui-monospace"):
                continue
            bad += 1
            rep.err(f"Konsistenz: {Path(f).name} verwendet Schrift außerhalb der Tokens: {first}")
    if not bad:
        rep.ok(f"Konsistenz: {len(files)} Kanal-Ausgaben verwenden nur Token-Farben und Token-Schriften")


# ───────────────────────── Hauptablauf ─────────────────────────
def main():
    ap = argparse.ArgumentParser(description="PDS Brand-Kit-Generator")
    ap.add_argument("kit")
    ap.add_argument("--no-export", action="store_true")
    ap.add_argument("--chrome")
    a = ap.parse_args()

    kit_path = Path(a.kit).resolve()
    kit_dir = kit_path.parent
    kit = json.loads(kit_path.read_text(encoding="utf-8"))
    global DEMO
    DEMO = bool(kit.get("meta", {}).get("demo"))
    rep = Report()
    dist = kit_dir / "dist"
    if dist.exists():
        shutil.rmtree(dist)
    (dist / "assets").mkdir(parents=True)
    (dist / "channels").mkdir()

    tok = kit.get("tokens", {})
    tree = {}
    for f in tok.get("files", []):
        deep_merge(tree, json.loads((kit_dir / f).read_text(encoding="utf-8")))
    flat = flatten(tree)
    flat_dark = flatten(json.loads((kit_dir / tok["dark"]).read_text(encoding="utf-8"))) if tok.get("dark") else {}

    validate(kit, kit_dir, flat, rep)

    for lg in kit.get("logos", []):
        if lg.get("_exists"):
            shutil.copy(kit_dir / lg["file"], dist / "assets" / Path(lg["file"]).name)

    (dist / "brand.css").write_text(build_css(flat, flat_dark, kit), encoding="utf-8")

    chrome_bin = None if a.no_export else find_chrome(a.chrome)
    if not a.no_export and not chrome_bin:
        rep.warn("Chrome/Chromium nicht gefunden: PDF- und PNG-Export übersprungen")

    # Kanäle
    channel_files, generated = {}, []
    for ch, node in (kit.get("channels") or {}).items():
        if ch not in CHANNELS:
            continue
        starter, kind = CHANNELS[ch]
        src = STARTERS / starter
        if not src.exists():
            rep.err(f"Starter fehlt: {starter}")
            continue
        tpl = src.read_text(encoding="utf-8")
        out_html = dist / "channels" / starter
        out_html.write_text(fill(tpl, kit, kit_dir, flat, rep, f"channels.{ch}", "../"), encoding="utf-8")
        generated.append(out_html)
        files = [f"channels/{starter}"]
        if chrome_bin and kind in ("png", "pdf"):
            size = re.search(r"pds:size\s+(\d+)x(\d+)", tpl)
            if kind == "png" and size:
                png = out_html.with_suffix(".png")
                r = chrome_export(chrome_bin, [f"--screenshot={png}", f"--window-size={size.group(1)},{size.group(2)}", out_html.as_uri()], png)
                if png.exists():
                    files.append(f"channels/{png.name}")
                else:
                    rep.err(f"PNG-Export {ch} fehlgeschlagen: {r.stderr[-200:]}")
            if kind == "pdf":
                pdf = out_html.with_suffix(".pdf")
                chrome_export(chrome_bin, [f"--print-to-pdf={pdf}", out_html.as_uri()], pdf)
                if pdf.exists():
                    files.append(f"channels/{pdf.name}")
                    exp = re.search(r"pds:pages\s+(\d+)", tpl)
                    n = pdf_pages(pdf)
                    if exp and n != int(exp.group(1)):
                        rep.err(f"{ch}: PDF hat {n} Seiten, erwartet {exp.group(1)}")
                    else:
                        rep.ok(f"{ch}: PDF mit {n} Seite(n)")
                else:
                    rep.err(f"PDF-Export {ch} fehlgeschlagen")
        channel_files[ch] = files

    consistency(generated + [dist / "brand.css"] + sorted((dist / "assets").glob("*.svg")), flat, rep)

    # Brand-Kit-HTML (zweimal rendern: erst für die Prüfung, dann mit Endstatus)
    html_path = dist / "BRAND-KIT.html"
    html_path.write_text(build_html(kit, kit_dir, flat, rep, bool(rep.errors), channel_files), encoding="utf-8")
    if chrome_bin:
        pdf = dist / "BRAND-KIT.pdf"
        # Druckfassung: Links auf Dateien werden zu Text, sonst schreibt Chrome absolute file://-Pfade ins PDF
        printable = re.sub(r'<a href="(?!#)[^"]*"([^>]*)>(.*?)</a>', r"<span\1>\2</span>", html_path.read_text(encoding="utf-8"), flags=re.S)
        print_path = dist / "_print.html"
        print_path.write_text(printable, encoding="utf-8")
        chrome_export(chrome_bin, [f"--print-to-pdf={pdf}", print_path.as_uri()], pdf)
        print_path.unlink()
        if pdf.exists():
            n = pdf_pages(pdf)
            rep.ok(f"BRAND-KIT.pdf erzeugt ({n} Seiten, A4)") if n >= 3 else rep.err(f"BRAND-KIT.pdf hat nur {n} Seiten")
        else:
            rep.err("BRAND-KIT.pdf konnte nicht erzeugt werden")
    for p in sorted(dist.rglob("*.pdf")):
        leaks = pdf_local_paths(p)
        if leaks:
            rep.err(f"{p.name} enthält lokale Pfade bzw. file://-Links ({leaks} Fundstellen) – nicht veröffentlichen")
    if any(dist.rglob("*.pdf")) and not any("lokale Pfade" in e for e in rep.errors):
        rep.ok("PDFs ohne lokale Pfade und file://-Links")
    if rep.errors:
        html_path.write_text(build_html(kit, kit_dir, flat, rep, True, channel_files), encoding="utf-8")

    # Bericht
    m = kit["meta"]
    lines = [f"# QA-Bericht · Brand Kit {m['name']} v{m['version']}", "",
             f"- Erzeugt: {datetime.datetime.now().isoformat(timespec='seconds')} · Generator {GEN_VERSION}",
             f"- Kit-Status: **{m['status']}**" + (" · **DEMO (fiktiv)**" if m.get("demo") else ""),
             f"- Ergebnis: **{'FEHLGESCHLAGEN' if rep.errors else 'BESTANDEN'}** · {len(rep.errors)} Fehler · {len(rep.warnings)} Warnungen · {len(rep.open_items)} offene Punkte", ""]
    for title, items in (("Fehler", rep.errors), ("Warnungen", rep.warnings), ("Bestanden", rep.passed)):
        lines += [f"## {title}", ""] + ([f"- {x}" for x in items] or ["- keine"]) + [""]
    lines += ["## Offene Punkte (nicht freigegeben)", ""] + ([f"- {w}: {s}" for w, s in rep.open_items] or ["- keine"]) + [""]
    lines += ["## Ausgaben", "", "- brand.css", "- BRAND-KIT.html", "- BRAND-KIT.pdf" if (dist / "BRAND-KIT.pdf").exists() else "- BRAND-KIT.pdf (nicht erzeugt)"]
    lines += [f"- {f}" for ch in channel_files for f in channel_files[ch]]
    (dist / "QA-REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"{'FEHLGESCHLAGEN' if rep.errors else 'BESTANDEN'}: {len(rep.errors)} Fehler, {len(rep.warnings)} Warnungen, {len(rep.open_items)} offene Punkte → {dist}")
    for e in rep.errors:
        print("  ✕", e)
    for w in rep.warnings:
        print("  !", w)
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
