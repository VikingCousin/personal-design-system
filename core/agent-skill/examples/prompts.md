# Beispiel-Prompts und erwartetes Verhalten

## 1. Neues Projekt starten

> „Ich möchte ein neues Projekt ‚Anhängerverleih Müller‘ erstellen. Verwende mein Personal Design System.“

**Claude:**
1. liest `README.md`, `core/README.md`, `core/agent-skill/SKILL.md`
2. legt `projects/anhaengerverleih-mueller/` aus der Vorlage an
3. stellt die Kurzbrief-Fragen gebündelt (oder übernimmt einen mitgelieferten Brief)
4. schlägt vor: Tiefe S, Profil Standard, Einstieg „neue Marke“ oder „bestehende Marke“ (falls schon ein Logo existiert), Ergebnisse (Landingpage mit Reservierungsanfrage, Preisliste, Fahrzeugbeschriftung, Visitenkarte), restriktivstes Medium (Fahrzeugbeschriftung, Favicon)
5. **stoppt an G0/G1** und wartet

## 2. Nur eine Anwendung

> „Erstelle für Projekt X eine Präsentation für das Investorengespräch.“

**Claude:** prüft, ob Projekt X freigegebene Tokens und ein Präsentations-Template hat. Wenn ja: Präsentation nach `core/templates/presentation.md` mit Projekt-Tokens. Wenn nein: benennt die Lücke und schlägt den kürzesten Weg vor (z. B. Brand-Import der vorhandenen CI), statt Farben zu erfinden.

## 3. Tokens ableiten

> „Leite die Tokens für Projekt X ab.“

**Claude:** prüft, ob G3 erreicht ist. Falls ja: Primitives aus der gewählten Richtung, Pflicht-Tokens des Vertrags, Kontrastnachweis, Lizenzprüfung. Legt vor (G4). Falls nein: weist darauf hin, dass zuerst eine Richtung gewählt werden muss.

## 4. Core-Regel aufnehmen

> „Nimm die Regel ‚Preise immer inkl. MwSt.-Hinweis‘ in Core auf.“

**Claude:** prüft nach `process/promotion.md`. Ergebnis zum Beispiel: gilt für B2C und B2B unterschiedlich, deshalb als bedingte Regel in `templates/marketing-page.md` („MwSt.-Angabe je Zielgruppe klar kennzeichnen“). Schlägt Formulierung und Ort vor und setzt erst nach Freigabe um, mit CHANGELOG-Eintrag und PATCH/MINOR-Version.

## 5. „Mach einfach“

> „Mach einfach eine schöne Website für meinen Verleih, ich hab keine Zeit.“

**Claude:** arbeitet mit Tiefe S und maximaler Eigenständigkeit bei Arbeitsständen, legt aber Richtung und finale Farben trotzdem als **zwei kurze Optionen** zur Wahl vor (G3), statt selbst zu finalisieren. Veröffentlicht nichts ohne Freigabe (G6).
