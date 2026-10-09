# Cross-Channel: eine Marke in allen Kanälen (Core)

> Neu in Core **1.1.0**. Gemeinsame Regeln für alle Kanal-Templates. Die kanalspezifischen Details stehen in den jeweiligen Template-Dateien. Diese Datei wird dort referenziert und nicht wiederholt.
> **Plattformmaße, Dateigrenzen und rechtliche Anforderungen ändern sich.** Alle Angaben hier sind Prüfpunkte bzw. Richtwerte und müssen **vor jeder Produktion aktuell verifiziert** werden (offizielle Hilfe-Seiten der Plattform, fachkundige Rechtsprüfung).

## 1. Kanäle und Templates

| Kanal | Template (Regeln) | Starter (Ausgangsvorlage) |
|---|---|---|
| Website / Landingpage | [website-landingpage.md](website-landingpage.md) | `core/brand-kit/generator/starters/website.html` |
| Instagram Post, Story | [social-media.md](social-media.md#instagram) | `instagram-post.html`, `instagram-story.html` |
| Pinterest Pin | [social-media.md](social-media.md#pinterest) | `pinterest-pin.html` |
| LinkedIn Post, Carousel | [social-media.md](social-media.md#linkedin) | `linkedin-post.html`, `linkedin-carousel.html` |
| Newsletter, E-Mail | [newsletter-email.md](newsletter-email.md) | `newsletter.html` |
| Präsentation | [presentation.md](presentation.md) | `presentation.html` |
| PDF-Dokument, Angebot | [document.md](document.md) | `document-offer.html` |

## 2. Token-Zuordnung je Kanal

Alle Kanäle verwenden **dieselben semantischen Tokens** des Projekts. Unterschiede entstehen nur über Größe und Einheit, nie über andere Farben oder Schriften.

| Rolle | Token | Website/App | Social | Newsletter | Präsentation | Dokument |
|---|---|---|---|---|---|---|
| Hintergrund | `color.bg.canvas` / `color.bg.surface` | CSS-Variable | CSS-Variable → PNG | Inline-Wert | CSS-Variable → PDF | CSS-Variable → PDF |
| Markenfläche | `color.brand.primary` | Akzentflächen | Hauptfläche erlaubt | Kopf/CTA sparsam | Titelfolie | Linie, Akzent |
| Text | `color.text.*` | ✓ | ✓ (`text.inverse` auf Markenfläche) | Inline | ✓ | ✓ |
| Hauptaktion | `color.action.primary.*` | Button | CTA-Fläche | Button (Tabellen-Button) | — | — |
| Display-Schrift | `font.family.display` | Überschriften | Headline | Headline (mit Fallback!) | Titel | Titel |
| Lesetext | `font.family.body` | ✓ | ✓ | ✓ | ✓ | ✓ |
| Abstände | `space.*` | px → rem | px (feste Fläche) | px | px | pt/mm (Umrechnung dokumentieren) |
| Radius | `radius.*` | ✓ | ✓ | ✓ (eingeschränkt unterstützt) | ✓ | sparsam |

**Skalierung der Typografie:** Social-Grafiken und Folien werden in Pixeln der Zielfläche gesetzt (z. B. Headline auf einer 1080-px-Grafik). Die **Rollen und Verhältnisse** der Typo-Skala bleiben gleich, nur der Maßstab ändert sich. Kleinste Schrift auf Social-Grafiken: so groß, dass sie auf einem Smartphone ohne Zoom lesbar ist (Richtwert ≥ 24 px auf 1080 px Breite).

## 3. Logo- und CTA-Regeln (alle Kanäle)

- Nur **freigegebene** Logo-Varianten aus dem Brand Kit (`logos[]` mit Status `ENTSCHIEDEN`). Positiv auf hellen, Negativ auf dunklen bzw. Markenflächen.
- Schutzraum und Mindestgröße aus dem Brand Kit einhalten. Kein Verzerren, Umfärben, Schatten oder Freistellen auf unruhigen Bildern.
- **Eine Hauptaktion (CTA) pro Ausgabe**, benannt nach dem Ergebnis („Termin buchen“), gleicher Begriff in allen Kanälen ([content-writing.md](../principles/content-writing.md)).
- CTA-Darstellung nach `channels.<kanal>.cta_style` im Brand Kit.

## 4. Accessibility und Lesbarkeit (alle Kanäle)

- Kontrast nach [color.md](../tokens/color.md#3-kontrastregeln): Text ≥ 4.5:1, großer Text ≥ 3:1. Text auf Fotos nur mit gesicherter Fläche.
- Information nie nur über Farbe.
- **Alt-Text** für jede veröffentlichte Grafik (Plattformfeld nutzen), Untertitel für Videos, Transkript für Audio.
- Wichtiger Text gehört **in den Beitragstext** bzw. die E-Mail selbst, nicht nur in die Grafik.
- Emojis sparsam und nicht als Ersatz für Wörter; Hashtags in CamelCase, wo sinnvoll (Screenreader).

## 5. Pre-Production-Check (jeder Kanal)

- [ ] Brand-Kit-Version notiert, Kit ist `FREIGEGEBEN` (sonst als Entwurf kennzeichnen)
- [ ] nur Tokens, freigegebene Logos und freigegebene Bilder verwendet (QA-Konsistenzprüfung bestanden)
- [ ] keine `[OFFEN: …]`-Platzhalter mehr in der Ausgabe
- [ ] **aktuelle Plattformmaße, Sicherheitsbereiche und Dateigrenzen geprüft** (offizielle Quelle, Datum notieren)
- [ ] Text in der Grafik lesbar auf Smartphone-Größe
- [ ] Alt-Text bzw. Beschreibung vorbereitet
- [ ] Bildrechte und Einwilligungen abgebildeter Personen vorhanden
- [ ] **Werbekennzeichnung** geprüft (bezahlte Kooperation, Anzeige, Affiliate)
- [ ] **KI-generierte Bilder** gemäß Plattformregeln und Projektregel gekennzeichnet ([content-writing.md](../principles/content-writing.md#6-ki-erzeugte-und-ki-bearbeitete-inhalte-bedingt))
- [ ] rechtliche Pflichtangaben je Kanal geprüft (z. B. Anbieterkennzeichnung, Newsletter-Einwilligung und Abmeldung), fachkundig verifiziert
- [ ] Export geprüft: Format, Auflösung, Farbraum (sRGB für digital), Dateiname nach Konvention
- [ ] Freigabe zur Veröffentlichung (Gate **G6**)

## 6. Export und Dateinamen

`<projekt>_<kanal>_<thema>_<JJJJ-MM-TT>_v<n>.<ext>`, z. B. `acme_instagram-post_fruehjahr_2026-04-02_v1.png`. Exporte liegen in `projects/<p>/exports/` oder im Ausgabeordner des Generators, nie in `core/`.
