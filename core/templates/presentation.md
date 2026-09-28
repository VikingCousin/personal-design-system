# Template: Präsentation (Core)

## Zweck
Folien, die einen Vortrag unterstützen oder allein gelesen werden (Pitch, Workshop, Report). Format 16:9, Ausgabe als PPTX, PDF oder Online-Slides.

## Folientypen

| Typ | Pflicht? | Inhalt |
|---|---|---|
| Titel | Pflicht | Titel, Untertitel, Datum, Vortragende/r |
| Agenda | ab ca. 10 Folien | Kapitel, Position anzeigen |
| Kapiteltrenner | optional | Kapitelnummer und -titel |
| Kernaussage | häufig | **eine** Aussage als Satz, groß |
| Inhalt mit Text | häufig | Überschrift als Aussage + max. ca. 5 Punkte |
| Bild bzw. Beleg | optional | großes Bild oder Screenshot + Aussage |
| Daten | optional | ein Diagramm mit einer Botschaft in der Überschrift, Quelle |
| Vergleich | optional | 2–3 Spalten oder Tabelle |
| Zitat | optional | Zitat mit Quelle (echt) |
| Abschluss | Pflicht | Zusammenfassung bzw. nächster Schritt, Kontakt |

## Qualitätsregeln
- **Überschrift = Aussage** („Buchungen am Wochenende verdoppelt“), nicht Thema („Buchungen“).
- **Eine Botschaft pro Folie.**
- **Lesbarkeit:** Fließtext ≥ 18 pt (Vortrag ≥ 24 pt), Kontrast wie digital; nichts Wichtiges in den äußeren 5 % (Beamer-Ränder).
- **Raster und Ränder** auf allen Folien gleich (Folienmaster verwenden, keine frei platzierten Textfelder).
- **Diagramme:** direkt beschriftet statt Legende, Reihen nicht nur farblich unterschieden, Quelle angegeben.
- **Barrierefreiheit:** Folientitel gesetzt (auch wenn visuell versteckt), Lesereihenfolge geprüft, Alt-Texte, Untertitel bei Video.
- **Bewegung:** keine dekorativen Animationen; Einblendungen nur, wenn sie das Erzählen unterstützen.

## Komponenten und Tokens
Farb- und Typo-Tokens des Projekts, übersetzt in Folienmaster und Designfarben (PPTX-Theme); `color.data.*` für Diagramme.

## Was das Projekt festlegt
Folienmaster, Titel- und Abschlussfolie, Bildsprache, Diagrammstil, ob Speaker Notes Pflicht sind.
