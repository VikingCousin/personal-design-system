#!/usr/bin/env python3
"""
PDS AI Brand Context Pack · Core 1.1.0

Exportiert die Markenregeln EINES Projekts für externe KI-Tools (ChatGPT, Claude, Gemini …).
Quelle ist ausschließlich das Brand Kit des Projekts (brand-kit.json + Token-Dateien) und,
falls vorhanden und aktuell, dessen BRAND-KIT.pdf. Keine parallele Markenlogik: Validierung,
Token-Auflösung und Status kommen aus build_brand_kit.py.

Aufruf (aus dem Repository-Wurzelverzeichnis):
  python3 core/brand-kit/generator/export_ai_context.py projects/<name>/brand-kit/brand-kit.json
Fehlt brand-kit.json, wird nur eine als ENTWURF markierte Vorlage erzeugt.

Ausgabe: <brand-kit-ordner>/ai-pack/
  AI-BRAND-CONTEXT.md      Markenregeln für KI-Modelle
  CHATGPT-IMAGE-PROMPT.md  wiederverwendbarer Bildprompt
  brand-tokens.json        aufgelöste Design Tokens mit Status
  BRAND-KIT.pdf            visuelle Referenz (nur wenn vorhanden, aktuell und unbedenklich)
  assets/                  nur ausdrücklich zur KI-Weitergabe freigegebene Assets
  MANIFEST.json            Version, Status, Prüfsummen (für Versionssynchronität)
  README.md                Anleitung zum Hochladen
  EXPORT-CHECK.md          Datenschutz-/Weitergabeprüfung
Keine automatische Veröffentlichung. Exit-Code 1 = Paket nicht weitergeben.
"""
import datetime
import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_brand_kit as bk  # noqa: E402

EXPORT_VERSION = "1.1.0"
REPO = bk.CORE.parent
OFFEN = "OFFEN"

# Muster für Inhalte, die nicht an externe KI-Dienste gehen sollen
PRIVACY_PATTERNS = [
    ("E-Mail-Adresse", re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")),
    ("Telefonnummer", re.compile(r"(?<![\w#/.])(?:\+\d{1,3}|0)[\d ()/-]{5,}\d(?![\w/])")),
    ("IBAN", re.compile(r"\b[A-Z]{2}\d{2}(?: ?[A-Z0-9]{4}){3,7}\b")),
    ("lokaler Pfad", re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\\\|~/)[^\s)]*")),
    ("interner Projektpfad", re.compile(r"(?:\.\./|projects/|brief/|research/|prototypes/)[\w./-]+")),
    ("Secret/Token", re.compile(r"(?i)(?:api[_-]?key|secret|passwor[dt]|bearer\s|sk-[A-Za-z0-9]{16,}|gh[pousr]_[A-Za-z0-9]{16,}|AKIA[0-9A-Z]{16})")),
    ("Vertraulichkeitsvermerk", re.compile(r"(?i)\b(?:vertraulich|confidential|intern(?:e|er)? strategie|nicht weitergeben)\b")),
]


def status_text(kit, errors):
    m = kit["meta"]
    if m.get("demo"):
        return "DEMO · fiktive Beispielmarke · nicht freigegeben"
    if m.get("status") == "FREIGEGEBEN" and not errors:
        return f"FREIGEGEBEN am {m.get('approved_at')}"
    return "ENTWURF · nicht freigegeben · nur zur Abstimmung"


def lbl(st):
    return bk.LABEL.get(st, OFFEN) + (" (Demo)" if bk.DEMO and st == "ENTSCHIEDEN" else "")


def other_project_names(own_dir):
    names = set()
    for base in ("projects", "demo"):
        for d in (REPO / base).glob("*"):
            if d.is_dir() and d.resolve() not in own_dir.resolve().parents and d.resolve() != own_dir.resolve():
                names.add(d.name)
    return names


def shareable(item):
    """Asset darf nur raus, wenn freigegeben, ausdrücklich für KI-Weitergabe markiert und Rechte geklärt."""
    return item.get("status") == "ENTSCHIEDEN" and item.get("ai_share") is True and item.get("rights_cleared") is True and item.get("_exists")


# ───────────────────────── Inhalte ─────────────────────────
def build_context(kit, flat, rep, head):
    m = kit["meta"]
    L = []
    a = L.append
    a(f"# AI Brand Context · {m['name']}")
    a("")
    a(f"> **Status: {head}** · Brand-Kit-Version **{m['version']}** · Stand {m['updated']} · PDS Core {m['core_version']}")
    a("")
    a("## Anweisungen für das KI-Modell")
    a("")
    a("1. Verwende für diese Marke ausschließlich die Regeln und Werte in dieser Datei und in `brand-tokens.json`.")
    a("2. Erfinde keine neuen Farben, Schriften, Logos, Slogans, Markenwerte oder Fakten (Preise, Kundenstimmen, Auszeichnungen).")
    a(f"3. Alles mit **{OFFEN}** ist nicht entschieden: nicht als final verwenden, sondern nachfragen oder als Platzhalter kennzeichnen.")
    a("4. **Logos nicht generieren oder nachzeichnen.** Plane eine freie Fläche ein; das Logo wird nachträglich aus `assets/` eingesetzt.")
    a("5. Wenn eine Anfrage diesen Regeln widerspricht, weise darauf hin, bevor du etwas erzeugst.")
    a("6. KI-generierte Bilder sind als KI-generiert zu behandeln und nicht als dokumentarische Fotos auszugeben.")
    if head.startswith("ENTWURF") or head.startswith("DEMO"):
        a("7. **Diese Marke ist nicht freigegeben.** Ergebnisse sind Entwürfe und müssen so gekennzeichnet werden.")
    a("")

    idn = kit.get("identity", {})
    a(f"## Positionierung und Identität · {lbl(idn.get('status'))}")
    a("")
    a(f"- **In einem Satz:** {idn.get('one_liner') or OFFEN}")
    a(f"- **Positionierung:** {idn.get('positioning') or OFFEN}")
    vals = idn.get("values") or []
    a("- **Markenwerte:** " + ("; ".join(f"{v.get('name')} ({v.get('description', '')})" for v in vals) if vals else OFFEN))
    p = idn.get("personality") or {}
    a(f"- **Wirkt:** {', '.join(p.get('is', [])) or OFFEN}")
    a(f"- **Wirkt nie:** {', '.join(p.get('is_not', [])) or OFFEN}")
    a("")

    a("## Farben")
    a("")
    a("| Name | Rolle | HEX | RGB | Verwendung | Status |")
    a("|---|---|---|---|---|---|")
    for c in kit.get("colors", []):
        try:
            v = bk.resolve(c["token"], flat)
            r, g, b = bk.hex_rgb(v)
            a(f"| {c.get('name', c['token'])} | {c.get('role', '')} | `{v}` | {r}, {g}, {b} | {c.get('usage', '')} | {lbl(c.get('status'))} |")
        except (KeyError, ValueError):
            a(f"| {c.get('name', c.get('token'))} | {c.get('role', '')} | {OFFEN} | {OFFEN} | {c.get('usage', '')} | {OFFEN} |")
    if not kit.get("colors"):
        a(f"| {OFFEN} | | | | | |")
    a("")
    a("Feste UI-Rollen (aus den Tokens): " + ", ".join(
        f"{n} `{bk.resolve(t, flat)}`" for n, t in (("Text", "color.text.primary"), ("Hintergrund", "color.bg.canvas"),
                                                   ("Hauptaktion", "color.action.primary.bg"), ("Text auf Hauptaktion", "color.action.primary.text"))
        if t in flat) + ". Kontrast mindestens 4.5:1 für Text, 3:1 für großen Text.")
    a("")

    typ = kit.get("typography", {})
    a(f"## Typografie · {lbl(typ.get('status'))}")
    a("")
    for f in typ.get("families", []):
        a(f"- **{f.get('name') or OFFEN}** ({f.get('token', '').split('.')[-1]}), Fallback: {f.get('fallback', '—')} · Lizenz: {f.get('license', OFFEN)} · {lbl(f.get('license_status'))}")
    if not typ.get("families"):
        a(f"- {OFFEN}")
    rows = []
    for s in typ.get("styles", []):
        try:
            v = bk.resolve(s, flat)
            rows.append(f"{s.replace('text.', '')}: {v.get('fontSize')} / {v.get('fontWeight')}")
        except (KeyError, AttributeError):
            pass
    if rows:
        a("- **Hierarchie:** " + " · ".join(rows))
    a("")

    a("## Logo-Verwendung")
    a("")
    for lg in kit.get("logos", []):
        ms = lg.get("min_size", {})
        share = "liegt in `assets/`" if shareable(lg) else "nicht im Paket"
        bgname = {"light": "helle", "dark": "dunkle", "any": "beliebige"}.get(lg.get("background"), lg.get("background", "—"))
        a(f"- **{lg.get('name', lg.get('id'))}** ({lg.get('variant')}, für {bgname} Hintergründe) · Mindestgröße {ms.get('digital_px', '—')} px · Schutzraum: {lg.get('clear_space', '—')} · {lbl(lg.get('status'))} · {share}")
    if not kit.get("logos"):
        a(f"- {OFFEN}")
    a("- Logo nie verzerren, umfärben, mit Effekten versehen oder auf unruhige Bildflächen setzen.")
    a("")

    a("## Bildsprache")
    a("")
    for key, name in (("photography", "Fotografie"), ("icons", "Icons"), ("illustration", "Illustration")):
        n = bk.get_path(kit, f"imagery.{key}") or {}
        a(f"- **{name}** · {lbl(n.get('status'))}: {n.get('description') or OFFEN}")
        if n.get("do"):
            a(f"  - Do: {', '.join(n['do'])}")
        if n.get("dont"):
            a(f"  - Don't: {', '.join(n['dont'])}")
    a("")

    vo = kit.get("voice", {})
    a(f"## Tonalität · {lbl(vo.get('status'))}")
    a("")
    a(f"- **Stil:** {vo.get('summary') or OFFEN}")
    a(f"- **Anrede:** {vo.get('address_rule') or OFFEN}")
    if vo.get("principles"):
        a(f"- **Regeln:** {'; '.join(vo['principles'])}")
    if vo.get("words_use"):
        a(f"- **Verwenden:** {', '.join(vo['words_use'])}")
    if vo.get("words_avoid"):
        a(f"- **Vermeiden:** {', '.join(vo['words_avoid'])}")
    for ex in vo.get("examples", []):
        a(f"- {ex.get('context', 'Beispiel')}: ✓ „{ex.get('do', '')}“ · ✕ „{ex.get('dont', '')}“")
    a("")

    a("## Do / Don't")
    a("")
    for d in kit.get("do_dont", []):
        a(f"- **{d.get('topic', '')}** ({lbl(d.get('status'))}): ✓ {d.get('do', '')} · ✕ {d.get('dont', '')}")
    if not kit.get("do_dont"):
        a(f"- {OFFEN}")
    a("")

    a("## Kanäle")
    a("")
    a("| Kanal | Status | Logo | CTA | Regeln |")
    a("|---|---|---|---|---|")
    for ch, n in (kit.get("channels") or {}).items():
        a(f"| {ch} | {lbl(n.get('status'))} | {n.get('logo', '—')} | {n.get('cta_style', '—')} | {n.get('notes', '')} |")
    a("")
    a("Plattformmaße und rechtliche Pflichten (z. B. Werbekennzeichnung) vor jeder Veröffentlichung aktuell prüfen.")
    a("")

    a(f"## Offene Punkte ({len(rep.open_items)})")
    a("")
    seen = set()
    for w, s in rep.open_items:
        w = re.sub(r"^channels\.[a-z_]+: channels\.[a-z_]+\.sample\..*$", "fehlender Beispielinhalt in einem Kanal", w)
        if (w, s) not in seen:
            seen.add((w, s))
            a(f"- {w}: **{s}**")
    if not rep.open_items:
        a("- keine")
    a("")
    a("---")
    a(f"Erzeugt mit PDS AI Brand Context Pack {EXPORT_VERSION} aus Brand Kit v{m['version']}. Bei einer neuen Brand-Kit-Version alle Dateien dieses Pakets ersetzen.")
    return "\n".join(L) + "\n"


def build_prompt(kit, flat, head):
    m = kit["meta"]
    cols = []
    for c in kit.get("colors", []):
        try:
            cols.append(f"{c.get('name')} {bk.resolve(c['token'], flat)} ({c.get('usage', c.get('role'))})" + ("" if c.get("status") == "ENTSCHIEDEN" else f" [{OFFEN}]"))
        except KeyError:
            pass
    ph = bk.get_path(kit, "imagery.photography") or {}
    il = bk.get_path(kit, "imagery.illustration") or {}
    vo = kit.get("voice", {})
    return f"""# ChatGPT-Bildprompt · {m['name']}

> Status: **{head}** · Brand-Kit-Version {m['version']} · gehört zu `AI-BRAND-CONTEXT.md` derselben Version.

## So verwenden
1. `AI-BRAND-CONTEXT.md`, `brand-tokens.json` und ggf. `BRAND-KIT.pdf` als Projektdateien hochladen.
2. Den Prompt unten kopieren, die Felder in [ECKIGEN KLAMMERN] ausfüllen.
3. Ergebnis gegen die Do/Don'ts prüfen. Logo nachträglich aus `assets/` einsetzen, nicht generieren lassen.
4. Vor Veröffentlichung: Kennzeichnung KI-generierter Bilder, Bildrechte und Plattformmaße prüfen.

## Prompt

```
Erstelle ein Bild für die Marke „{m['name']}“ gemäß der hochgeladenen Datei AI-BRAND-CONTEXT.md (Version {m['version']}).

Verwendung: [Profilbild | Social-Media-Grafik | Newsletter-Kopfbild | Website-Hero | Präsentationsfolie | Dokument-Titel]
Format/Seitenverhältnis: [z. B. 1:1, 4:5, 9:16, 2:3, 16:9 – aktuelles Plattformmaß prüfen]
Motiv: [konkret beschreiben, was zu sehen ist]
Text im Bild: [kein Text | maximal 5 Wörter: „…“]

Markenregeln:
- Farben nur aus dieser Palette: {'; '.join(cols) or OFFEN}
- Fotografie: {ph.get('description') or OFFEN}
- Bevorzugt: {', '.join(ph.get('do', [])) or OFFEN}
- Vermeiden: {', '.join(ph.get('dont', [])) or OFFEN}
- Illustration: {il.get('description') or OFFEN}{'' if il.get('status') == 'ENTSCHIEDEN' else f' [{OFFEN}: keine Illustrationen verwenden, bis entschieden]'}
- Wirkung: {', '.join((kit.get('identity') or {}).get('personality', {}).get('is', [])) or OFFEN}; niemals: {', '.join((kit.get('identity') or {}).get('personality', {}).get('is_not', [])) or OFFEN}
- Kein Logo zeichnen. Freie, ruhige Fläche [oben links | unten rechts] für das Logo lassen.
- Keine erfundenen Personen als echte Kunden oder Team darstellen, keine erfundenen Zahlen oder Auszeichnungen.
- Tonalität für Bildtext: {vo.get('summary') or OFFEN}

Wenn etwas davon als {OFFEN} markiert ist, frage nach, statt es zu erfinden.
```
"""


def resolved_tokens(flat, head, kit):
    tree = {"$description": f"Aufgelöste Design Tokens · {kit['meta']['name']} · Brand-Kit-Version {kit['meta']['version']} · Status: {head}"}
    for p in sorted(flat):
        node = tree
        parts = p.split(".")
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = {"$type": flat[p]["type"], "$value": bk.resolve(p, flat)}
    return tree


def scan(files, own_dir, kit, rep_lines):
    findings = []
    others = other_project_names(own_dir)
    for f in files:
        txt = Path(f).read_text(encoding="utf-8", errors="ignore")
        if str(f).endswith(".svg"):
            # nur menschenlesbare Inhalte prüfen (Texte, Beschriftungen, Metadaten), nicht Geometrie
            parts = re.findall(r">([^<]+)<", txt) + re.findall(r'(?:aria-label|title|alt|xlink:href|href)="([^"]*)"', txt)
            parts += re.findall(r"<(?:metadata|desc|title)[^>]*>(.*?)</", txt, re.S) + re.findall(r"<!--(.*?)-->", txt, re.S)
            txt = "\n".join(parts)
        for label, rx in PRIVACY_PATTERNS:
            for hit in set(rx.findall(txt)):
                if label == "Telefonnummer" and (len(re.sub(r"\D", "", hit)) < 7 or re.fullmatch(r"\d{1,3}(?:/\d{1,3}){3}", hit.strip())
                                                 or re.search(r"\d{4}-\d{2}-\d{2}", hit)):
                    continue
                findings.append((Path(f).name, label, hit if len(hit) < 60 else hit[:57] + "…"))
        for name in others:
            if re.search(rf"\b{re.escape(name)}\b", txt, re.I):
                findings.append((Path(f).name, "anderes Projekt erwähnt", name))
    return findings


def draft_template(out, project_hint):
    out.mkdir(parents=True)
    (out / "AI-BRAND-CONTEXT.md").write_text(f"""# AI Brand Context · {project_hint}

> **Status: ENTWURF · VORLAGE · kein Brand Kit vorhanden · nicht an KI-Dienste weitergeben**

Für dieses Projekt gibt es noch kein Brand Kit (`brand-kit/brand-kit.json`). Alle Markenregeln sind **{OFFEN}**:
Positionierung, Markenwerte, Farben, Typografie, Logo, Bildsprache, Tonalität, Do/Don't, Kanäle.

Nächster Schritt: Brand Kit aus `core/process/project-template/brand-kit/` anlegen und füllen (bzw. bestehende Marke importieren), dann diesen Export erneut ausführen.
""", encoding="utf-8")
    print(f"ENTWURF-VORLAGE erzeugt (kein Brand Kit): {out}")
    return 1


# ───────────────────────── Hauptablauf ─────────────────────────
def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    kit_path = Path(sys.argv[1]).resolve()
    kit_dir = kit_path.parent
    out = kit_dir / "ai-pack"
    if out.exists():
        shutil.rmtree(out)
    if not kit_path.exists():
        return draft_template(out, kit_dir.parent.name)

    kit = json.loads(kit_path.read_text(encoding="utf-8"))
    bk.DEMO = bool(kit.get("meta", {}).get("demo"))
    tree = {}
    for f in kit.get("tokens", {}).get("files", []):
        bk.deep_merge(tree, json.loads((kit_dir / f).read_text(encoding="utf-8")))
    flat = bk.flatten(tree)
    rep = bk.Report()
    bk.validate(kit, kit_dir, flat, rep)
    head = status_text(kit, rep.errors)
    m = kit["meta"]

    out.mkdir(parents=True)
    (out / "assets").mkdir()
    (out / "AI-BRAND-CONTEXT.md").write_text(build_context(kit, flat, rep, head), encoding="utf-8")
    (out / "CHATGPT-IMAGE-PROMPT.md").write_text(build_prompt(kit, flat, head), encoding="utf-8")
    (out / "brand-tokens.json").write_text(json.dumps(resolved_tokens(flat, head, kit), ensure_ascii=False, indent=2), encoding="utf-8")

    log, excluded = [], []
    # Assets: nur ausdrücklich freigegeben + KI-Weitergabe + Rechte geklärt
    for item in kit.get("logos", []) + kit.get("reference_assets", []):
        if item not in kit.get("logos", []):
            item["_exists"] = bool(item.get("file")) and (kit_dir / item["file"]).exists()
        if shareable(item):
            shutil.copy(kit_dir / item["file"], out / "assets" / Path(item["file"]).name)
            log.append(f"Asset übernommen: {Path(item['file']).name}")
        else:
            why = [w for w, c in (("nicht freigegeben", item.get("status") != "ENTSCHIEDEN"), ("nicht für KI-Weitergabe markiert", item.get("ai_share") is not True),
                                 ("Rechte nicht bestätigt", item.get("rights_cleared") is not True), ("Datei fehlt", not item.get("_exists"))) if c]
            excluded.append(f"{item.get('id', item.get('file'))}: {', '.join(why)}")

    # BRAND-KIT.pdf nur, wenn aktuell (gleiche Version) und ohne bedenkliche Inhalte
    pdf, html_file = kit_dir / "dist" / "BRAND-KIT.pdf", kit_dir / "dist" / "BRAND-KIT.html"
    pdf_ok = False
    if pdf.exists() and html_file.exists() and f"v{m['version']}" in html_file.read_text(encoding="utf-8") and pdf.stat().st_mtime >= kit_path.stat().st_mtime:
        text = re.sub(r"<style.*?</style>|<script.*?</script>|<[^>]+>", " ", html_file.read_text(encoding="utf-8"), flags=re.S)
        tmp = out / "_pdf-text.txt"
        tmp.write_text(html.unescape(text), encoding="utf-8")
        pdf_findings = scan([tmp], kit_dir.parent, kit, log)
        tmp.unlink()
        if bk.pdf_local_paths(pdf):
            pdf_findings.append(("BRAND-KIT.pdf", "lokaler Pfad im PDF", "file:// bzw. absoluter Pfad"))
        if pdf_findings:
            excluded.append("BRAND-KIT.pdf: bedenkliche Inhalte (" + "; ".join(f"{l}: {h}" for _, l, h in pdf_findings[:5]) + ")")
        else:
            shutil.copy(pdf, out / "BRAND-KIT.pdf")
            pdf_ok = True
    else:
        excluded.append("BRAND-KIT.pdf: nicht vorhanden oder älter als brand-kit.json – zuerst build_brand_kit.py ausführen")

    text_files = [out / n for n in ("AI-BRAND-CONTEXT.md", "CHATGPT-IMAGE-PROMPT.md", "brand-tokens.json")]
    findings = scan(text_files, kit_dir.parent, kit, log)
    for a in (out / "assets").glob("*.svg"):
        findings += scan([a], kit_dir.parent, kit, log)

    files = sorted(p for p in out.rglob("*") if p.is_file())
    manifest = {"pack": "PDS AI Brand Context Pack", "exporter": EXPORT_VERSION, "brand": m["name"], "brand_kit_version": m["version"],
                "status": head, "demo": bool(m.get("demo")), "generated": datetime.datetime.now().isoformat(timespec="seconds"),
                "files": {str(p.relative_to(out)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    (out / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    (out / "README.md").write_text(f"""# AI Brand Context Pack · {m['name']} · v{m['version']}

**Status: {head}**

## In ein ChatGPT-Projekt (oder Claude-Projekt, Gemini Gem …) hochladen
1. `AI-BRAND-CONTEXT.md` (Pflicht)
2. `brand-tokens.json` (Pflicht für Websites, Newsletter, Präsentationen)
3. `BRAND-KIT.pdf` (optional, visuelle Referenz){'' if pdf_ok else ' – in diesem Paket nicht enthalten'}
4. Dateien aus `assets/` nur, wenn das Logo als Referenz gebraucht wird
5. `CHATGPT-IMAGE-PROMPT.md` nicht hochladen, sondern als Vorlage zum Kopieren nutzen

In die Projektanweisungen: „Halte dich bei allen Ergebnissen an AI-BRAND-CONTEXT.md (Version {m['version']}). Erfinde keine Markenwerte. Frage bei OFFEN nach.“

## Versionen synchron halten
- Quelle der Wahrheit ist `brand-kit.json` im Design System, nie die Kopie im KI-Tool.
- Nach jeder Änderung: Brand Kit neu erzeugen, dann dieses Paket neu exportieren.
- Im KI-Tool **alle** Dateien der alten Version löschen und die neuen hochladen. Die Version steht in jeder Datei und in `MANIFEST.json`.

Weitergabe an externe KI-Dienste ist eine Veröffentlichung im Sinne von Gate G6: nur nach Prüfung von `EXPORT-CHECK.md` und eigener Freigabe.
""", encoding="utf-8")

    ok = not findings and not rep.errors
    check = [f"# Export-Check · {m['name']} v{m['version']}", "", f"- Ergebnis: **{'WEITERGABE MÖGLICH (nach eigener Freigabe)' if ok else 'NICHT WEITERGEBEN'}**",
             f"- Status des Brand Kits: {head}", f"- Brand-Kit-QA: {len(rep.errors)} Fehler, {len(rep.open_items)} offene Punkte", "",
             "## Funde (personenbezogene Daten, Secrets, Pfade, Vertrauliches, andere Projekte)", ""]
    check += [f"- {f}: {l} → `{h}`" for f, l, h in findings] or ["- keine"]
    check += ["", "## Brand-Kit-Fehler", ""] + ([f"- {e}" for e in rep.errors] or ["- keine"])
    check += ["", "## Nicht ins Paket übernommen", ""] + ([f"- {e}" for e in excluded] or ["- nichts"])
    check += ["", "## Bewusst nie exportiert", "", "- Beispielinhalte der Kanäle (können Adressen, Impressum, Kontaktdaten enthalten)",
              "- Quellverweise auf interne Dateien, Freigebende Person (`approved_by`)", "- Brief, Research, Entscheidungslog, andere Projekte",
              "", "## Manuell zu prüfen (nicht automatisierbar)", "", "- Bildrechte und Lizenzen der Assets und Schriften für die Nutzung in KI-Tools",
              "- Ob Positionierung und Markenwerte bereits öffentlich sein dürfen",
              "- Bildinhalte im BRAND-KIT.pdf (z. B. Kanal-Vorschauen mit Adressen) – Text in Bildern wird nicht automatisch geprüft", "- Nutzungsbedingungen und Datenschutz des KI-Dienstes"]
    (out / "EXPORT-CHECK.md").write_text("\n".join(check) + "\n", encoding="utf-8")

    print(f"{'OK' if ok else 'NICHT WEITERGEBEN'}: {head} · {len(findings)} Funde · {len(excluded)} ausgeschlossen → {out}")
    for f, l, h in findings:
        print(f"  ! {f}: {l}: {h}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
