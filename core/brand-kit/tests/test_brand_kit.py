"""
Automatisierte Tests · PDS Core 1.1.0 · Brand Kit, Kanal-Starter, AI Brand Context Pack

Ausführen (aus dem Repository-Wurzelverzeichnis):
  python3 -m unittest discover -s core/brand-kit/tests -v

Nur Python-Standardbibliothek. Tests mit PDF/PNG-Export laufen nur, wenn Chrome/Chromium gefunden wird.
Alle Tests arbeiten auf temporären Kopien der fiktiven Demo-Marke; das Repository wird nicht verändert.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import urllib.parse
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
GEN = REPO / "core" / "brand-kit" / "generator"
BUILD = GEN / "build_brand_kit.py"
EXPORT = GEN / "export_ai_context.py"
DEMO = REPO / "demo" / "radhof-demo"
TEMPLATE_KIT = REPO / "core" / "process" / "project-template" / "brand-kit" / "brand-kit.json"

sys.path.insert(0, str(GEN))
import build_brand_kit as bk  # noqa: E402


def run(script, kit, *args):
    return subprocess.run([sys.executable, str(script), str(kit), *args], capture_output=True, text=True, timeout=600)


class DemoCopy:
    """Temporäre Kopie der Demo-Marke, optional mit Änderungen an brand-kit.json."""

    def __init__(self, change=None):
        self.tmp = Path(tempfile.mkdtemp(prefix="pds-test-"))
        self.root = self.tmp / "radhof-demo"
        shutil.copytree(DEMO, self.root, ignore=shutil.ignore_patterns("dist", "ai-pack"))
        self.kit = self.root / "brand-kit" / "brand-kit.json"
        if change:
            data = json.loads(self.kit.read_text(encoding="utf-8"))
            change(data)
            self.kit.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        shutil.rmtree(self.tmp, ignore_errors=True)


class TestDateien(unittest.TestCase):
    def test_json_dateien_gueltig(self):
        for p in list((REPO / "core").rglob("*.json")) + list((REPO / "demo").rglob("*.json")):
            if "dist" in p.parts or "ai-pack" in p.parts:
                continue
            with self.subTest(datei=str(p.relative_to(REPO))):
                json.loads(p.read_text(encoding="utf-8"))

    def test_starter_ohne_feste_farben_und_schriften(self):
        for p in (GEN / "starters").glob("*.html"):
            txt = p.read_text(encoding="utf-8")
            with self.subTest(starter=p.name):
                self.assertEqual(re.findall(r"#[0-9a-fA-F]{6}\b", txt), [], "feste HEX-Farbe im Starter")
                for fam in re.findall(r"font-family\s*:\s*([^;}\"<]+)", txt):
                    self.assertTrue(fam.strip().startswith(("var(", "{{token:")), f"feste Schrift: {fam}")

    def test_core_bleibt_markenneutral(self):
        verboten = re.compile(r"radhof|barlow|c2410c|memorial|medaill|friedhof|steinmetz|lebensbuch", re.I)
        bereiche = ["principles", "tokens", "components", "templates", "process", "agent-skill", "patterns"]
        for b in bereiche:
            for p in (REPO / "core" / b).rglob("*"):
                if p.is_file() and p.suffix in (".md", ".json", ".html"):
                    with self.subTest(datei=str(p.relative_to(REPO))):
                        self.assertIsNone(verboten.search(p.read_text(encoding="utf-8")))
        for p in (GEN / "starters").glob("*.html"):
            self.assertIsNone(verboten.search(p.read_text(encoding="utf-8")), p.name)

    def test_interne_links_gueltig(self):
        files = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=REPO,
                               capture_output=True, text=True).stdout.split()
        pub = {os.path.normpath(f) for f in files}

        def slug(h):
            h = re.sub(r"[`*_]", "", h.strip().lower())
            return re.sub(r"[^\w\- ]", "", h, flags=re.U).replace(" ", "-")
        anchors = {}
        for f in files:
            if f.endswith(".md") and (REPO / f).exists():
                t = re.sub(r"```.*?```", "", (REPO / f).read_text(encoding="utf-8"), flags=re.S)
                anchors[os.path.normpath(f)] = {slug(m) for m in re.findall(r"^#+\s+(.*)$", t, flags=re.M)}
        broken = []
        for f in anchors:
            t = re.sub(r"```.*?```", "", (REPO / f).read_text(encoding="utf-8"), flags=re.S)
            for m in re.finditer(r"\]\(([^)\s]+)\)", t):
                link = m.group(1)
                if link.startswith(("http", "mailto:")):
                    continue
                path, _, anc = link.partition("#")
                tgt = os.path.normpath(os.path.join(os.path.dirname(f), urllib.parse.unquote(path))) if path else f
                ok = tgt in pub or any(x.startswith(tgt.rstrip("/") + "/") for x in pub)
                if not ok or (anc and tgt.endswith(".md") and urllib.parse.unquote(anc) not in anchors.get(tgt, set())):
                    broken.append(f"{f} → {link}")
        self.assertEqual(broken, [])

    def test_veroeffentlichte_pdfs_ohne_lokale_pfade(self):
        for pdf in list(REPO.glob("*.pdf")) + list((REPO / "demo").rglob("*.pdf")):
            if "ai-pack" in pdf.parts:
                continue
            with self.subTest(pdf=str(pdf.relative_to(REPO))):
                self.assertEqual(bk.pdf_local_paths(pdf), 0)

    def test_private_und_erzeugte_dateien_ausgeschlossen(self):
        for p in ["projects/digital-legacy/x", "demo/radhof-demo/brand-kit/ai-pack/x", "projects/x/brand-kit/ai-pack/x", ".env", ".DS_Store"]:
            with self.subTest(pfad=p):
                r = subprocess.run(["git", "check-ignore", "-q", p], cwd=REPO)
                self.assertEqual(r.returncode, 0, f"{p} wird nicht ignoriert")


class TestGenerator(unittest.TestCase):
    def test_demo_besteht(self):
        with DemoCopy() as d:
            r = run(BUILD, d.kit, "--no-export")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            qa = (d.kit.parent / "dist" / "QA-REPORT.md").read_text(encoding="utf-8")
            self.assertIn("BESTANDEN", qa)
            self.assertIn("Token-Vertrag vollständig", qa)
            self.assertIn("nur Token-Farben und Token-Schriften", qa)
            html = (d.kit.parent / "dist" / "BRAND-KIT.html").read_text(encoding="utf-8")
            self.assertIn("DEMO · fiktive Beispielmarke", html)
            self.assertIn("OFFEN", html)
            self.assertNotIn(">Freigegeben<", html, "Demo darf keine reale Freigabe zeigen")

    def test_demo_darf_nicht_freigegeben_werden(self):
        def c(k):
            k["meta"]["status"] = "FREIGEGEBEN"
        with DemoCopy(c) as d:
            r = run(BUILD, d.kit, "--no-export")
            self.assertEqual(r.returncode, 1)
            for msg in ("enthält aber Punkte", "approved_by", "Demo-Kit darf nie"):
                self.assertIn(msg, r.stdout)

    def test_kontrast_unbekanntes_token_fehlendes_logo(self):
        def c(k):
            k["contrast_pairs"].append({"fg": "color.text.disabled", "bg": "color.bg.canvas", "min": 4.5})
            k["colors"].append({"token": "color.gibt.es.nicht", "status": "ENTSCHIEDEN"})
            k["logos"][0]["file"] = "../assets/logos/fehlt.svg"
        with DemoCopy(c) as d:
            r = run(BUILD, d.kit, "--no-export")
            self.assertEqual(r.returncode, 1)
            self.assertIn("Kontrast color.text.disabled", r.stdout)
            self.assertIn("color.gibt.es.nicht", r.stdout)
            self.assertIn("Datei fehlt", r.stdout)

    def test_fremde_farbe_in_kanal_wird_erkannt(self):
        def c(k):
            k["channels"]["website"]["sample"]["headline"] = "Farbe #123456"
        with DemoCopy(c) as d:
            r = run(BUILD, d.kit, "--no-export")
            self.assertEqual(r.returncode, 1)
            self.assertIn("#123456", r.stdout)

    def test_echte_freigabe_nur_mit_allen_entscheidungen(self):
        """Freigabe-Logik ohne fiktive Freigabe im Repo: nur in einer temporären Kopie."""
        def c(k):
            k["meta"].update(status="FREIGEGEBEN", demo=False, approved_by="Testlauf", approved_at="2026-10-09")
            k["logos"] = [lg for lg in k["logos"] if lg["status"] == "ENTSCHIEDEN"]
            k["imagery"]["illustration"]["status"] = "ENTSCHIEDEN"
            k["channels"]["pinterest_pin"]["status"] = "ENTSCHIEDEN"
            k["channels"]["pinterest_pin"]["sample"]["url"] = "example.test"
        with DemoCopy(c) as d:
            r = run(BUILD, d.kit, "--no-export")
            self.assertEqual(r.returncode, 0, r.stdout)
            html = (d.kit.parent / "dist" / "BRAND-KIT.html").read_text(encoding="utf-8")
            self.assertIn("Status: FREIGEGEBEN", html)

    @unittest.skipUnless(bk.find_chrome(None), "Chrome/Chromium nicht gefunden")
    def test_export_pdf_und_png(self):
        with DemoCopy() as d:
            r = run(BUILD, d.kit)
            self.assertEqual(r.returncode, 0, r.stdout)
            dist = d.kit.parent / "dist"
            self.assertGreaterEqual(bk.pdf_pages(dist / "BRAND-KIT.pdf"), 3)
            for png in ("instagram-post", "instagram-story", "pinterest-pin", "linkedin-post"):
                self.assertTrue((dist / "channels" / f"{png}.png").exists(), png)
            self.assertEqual(bk.pdf_pages(dist / "channels" / "document-offer.pdf"), 1)
            for pdf in dist.rglob("*.pdf"):
                self.assertEqual(bk.pdf_local_paths(pdf), 0, f"lokaler Pfad in {pdf.name}")


class TestAIPack(unittest.TestCase):
    def test_demo_export(self):
        with DemoCopy() as d:
            r = run(EXPORT, d.kit)
            self.assertEqual(r.returncode, 0, r.stdout)
            pack = d.kit.parent / "ai-pack"
            ctx = (pack / "AI-BRAND-CONTEXT.md").read_text(encoding="utf-8")
            self.assertIn("DEMO", ctx)
            self.assertIn("OFFEN", ctx)
            self.assertNotIn("Musterstraße", ctx, "Kanal-Beispielinhalte dürfen nicht exportiert werden")
            assets = {p.name for p in (pack / "assets").iterdir()}
            self.assertEqual(assets, {"radhof-demo-primary.svg", "radhof-demo-negative.svg"})
            tokens = json.loads((pack / "brand-tokens.json").read_text(encoding="utf-8"))
            self.assertEqual(tokens["color"]["brand"]["primary"]["$value"], bk.resolve("color.brand.primary", bk.flatten(
                bk.deep_merge(json.loads((d.root / "tokens/primitives.tokens.json").read_text()), json.loads((d.root / "tokens/semantic.tokens.json").read_text())))))
            manifest = json.loads((pack / "MANIFEST.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["brand_kit_version"], "0.1.0")
            self.assertIn("AI-BRAND-CONTEXT.md", manifest["files"])

    def test_datenschutzfunde_blockieren(self):
        def c(k):
            k["identity"]["positioning"] += " max@example.org +49 7361 123456 /Users/x/a.md vertraulich api_key"
        with DemoCopy(c) as d:
            r = run(EXPORT, d.kit)
            self.assertEqual(r.returncode, 1)
            for label in ("E-Mail-Adresse", "Telefonnummer", "lokaler Pfad", "Vertraulichkeitsvermerk", "Secret/Token"):
                self.assertIn(label, r.stdout)

    def test_kein_brand_kit_nur_entwurf(self):
        tmp = Path(tempfile.mkdtemp(prefix="pds-test-"))
        try:
            kit = tmp / "p" / "brand-kit" / "brand-kit.json"
            kit.parent.mkdir(parents=True)
            r = run(EXPORT, kit)
            self.assertEqual(r.returncode, 1)
            self.assertIn("ENTWURF · VORLAGE", (kit.parent / "ai-pack" / "AI-BRAND-CONTEXT.md").read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_projektvorlage_ist_entwurf_ohne_assets(self):
        tmp = Path(tempfile.mkdtemp(prefix="pds-test-"))
        try:
            shutil.copytree(TEMPLATE_KIT.parent, tmp / "p" / "brand-kit")
            shutil.copytree(DEMO / "tokens", tmp / "p" / "tokens")
            r = run(EXPORT, tmp / "p" / "brand-kit" / "brand-kit.json")
            self.assertEqual(r.returncode, 0, r.stdout)
            ctx = (tmp / "p" / "brand-kit" / "ai-pack" / "AI-BRAND-CONTEXT.md").read_text(encoding="utf-8")
            self.assertIn("ENTWURF · nicht freigegeben", ctx)
            self.assertGreater(ctx.count("OFFEN"), 20)
            self.assertEqual(list((tmp / "p" / "brand-kit" / "ai-pack" / "assets").iterdir()), [])
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
