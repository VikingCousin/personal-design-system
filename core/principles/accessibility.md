# Accessibility (Core)

> **Baseline: WCAG 2.2, Konformitätsstufe AA.** Gilt für jedes Projekt und jedes Medium, das es betrifft.
> Projekte dürfen verschärfen (z. B. Profil „Erweitert“, AAA-Kontrast), **nie absenken**. Accessibility ist nie ein Premium-Feature einzelner Angebotsstufen.
> Hinweis: Diese Datei fasst Arbeitsregeln zusammen. Rechtliche Pflichten (z. B. nationale Umsetzung des European Accessibility Act) prüft das Projekt gesondert.

## 1. Profile

| Profil | Wann | Unterschiede zum Standard |
|---|---|---|
| **Standard** | Default für jedes Projekt | Werte in dieser Datei |
| **Erweitert** | Zielgruppe mit häufig eingeschränktem Sehen, Hören oder eingeschränkter Motorik (z. B. ältere Menschen), öffentliche Einrichtungen, Gesundheit | Fließtext ≥ 18–20 px, Touch-Targets ≥ 48 px, Textkontrast Ziel 7:1 (AAA) für Fließtext, großzügigere Zeilenhöhe, keine zeitgesteuerten Inhalte |

Das Projekt wählt das Profil im Bootstrap (`README.md` des Projekts) und begründet es.

## 2. Wahrnehmbar

| Regel | Standard | Referenz |
|---|---|---|
| Textkontrast | ≥ 4.5:1, großer Text (≥ 24 px bzw. ≥ 18.66 px fett) ≥ 3:1 | WCAG 1.4.3 |
| Kontrast von UI-Elementen und Grafiken | Rahmen von Eingabefeldern, Icons mit Bedeutung, Fokusrahmen ≥ 3:1 gegen die Umgebung | WCAG 1.4.11 |
| Nicht nur Farbe | Status, Fehler, Auswahl, Kategorien und Kennzeichnungen immer zusätzlich über Text, Form, Icon oder Muster | WCAG 1.4.1 |
| Textgröße | Fließtext ≥ 16 px. Kein Text unter 12 px. Hilfstexte und Captions ≥ 14 px empfohlen | Core |
| Zoom und Reflow | Nutzbar bei 200 % Zoom und bei 320 px Breite ohne horizontales Scrollen (außer Tabellen, Karten, Diagramme) | WCAG 1.4.4, 1.4.10 |
| Textabstände | Layout bricht nicht, wenn Nutzende Zeilen- und Buchstabenabstand erhöhen | WCAG 1.4.12 |
| Alternativtexte | Informative Bilder haben Alt-Text, dekorative Bilder `alt=""` | WCAG 1.1.1 |
| Medien | Videos mit Untertiteln, Audio mit Transkript, keine Autoplay-Tonspur | WCAG 1.2 |

## 3. Bedienbar

| Regel | Standard | Referenz |
|---|---|---|
| Tastatur | Alles, was mit der Maus geht, geht mit der Tastatur. Keine Tastaturfallen | WCAG 2.1.1, 2.1.2 |
| Sichtbarer Fokus | Immer sichtbar, ≥ 2 px, Kontrast ≥ 3:1, nicht von Sticky-Elementen verdeckt | WCAG 2.4.7, 2.4.11 |
| Fokusreihenfolge | folgt der visuellen und logischen Reihenfolge | WCAG 2.4.3 |
| Zielgrößen | **Touch: ≥ 44 × 44 px.** Rein zeigergesteuerte, dichte Oberflächen (z. B. Tabellen in Desktop-Software): mindestens 24 × 24 px bzw. ausreichend Abstand | WCAG 2.5.8 (AA), 2.5.5 (AAA) |
| Keine reinen Gesten | Ziehen, Wischen und Mehrfinger-Gesten haben immer eine Alternative mit Einzelklick | WCAG 2.5.1, 2.5.7 |
| Zeit | Keine Zeitlimits ohne Verlängerung. Bewegte Inhalte > 5 s lassen sich pausieren | WCAG 2.2.1, 2.2.2 |
| Bewegung | `prefers-reduced-motion` wird respektiert. Keine blinkenden Inhalte > 3×/s | WCAG 2.3.1, 2.3.3 |
| Sprunglinks und Überschriften | „Zum Inhalt springen“ bei wiederkehrender Navigation; logische Überschriftenhierarchie | WCAG 2.4.1, 2.4.6 |

## 4. Verständlich

| Regel | Standard | Referenz |
|---|---|---|
| Sprache | `lang` gesetzt; fremdsprachige Passagen ausgezeichnet | WCAG 3.1 |
| Formulare | sichtbare Labels (nicht nur Platzhalter), Pflichtfelder gekennzeichnet, Fehler als Text beim Feld mit Lösungshinweis | WCAG 3.3.1–3.3.3 |
| Keine Doppeleingaben | bereits eingegebene Daten nicht erneut abfragen | WCAG 3.3.7 |
| Zugängliche Anmeldung | keine kognitiven Tests (z. B. Rätsel) als einzige Anmeldung; Einfügen aus Passwortmanager erlaubt | WCAG 3.3.8 |
| Konsistenz | gleiche Funktionen heißen und sehen überall gleich aus; Hilfe an konsistenter Stelle | WCAG 3.2.3, 3.2.4, 3.2.6 |
| Verständliche Sprache | siehe [content-writing.md](content-writing.md) | — |

## 5. Robust

- Semantisches HTML zuerst, ARIA nur, wo HTML nicht reicht. Richtig eingesetzt: Rollen, Namen und Zustände.
- Statusmeldungen (Toast, „gespeichert“) werden Screenreadern angekündigt (`role="status"` / `aria-live`) (WCAG 4.1.3).
- Jede Komponente in `core/components/` beschreibt ihre Tastatur- und Screenreader-Anforderungen.

## 6. Accessibility in jeder Phase

| Phase | Was geprüft wird |
|---|---|
| Brief | Profil festlegen (Standard / Erweitert), besondere Zielgruppen erfassen |
| Creative Direction | Auch Explorationen halten die Untergrenze: Fließtext ≥ 16 px (bzw. Profilwert), Targets ≥ 44 px, sichtbarer Fokus, Kontrast. Keine Richtung darf nur „schön“ sein. |
| Tokens | Kontrastpaare aller semantischen Farbrollen prüfen und in `tokens/README.md` des Projekts dokumentieren |
| Components | Tastatur, Screenreader, States, Zielgröße je Komponente |
| Templates | Überschriftenhierarchie, Landmarks, Reflow bei 320 px, Zoom 200 % |
| Release | Checkliste in [quality-standards.md](quality-standards.md) |

## 7. Physische und Print-Medien (falls vorhanden)

- Print: Fließtext ≥ 9–10 pt je nach Schrift, Kontrast wie digital, keine Information nur über Farbe.
- Beschilderung und Fahrzeuge: Lesbarkeit aus Distanz prüfen (Buchstabenhöhe zur Lesedistanz).
- Gravur und Prägung: Kontrast über Tiefe und Material prüfen, nicht über Farbe.
