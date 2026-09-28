# Methode: Creative Directions entwickeln und vergleichen (Core)

> Wie visuelle Richtungen für eine neue oder grundlegend überarbeitete Marke entstehen. Beginnt erst nach G2 (Brand Foundation freigegeben). Endet mit der Wahl durch den Nutzer (G3).

## 1. Vorbereitung (vor jedem Entwurf)

1. **Designprobleme benennen:** Welche Spannungen muss die Gestaltung lösen (z. B. „günstig, aber nicht billig“, „technisch, aber menschlich“)?
2. **Restriktivstes Medium bestimmen:** Das Medium mit den härtesten Bedingungen wird zuerst geprüft (z. B. Favicon, Fahrzeugbeschriftung, Stempel, Stickerei, Gravur, Schwarz-Weiß-Fax). Was dort nicht funktioniert, trägt keine Identität.
3. **Stress-Test-Szenarien festlegen:** 6–12 konkrete Situationen aus dem echten Projekt, an denen jede Richtung gezeigt wird (z. B. Hero, Formular, Fehlermeldung, Rechnung, Schild aus 20 m).
4. **Bewertungskriterien und Gewichtung festlegen, bevor Entwürfe gesichtet werden**, damit die Bewertung nicht nachträglich zur Lieblingsrichtung passt. Dazu K.o.-Kriterien (mindestens: Accessibility erreichbar, restriktivstes Medium funktioniert, keine Tabus des Projekts).
5. **Offene Strategieentscheidungen prüfen:** Ist eine strategische Frage OPEN (z. B. Zielgruppe A oder B zuerst), müssen alle Richtungen an Szenarien **aller** Kandidaten gezeigt werden. Keine Richtung entscheidet die Frage implizit.

## 2. Entwicklung

- **Echte Alternativen:** Die Richtungen unterscheiden sich auf mindestens zwei grundlegenden Achsen (Referenzwelt, Temperatur, Materialität, Energie, Verhältnis zum Inhalt), nicht nur in der Farbe.
- **Pro Richtung dokumentieren:** Leitidee · emotionaler Charakter · visuelle Sprache · typografische Richtung · Farbrichtung · Bildsprache · Übersetzung in alle Medien des Projekts · Umgang mit Status- bzw. Kennzeichnungssystemen des Projekts · Eignung für die Zielgruppen · Risiken · was sie bewusst nicht ist.
- **Standard-Look vermeiden:** Richtungen, die wie ein beliebiger Default aussehen (austauschbare SaaS-Optik, generische Stock-Welt), werden überarbeitet.

## 3. Style-Tiles (Vergleichsformat)

- Jede Richtung wird mit **denselben Proben** und **demselben Beispielinhalt** gezeigt (z. B. Hero, Karte, Formularfeld mit Fehler, Status-Kennzeichnung, restriktivstes Medium, Farbwelt, Typo-Hierarchie, Bildrichtung).
- Style-Tiles liegen in `projects/<p>/prototypes/` und sind als **Exploration** gekennzeichnet.
- Sie halten die Accessibility-Untergrenze ein (Profilwerte für Schrift, Zielgröße ≥ 44 px, sichtbarer Fokus, Kontrast, reduzierte Bewegung). Ein Dunkelmodus wird nur gezeigt, wenn das Projekt einen plant.
- **Explorationswerte ≠ Tokens:** Farben heißen „Arbeitswerte“, Schriften „Probeschriften“. Sie werden erst nach G3 geprüft und in Tokens überführt.

## 4. Bewertung

- K.o.-Kriterien zuerst, dann die gewichteten Kriterien nach Prioritätsstufen.
- Keine Gesamtsumme, kein vorgeschlagener Gewinner, außer der Nutzer bittet darum. Stattdessen: Stärken, Schwächen, K.o.-Risiken, Trade-offs.
- Designhypothesen („wirkt vertrauenswürdig für …“) werden als solche gekennzeichnet und, wo es darauf ankommt, mit Nutzenden getestet.

## 5. Entscheidung (G3)

Der Nutzer wählt eine Richtung, eine Kombination oder verlangt eine Überarbeitung. Claude dokumentiert die Entscheidung in `DECISIONS.md` und überführt die Richtung in `brand/visual-direction.md`. Erst danach beginnen die Tokens.
