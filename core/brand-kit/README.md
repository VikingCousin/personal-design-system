# Brand Kit (Core)

> Neu in Core **1.1.0**. Ein Brand Kit bündelt die freigegebene Identität eines Projekts so, dass Menschen und AI Agents sie in **jedem Kanal gleich** anwenden: Website, App, Social Media, Newsletter, Präsentation, Dokument.
> Core definiert den **Vertrag**, den **Generator** und die **Kanal-Starter**. Die Inhalte und Werte gehören immer dem Projekt. Core enthält keine Markenwerte.

## 1. Prinzip: eine Quelle, viele Ausgaben

```
projects/<p>/tokens/*.tokens.json   ← Werte (Farben, Schriften, Abstände …), freigegeben in G4
projects/<p>/brand-kit/brand-kit.json   ← Identität, Logos, Rollen, Regeln, Status, Kanalinhalte
            │
            ▼  core/brand-kit/generator/build_brand_kit.py
projects/<p>/brand-kit/dist/
├── brand.css          CSS-Variablen aus den Tokens (minimaler CSS-Adapter)
├── BRAND-KIT.html     visuelles Brand Portal (Navigation, Farbcodes zum Kopieren, responsive)
├── BRAND-KIT.pdf      Druckfassung DERSELBEN HTML-Datei (A4)
├── channels/          Kanal-Ausgaben aus den Core-Startern (HTML + PNG/PDF)
├── assets/            kopierte, freigegebene Assets
└── QA-REPORT.md       Prüfbericht
```

- **Werte stehen nur in den Token-Dateien.** `brand-kit.json` verweist auf Tokens (`"token": "color.brand.primary"`) und kopiert keine Werte. Damit können Tokens, HTML, PDF und Kanäle nicht auseinanderlaufen.
- **HTML und PDF** entstehen aus demselben Render-Durchlauf. Das PDF ist die Druckansicht der HTML-Datei.
- Inhaltlich folgt das Kit dem Inhaltsmodell [`templates/brand-guideline.md`](../templates/brand-guideline.md), das Brand Kit ist dessen erzeugte Form.
- Assets liegen im Projekt unter `assets/`; `brand-kit.json` verweist mit `../assets/…` darauf.
- `dist/` ist eine **Build-Ausgabe** und wird nie von Hand bearbeitet ([architecture.md](../tokens/architecture.md#4-dateien-im-projekt)).

## 2. Brand-Kit-Vertrag (`brand-kit.json`)

Vorlage: [`../process/project-template/brand-kit/brand-kit.json`](../process/project-template/brand-kit/brand-kit.json). Optional: `reference_assets[]` (weitere Referenzbilder mit Status, `ai_share`, `rights_cleared`). Pflichtabschnitte:

| Abschnitt | Inhalt | Quelle im Projekt |
|---|---|---|
| `meta` | Projekt, Name, **Version** (SemVer), **Gesamtstatus** `ENTWURF` / `FREIGEGEBEN`, `approved_by`, `approved_at`, Core-Version, Sprache, Datum, `demo` | `DECISIONS.md` |
| `tokens` | Pfade zu den Token-Dateien (und optional Dunkelmodus) | `tokens/` |
| `identity` | Ein-Satz-Idee, Positionierung, Markenwerte, Persönlichkeit (ist / ist nicht), Verweis auf die Quelle | `brand/foundation.md` |
| `logos[]` | je Variante: `id`, Name, Variante (primary, negative, mark, mono …), Hintergrund, Datei, Alt-Text, Mindestgröße digital/Druck, Schutzraum, Status, für den KI-Export `ai_share` und `rights_cleared` | `assets/logos/` |
| `colors[]` | Farbrollen als **Token-Verweis**, Name, Rolle (brand, ui, feedback, material, data), Verwendung, optional Druckwerte (CMYK, RAL, Pantone als Näherung), Status | `tokens/` |
| `contrast_pairs[]` | Paare aus Vordergrund- und Hintergrund-Token mit Mindestwert | [color.md](../tokens/color.md#3-kontrastregeln) |
| `typography` | Familien als Token-Verweis mit Name, Fallback, **Lizenz** und Lizenzstatus, Liste der Textstile, Beispielsatz | [typography.md](../tokens/typography.md) |
| `layout` | Raster und Formen in Worten, Auswahl an Abstands- und Radius-Tokens | `tokens/` |
| `imagery` | `photography`, `icons`, `illustration`: Beschreibung, Do, Don't, Status | `brand/visual-direction.md` |
| `voice` | Zusammenfassung, Anrede-Regel, Schreibprinzipien, Wörter verwenden/vermeiden, Beispiele je Kontext, Quelle | `brand/voice.md` |
| `ui` | Status der UI-Grundelemente, Beispiel-Beschriftungen | `components/` |
| `do_dont[]` | Thema, Do, Don't, Status | — |
| `channels` | je Kanal: Status, Logo-Variante, CTA-Stil, Regeln, `sample` (Beispielinhalt für den Starter) | [cross-channel.md](../templates/cross-channel.md) |

**Statuswerte** (aus [documentation.md](../principles/documentation.md#2-entscheidungsstatus), keine neue Logik):
- je Abschnitt bzw. Eintrag: `OPEN` · `ARBEITSFREIGABE` · `ENTSCHIEDEN`
- Gesamtstatus des Kits: `ENTWURF` · `FREIGEGEBEN`

## 3. Regeln für offene und fehlende Inhalte

1. **Fehlende Assets und unentschiedene Werte werden als `OPEN` gekennzeichnet.** Sie erscheinen in HTML, PDF und Kanälen sichtbar als **„OFFEN“** und werden in „Offene Punkte“ und im QA-Bericht gelistet.
2. **Nichts Offenes wird als freigegeben ausgegeben.** Der Generator meldet einen **Fehler**, wenn …
   - das Kit `FREIGEGEBEN` ist, aber ein Eintrag nicht `ENTSCHIEDEN` ist,
   - `FREIGEGEBEN` ohne `approved_by` / `approved_at` gesetzt ist,
   - ein als `ENTSCHIEDEN` markiertes Logo keine Datei hat,
   - ein Demo-Kit (`meta.demo: true`) als `FREIGEGEBEN` markiert ist.
3. **Fehlende Kanalinhalte** (z. B. Impressum im Newsletter) werden im Kanal als `[OFFEN: …]` sichtbar gemacht, nie still weggelassen und nie erfunden.
4. Nur der Nutzer setzt `ENTSCHIEDEN` bzw. `FREIGEGEBEN` (Gate G4, [approval-gates.md](../agent-skill/rules/approval-gates.md)).

## 4. Generator

```bash
python3 core/brand-kit/generator/build_brand_kit.py projects/<name>/brand-kit/brand-kit.json
```

- Nur Python-Standardbibliothek. PDF- und PNG-Export brauchen **Chrome oder Chromium** (headless). Pfad automatisch oder per `--chrome` bzw. Umgebungsvariable `CHROME_PATH`. `--no-export` erzeugt nur HTML/CSS.
- **Exit-Code 1**, wenn die QA Fehler findet. Die Ausgaben werden trotzdem erzeugt, aber im Portal als „QA fehlgeschlagen“ markiert.

**Automatische Prüfungen (QA-REPORT.md)**

| Prüfung | Ergebnis bei Problem |
|---|---|
| Pflichtfelder und Statuswerte vorhanden | Fehler |
| Freigabestatus widerspruchsfrei (s. §3) | Fehler |
| Token-Vertrag vollständig (`contract.tokens.json`) | Warnung im Entwurf, Fehler bei Freigabe |
| alle Token-Verweise auflösbar | Fehler |
| alle Farbrollen sind gültige HEX-Tokens | Fehler |
| Kontrastpaare erfüllen den Mindestwert | Fehler |
| Logo-Dateien vorhanden | Fehler bei freigegebenem Logo, sonst OFFEN |
| **Konsistenz:** Kanal-Ausgaben, `brand.css` und SVG-Assets enthalten nur Farben und Schriften aus den Tokens | Fehler |
| Seitenzahl der PDFs (Brand Kit ≥ 3, Starter mit `pds:pages`) | Fehler |
| unbekannte Platzhalter in Startern | Fehler |

Was der Generator **nicht** prüft: Bildrechte, Lizenzverträge, rechtliche Pflichtangaben, aktuelle Plattformmaße, inhaltliche Qualität. Diese Punkte stehen als Checkliste in [cross-channel.md](../templates/cross-channel.md#5-pre-production-check-jeder-kanal).

## 5. Kanal-Starter

Wiederverwendbare, markenneutrale Ausgangsvorlagen in [`generator/starters/`](generator/starters/). Sie verwenden **ausschließlich** Tokens (über `brand.css` bzw. Inline-Token-Werte im Newsletter) und Inhalte aus `brand-kit.json`.

| Kanal (`channels.<key>`) | Starter | Export |
|---|---|---|
| `website` | `website.html` | HTML |
| `instagram_post` | `instagram-post.html` | PNG |
| `instagram_story` | `instagram-story.html` | PNG |
| `pinterest_pin` | `pinterest-pin.html` | PNG |
| `linkedin_post` | `linkedin-post.html` | PNG |
| `linkedin_carousel` | `linkedin-carousel.html` | PDF |
| `newsletter` | `newsletter.html` | HTML (Inline-Werte) |
| `presentation` | `presentation.html` | PDF |
| `document` | `document-offer.html` | PDF (A4) |

**Platzhalter:** `{{kit:pfad}}` Inhalt (fehlt → OFFEN) · `{{opt:pfad}}` optionaler Inhalt · `{{token:pfad}}` aufgelöster Token-Wert · `{{logo:variante}}` · `{{css}}` · `{{demo_banner}}`. Formatangaben (`pds:size`, `pds:pages`) stehen als Kommentar im Starter und sind **Richtwerte, die vor Produktion verifiziert werden müssen**.

**Erweitern:** Projekte kopieren einen Starter nach `projects/<p>/templates/` und passen Layout und Inhalt an. Die Regeln bleiben: nur Tokens, nur freigegebene Assets, keine festen Farben oder Schriften.

## 6. Ablauf im Projekt

| Situation | Vorgehen |
|---|---|
| **Neue Marke** | Nach G3 (Richtung) und den Tokens: `brand-kit.json` aus der Vorlage anlegen, füllen, generieren, QA prüfen, mit G4 („Tokens und Brand Kit“) freigeben lassen |
| **Bestehende Marke (Brand-Import)** | Vorhandenes CI-Material erfassen: Logos nach `assets/`, Farben und Schriften als Tokens, Regeln ins Kit. Jeder importierte Wert bekommt die Quelle (`source`) und den Status `ARBEITSFREIGABE`, bis der Nutzer ihn bestätigt. Probleme (z. B. zu geringer Kontrast) werden gemeldet, nicht still korrigiert |
| **Projekt ohne Brand Kit** | Kanalaufträge (z. B. „Pinterest Pin für Projekt X“) werden **nicht** mit erfundener Identität erledigt. Claude bietet an: Brand Kit aufbauen bzw. importieren, oder einen klar als **Entwurf ohne Markenidentität** gekennzeichneten Strukturentwurf |
| **Kit-Update** | Version erhöhen (PATCH: Korrektur; MINOR: neue Kanäle, Assets; MAJOR: neue Markenwerte bzw. Identität), neu generieren, Freigabe in `DECISIONS.md` |

## 7. AI Brand Context Pack (Export für ChatGPT, Claude, Gemini …)

Exportiert die Markenregeln **eines** Projekts für externe KI-Tools, z. B. für Profilbilder, Social-Grafiken, Newsletter, Websites, Präsentationen und Dokumente. Quelle ist ausschließlich das Brand Kit dieses Projekts. Es gibt keine zweite Markenlogik: Validierung, Token-Auflösung und Status stammen aus dem Generator.

```bash
python3 core/brand-kit/generator/build_brand_kit.py projects/<name>/brand-kit/brand-kit.json     # zuerst: Brand Kit + PDF
python3 core/brand-kit/generator/export_ai_context.py projects/<name>/brand-kit/brand-kit.json   # dann: Paket
```

| Datei in `ai-pack/` | Inhalt | Hochladen? |
|---|---|---|
| `AI-BRAND-CONTEXT.md` | Anweisungen für das Modell, Positionierung, Werte, Farben (HEX/RGB), Typografie, Logo-Verwendung, Bildsprache, Tonalität, Do/Don't, Kanäle, offene Punkte, Status, Version | **ja** |
| `brand-tokens.json` | aufgelöste Design Tokens (DTCG-Format) mit Status | ja (für Web, Newsletter, Präsentation) |
| `BRAND-KIT.pdf` | visuelle Referenz, nur wenn aktuell (gleiche Version) und ohne Prüfbefund | optional |
| `assets/` | **nur** Assets mit `status: ENTSCHIEDEN`, `ai_share: true`, `rights_cleared: true` | nur bei Bedarf |
| `CHATGPT-IMAGE-PROMPT.md` | wiederverwendbarer Bildprompt mit Markenregeln | nein, zum Kopieren |
| `README.md`, `MANIFEST.json`, `EXPORT-CHECK.md` | Anleitung, Version und Prüfsummen, Prüfbericht | nein |

**Regeln**
- **Keine fiktiven Freigaben.** Der Status kommt aus dem Brand Kit: `FREIGEGEBEN` nur, wenn das Kit freigegeben ist und die QA keine Fehler hat, sonst `ENTWURF`. Demo-Kits sind immer `DEMO`. Offenes steht als **OFFEN** im Paket.
- **Kein Brand Kit vorhanden** → nur eine als ENTWURF/VORLAGE markierte Datei, keine erfundenen Inhalte.
- **Nie exportiert:** Kanal-Beispielinhalte (können Adressen und Impressum enthalten), Quellverweise auf interne Dateien, die freigebende Person, Brief, Research, Entscheidungslog und andere Projekte.
- **Automatische Prüfung** aller Paketdateien auf E-Mail-Adressen, Telefonnummern, IBAN, lokale und interne Pfade, Secrets, Vertraulichkeitsvermerke und Namen anderer Projekte. Bei einem Fund: Ergebnis „NICHT WEITERGEBEN“, Exit-Code 1.
- **Manuell zu prüfen:** Rechte an Assets und Schriften für die Nutzung in KI-Tools, ob die Positionierung schon öffentlich sein darf, Bildinhalte im PDF, Bedingungen des KI-Dienstes.
- **Keine automatische Veröffentlichung.** Das Hochladen in einen externen Dienst ist eine Weitergabe im Sinne von Gate **G6** und braucht die Freigabe des Nutzers.
- `ai-pack/` wird nicht versioniert (`.gitignore`), sondern bei Bedarf neu erzeugt.

**Versionen synchron halten:** Quelle bleibt `brand-kit.json`. Nach jeder Änderung Brand Kit und Paket neu erzeugen, im KI-Tool alle Dateien der alten Version löschen und die neuen hochladen. Die Version steht in jeder Datei und in `MANIFEST.json` (mit Prüfsummen).

## 8. Validierung v1.1.0

Automatisierte Tests: `python3 -m unittest discover -s core/brand-kit/tests -v` (ohne Chrome; der Export-Test mit Chrome läuft, wenn Chrome vorhanden ist).


Getestet mit der fiktiven Demo-Marke unter [`../../demo/radhof-demo/`](../../demo/radhof-demo/README.md). Ergebnisse: [`../decisions/0005-test-v1-1.md`](../decisions/0005-test-v1-1.md).
