# Qualitätsstandards (Core)

> Checklisten, mit denen jede Phase und jedes Artefakt geprüft wird. Claude führt diese Prüfungen selbst durch und berichtet das Ergebnis, bevor etwas als fertig gemeldet wird.

## 1. Allgemeine Qualitätskriterien

Jedes Artefakt eines Projekts (Token-Datei, Komponente, Template, Seite, Dokument) ist erst fertig, wenn:

- [ ] es auf Core-Regeln aufbaut oder die Abweichung dokumentiert ist,
- [ ] keine Werte hart kodiert sind, für die ein Token existiert oder existieren sollte,
- [ ] es die [Accessibility-Baseline](accessibility.md) erfüllt,
- [ ] es bei den [Prüfbreiten](responsive.md#prüfbreiten) funktioniert (falls digital),
- [ ] Texte den [Content-Regeln](content-writing.md) folgen,
- [ ] Logos, Icons und Bilder den [Asset-Regeln](visual-assets.md) folgen,
- [ ] Platzhalter als Platzhalter gekennzeichnet sind,
- [ ] seine Entscheidungen nachvollziehbar dokumentiert sind ([documentation.md](documentation.md)).

## 2. Checklisten je Phase

### Brief
- [ ] Ziel, Zielgruppen, Angebot, Kanäle und Medien sind erfasst
- [ ] Accessibility-Profil gewählt
- [ ] Prozess-Tiefe gewählt ([project-workflow.md](../process/project-workflow.md#2-prozess-tiefe))
- [ ] Widersprüche und Lücken als OPEN dokumentiert

### Brand Foundation
- [ ] Markenidee, Positionierung, Persönlichkeit, Voice (inkl. Kontext-Matrix und Anrede-Regel) vorhanden
- [ ] Jede Aussage als FAKT / ABLEITUNG / ANNAHME / OFFEN gekennzeichnet
- [ ] Vom Nutzer freigegeben (Gate G2)

### Creative Direction
- [ ] Bewertungskriterien und Gewichtung **vor** dem Sichten festgelegt
- [ ] Alle Richtungen zeigen dieselben Proben mit demselben Beispielinhalt
- [ ] Das restriktivste Medium des Projekts ist geprüft
- [ ] Explorationswerte als „Arbeitswerte“ gekennzeichnet, nicht als Tokens
- [ ] Keine Richtung entscheidet offene Strategiefragen implizit
- [ ] Die Auswahl trifft der Nutzer (Gate G3)

### Tokens
- [ ] Alle Pflicht-Tokens des [Vertrags](../tokens/contract.tokens.json) haben Werte
- [ ] Komponenten verweisen nur auf semantic bzw. component tokens
- [ ] Kontrastpaare geprüft und dokumentiert (Light **und** ggf. Dark)
- [ ] Farbangaben enthalten HEX und OKLCH, bei Print oder Physisch zusätzlich CMYK bzw. RAL/Pantone als gekennzeichnete Näherung
- [ ] Schriftlizenzen für alle Medien geprüft

### Components
- [ ] Spezifikation nach [Spec-Vorlage](../components/_spec-template.md)
- [ ] Alle relevanten Zustände definiert
- [ ] Tastaturbedienung und Screenreader-Verhalten beschrieben und getestet
- [ ] Zielgröße, Fokus und Kontrast geprüft

### Templates
- [ ] Überschriftenhierarchie und Landmarks korrekt
- [ ] Reflow bei 320 px, Zoom 200 %
- [ ] Nur Komponenten und Tokens des Projekts verwendet
- [ ] Performance: Bilder optimiert, höchstens 2 Schriftfamilien plus optional eine Mono, Schriften mit `font-display: swap`

## 3. Release-Check (digitale Anwendung)

- [ ] Tastatur: vollständiger Durchlauf ohne Maus
- [ ] Screenreader-Stichprobe (VoiceOver oder NVDA) für Hauptabläufe
- [ ] Automatischer Test (z. B. axe, Lighthouse) ohne kritische Fehler
- [ ] `prefers-reduced-motion` und ggf. Dark Mode geprüft
- [ ] Fehler-, Leer- und Ladezustände vorhanden
- [ ] Formulare mit echten Fehlerfällen getestet
- [ ] Rechtliche Pflichtangaben (Impressum, Datenschutz) vom Projekt geklärt, sofern relevant

## 4. Was nie als „fertig“ gemeldet wird

- Entwürfe mit ungeprüften Kontrasten
- Komponenten ohne Fokus-Zustand
- Seiten, die bei 320 px horizontal scrollen
- Designs, deren Markenentscheidungen nicht vom Nutzer freigegeben sind (sie heißen dann „Entwurf“ oder „Exploration“)
