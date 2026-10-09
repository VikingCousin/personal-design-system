# 0004 · v1.1: Visual Brand Kit und Cross-Channel-Konsistenz

- **Status:** accepted · **Ebene:** PDS · **Datum:** 2026-10-09 · **Core-Version:** 1.1.0
- **Freigabe:** Auftrag des Nutzers vom 2026-10-09 (Korrekturschleife v1.1, autonom, ohne Markenentscheidungen). Commit und Push erst nach Freigabe.

## 1. Gap Audit (Stand v1.0.0)

| # | Bereich | IST in v1.0 | SOLL | Lücke → Umsetzung in v1.1 |
|---|---|---|---|---|
| 1 | Visual Brand Kit | `templates/brand-guideline.md` beschreibt Kapitel, aber kein Datenmodell und keine Erzeugung | ein strukturiertes, versioniertes Brand Kit je Projekt | **groß** → Brand-Kit-Vertrag + Generator (`brand-kit/`) |
| 2 | Logo-System, Assets | Regeln in `principles/visual-assets.md` §1 (Varianten, Schutzraum, Mindestgröße) | Register freigegebener Logos mit Status und Dateipfad | **mittel** → Abschnitt `logos` im Vertrag, Prüfung fehlender Dateien |
| 3 | Farben, Farbrollen | vollständig in `tokens/color.md` (Rollen, HEX/OKLCH, Print bedingt) | Brand Kit zeigt HEX, RGB, OKLCH, Druckwerte, Kontraste | **klein** → Generator leitet RGB/OKLCH aus Tokens ab, Druckwerte aus dem Kit |
| 4 | Typografie, Lizenzen | Rollen, Skala, Lizenz-Prüfliste in `tokens/typography.md` | Lizenzstatus je Schrift im Kit | **klein** → Feld `license` + Status je Familie |
| 5 | Bildsprache, Icons, Illustration | Regeln in `visual-assets.md`, Projektinhalt in `brand/visual-direction.md` | strukturierte Do/Don'ts im Kit | **klein** → Abschnitt `imagery` |
| 6 | Werte, Positionierung, Voice | `brand/foundation.md`, `brand/voice.md`, `principles/content-writing.md` | Zusammenfassung im Kit | **klein** → Abschnitte `identity`, `voice` (Verweis auf Quelle, keine Kopie der Regeln) |
| 7 | Social Media | nicht vorhanden | Regeln + Ausgangsvorlagen Instagram, Pinterest, LinkedIn | **groß** → `templates/social-media.md`, Starter |
| 8 | Newsletter, E-Mail | nur Bestätigungs-E-Mail in `transaction-flow.md` | Newsletter-Regeln + Vorlage | **groß** → `templates/newsletter-email.md`, Starter |
| 9 | Dokumente, PDF, Präsentation | `templates/document.md`, `presentation.md` | Token-Zuordnung, Export- und QA-Prüfung | **klein** → Verweis auf Kanal-Matrix, Starter für Angebot und Präsentation |
| 10 | Website, App, Dashboard | vorhanden | Kanal-Zuordnung | **klein** → Verweis auf Kanal-Matrix, Website-Starter |
| 11 | Tokens über alle Kanäle | Architektur und Modi, aber kein Build | ein Weg von Tokens zu allen Kanälen | **mittel** → `brand.css` als minimaler CSS-Adapter, Token-Platzhalter für E-Mail (Inline-Werte) |
| 12 | Brand-Kit-HTML und -PDF | keine Erzeugung (Quick Start manuell) | reproduzierbare Ausgabe aus einer Quelle | **groß** → Generator mit HTML, PDF und QA-Bericht |
| 13 | Vorlagen, Asset-Export | Benennung in `assets/README.md` | Export von Social-Grafiken und PDFs mit Prüfung | **mittel** → Generator exportiert PNG/PDF je Starter |

## 2. Entscheidungen

| # | Entscheidung | Begründung |
|---|---|---|
| 1 | **Neuer Core-Bereich `core/brand-kit/`** (Vertrag, Generator, Starter) | Brand Kit ist ein eigenständiger Baustein mit Code; passt nicht in Principles oder Templates |
| 2 | **`brand-kit.json` je Projekt als einzige Quelle**, die **Werte kommen aus den Token-Dateien** und werden nicht kopiert | verhindert widersprüchliche Werte zwischen Tokens, Kit, HTML, PDF und Kanälen |
| 3 | **HTML und PDF aus demselben Render-Durchlauf** (PDF = Druckansicht derselben HTML-Datei) | eine Quelle, kein Auseinanderlaufen |
| 4 | **Status-Vokabular aus v1.0 wiederverwendet:** `OPEN` · `ARBEITSFREIGABE` · `ENTSCHIEDEN`; Gesamtstatus des Kits `ENTWURF` oder `FREIGEGEBEN` | keine zweite Status-Logik. `FREIGEGEBEN` ist technisch unmöglich, solange ein Pflichtpunkt OPEN ist |
| 5 | **Brand Kit gehört zu Gate G4** („Tokens und Brand Kit“), keine neue Gate-Nummer | v1.0-Gates bleiben kompatibel |
| 6 | **Generator nur mit Python-Standardbibliothek + Chrome/Chromium (headless) für PDF/PNG**, kein Framework | reproduzierbar, keine Abhängigkeiten |
| 7 | **Plattformmaße und Rechtliches nur als Prüfpunkte mit „vor Produktion verifizieren“** | Plattformen und Recht ändern sich |
| 8 | **Demo nur unter `demo/`**, als fiktive Marke gekennzeichnet; Generator stempelt Demo-Ausgaben sichtbar | Demo-Werte dürfen nie als Core-Defaults oder reale Marke erscheinen |
| 9 | `templates/brand-guideline.md` bleibt das **Inhaltsmodell**; das Brand Kit ist seine erzeugte Form | keine Dopplung |

## 3. Testergebnisse

Siehe Abschnitt „Validierung“ in [`../brand-kit/README.md`](../brand-kit/README.md#8-validierung-v110) und den QA-Bericht der Demo unter `demo/`.
