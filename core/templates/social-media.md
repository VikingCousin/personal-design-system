# Template: Social Media (Core)

> Neu in Core **1.1.0**. Gemeinsame Regeln (Tokens, Logo, CTA, Accessibility, Pre-Production-Check, Export): [cross-channel.md](cross-channel.md).
> **Formatangaben sind Richtwerte (Stand Oktober 2026) und müssen vor jeder Produktion bei der Plattform verifiziert werden.**

## Grundstruktur jeder Social-Grafik

```
[optional: Kennzeichnung, z. B. „Anzeige“]
[Eyebrow / Thema]
[Headline: eine Aussage]
[Kurztext: höchstens 1–2 Sätze]
[CTA]
[Logo · URL bzw. Absender]
```

- **Eine Aussage pro Grafik.** Höchstens drei Textebenen (Eyebrow, Headline, Kurztext).
- **Text in der Grafik ≠ Beitragstext.** Die vollständige Information steht im Beitragstext, die Grafik ist der Aufhänger.
- **Bildfläche** nur mit freigegebener Bildsprache (Brand Kit `imagery.photography`). Text auf Fotos nur mit gesicherter Kontrastfläche.
- **Logo** klein und konsistent an derselben Position, nicht als Hauptmotiv (außer bei Markenkampagnen).

## Instagram

| Format | Starter | Richtwert (verifizieren) | Besonderheiten |
|---|---|---|---|
| Post | `instagram-post.html` | Hochformat 4:5 (z. B. 1080 × 1350 px), auch 1:1 | Vorschau im Profilraster kann beschnitten werden: Wichtiges mittig |
| Story / Reel-Cover | `instagram-story.html` | 9:16 (z. B. 1080 × 1920 px) | **Sicherheitsbereiche** oben und unten frei lassen (Plattform-UI), Starter reserviert sie |
| Carousel | wie Post, mehrere Grafiken | 4:5 bzw. 1:1, einheitlich | erste Grafik = Aufhänger, letzte = CTA |

## Pinterest

| Format | Starter | Richtwert (verifizieren) | Besonderheiten |
|---|---|---|---|
| Pin | `pinterest-pin.html` | Hochformat 2:3 (z. B. 1000 × 1500 px) | Pins sind Suchinhalte: Headline als konkrete Lösung („Kette ölen in 3 Schritten“), Ziel-URL Pflicht, Bild oben, Text unten |

## LinkedIn

| Format | Starter | Richtwert (verifizieren) | Besonderheiten |
|---|---|---|---|
| Post-Grafik | `linkedin-post.html` | 1:1 (z. B. 1200 × 1200 px) oder 4:5 | sachlicher Ton laut Kontext-Matrix des Projekts |
| Carousel (Dokument) | `linkedin-carousel.html` | PDF, mehrere Seiten 4:5 oder 1:1 | Seitenzahl sichtbar, eine Aussage pro Seite, letzte Seite CTA |

## Token-Zuordnung (Social)

| Element | Token |
|---|---|
| Hauptfläche | `color.brand.primary` oder `color.bg.inverse`, alternativ `color.bg.canvas` |
| Text auf Markenfläche | `color.text.inverse` (Kontrast prüfen!) |
| CTA | `color.bg.canvas` + `color.text.primary` auf Markenfläche bzw. `color.action.primary.*` auf heller Fläche |
| Headline | `font.family.display`, Größe aus der Typo-Skala im Maßstab der Grafik |
| Abstände, Radien | `space.*`, `radius.control` |

## Accessibility und Compliance (zusätzlich zu cross-channel.md)

- Alt-Text im Plattformfeld; Text der Grafik im Beitragstext wiederholen.
- Videos: Untertitel eingebrannt **oder** als Datei; kein Ton als einzige Information.
- **Werbekennzeichnung** sichtbar und eindeutig (Wortlaut und Pflicht nach geltendem Recht und Plattformregeln prüfen).
- Gewinnspiele, Rabatte, Preisangaben: Bedingungen und Pflichtangaben prüfen.
- Anbieterkennzeichnung des Profils (je nach Land und Nutzung) prüfen.

## Qualitätsprüfung vor Export

- [ ] Starter-Ausgabe ohne `[OFFEN: …]`
- [ ] Lesbarkeit in Smartphone-Vorschau (Grafik auf ca. 360 px Breite verkleinert ansehen)
- [ ] aktuelle Maße und Sicherheitsbereiche verifiziert
- [ ] PNG in sRGB, Dateiname nach [Konvention](cross-channel.md#6-export-und-dateinamen)
