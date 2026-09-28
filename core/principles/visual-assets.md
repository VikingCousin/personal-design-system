# Visuelle Assets: Logo, Icons, Bilder, Illustration (Core)

> Ergänzt nach dem Smoke Test v1.0 ([0003](../decisions/0003-smoke-test-v1.md)). Core legt Regeln fest, keinen Stil. Motive, Bildsprache und Icon-Charakter bestimmt das Projekt.

## 1. Logo und Markenzeichen

- Jedes Logo hat definierte Varianten (z. B. horizontal, gestapelt, Bildzeichen), eine **positive und eine negative** Fassung und eine **einfarbige** Fassung.
- **Schutzraum** und **Mindestgröße** werden je Variante festgelegt, digital (px) und im Druck (mm).
- Das Logo funktioniert im **restriktivsten Medium** des Projekts (z. B. Favicon 16 px, Stempel, Stickerei, Fahrzeug aus Distanz).
- Logos werden als Vektor (SVG, PDF) abgelegt, Dateinamen nach [Projektvorlage](../process/project-template/assets/README.md).
- Das Logo ist ein Bild mit Alt-Text (Markenname), als Link zur Startseite mit zugänglichem Namen.

## 2. Icons

- **Ein** Icon-Set pro Projekt (einheitliche Strichstärke, Ecken, Füllung, Raster). Ergänzungen im Stil des Sets.
- Größen nur aus `size.icon.*`; Icons sitzen optisch auf der Grundlinie bzw. mittig zum Text.
- **Bedeutungstragende Icons** haben einen Text daneben oder einen zugänglichen Namen und ≥ 3:1 Kontrast. **Dekorative Icons** sind `aria-hidden`.
- Status nie nur über ein Icon **oder** nur über Farbe, sondern mindestens über zwei Merkmale bzw. Text.
- Allgemein verständliche Metaphern bevorzugen (Suche, Schließen, Menü). Eigenwillige Icons brauchen ein Label.

## 3. Fotografie und Bilder

- Jedes informative Bild hat einen **Alt-Text**, der den Zweck beschreibt; dekorative Bilder `alt=""`.
- **Keine erfundene Echtheit:** Stockfotos werden nicht als Kunden, Team oder Referenz ausgegeben. KI-generierte Bilder werden nicht als dokumentarische Fotos ausgegeben ([content-writing.md](content-writing.md#6-ki-erzeugte-und-ki-bearbeitete-inhalte-bedingt)).
- **Rechte** (Lizenz, Einwilligung abgebildeter Personen) sind geklärt und im Projekt dokumentiert.
- **Seitenverhältnisse** werden vom Projekt als kleiner Satz festgelegt (z. B. 16:9, 4:3, 1:1). Bildbereiche reservieren ihren Platz (keine Layout-Sprünge).
- **Performance:** moderne Formate (AVIF, WebP) mit Fallback, responsive Größen (`srcset`), Lazy Loading unterhalb des ersten Bildschirms.
- Text auf Bildern nur mit gesichertem Kontrast (Fläche oder Verlauf hinter dem Text), nie wichtige Information nur im Bild.

## 4. Illustration und Grafik

- Illustrationen folgen einem definierten Stil des Projekts; gemischte Stile nur bewusst.
- Diagramme und Infografiken haben eine Textalternative bzw. Datentabelle ([color.md](../tokens/color.md#7-datenvisualisierung)).

## 5. Ablage

Assets liegen in `projects/<p>/assets/` (`logos/`, `icons/`, `fonts/`, `images/`), niemals in `core/`.
