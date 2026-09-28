# Typografie (Core)

> Core definiert **Rollen, Skalenmethode und Mindestwerte**. Schriften und konkrete Größen wählt das Projekt.

## 1. Schriftrollen

| Primitive | Rolle | Pflicht? |
|---|---|---|
| `font.family.body` | Lesetext und Bedienung | Pflicht |
| `font.family.display` | Überschriften, große Anzeigen | optional (sonst = body) |
| `font.family.mono` | Code, tabellarische Daten | optional |

**Höchstens zwei Schriftfamilien plus optional eine Mono.** Mehr braucht eine Begründung.

## 2. Semantische Textstile (Composite Tokens)

Jeder Textstil fasst Familie, Größe, Zeilenhöhe, Schnitt und ggf. Laufweite zusammen (`$type: typography`).

| Token | Verwendung |
|---|---|
| `text.display.lg` / `text.display.md` | Hero, sehr große Anzeigen (optional) |
| `text.heading.xl` / `.lg` / `.md` / `.sm` | h1–h4 (h5/h6 = `heading.sm` bzw. `label`) |
| `text.body.lg` / `.md` / `.sm` | Lesetext: Einleitung, Standard, klein |
| `text.label.md` / `.sm` | Buttons, Formular-Labels, Navigation |
| `text.caption` | Bildunterschriften, Hilfstexte, Metadaten |
| `text.code` | Code (optional) |
| `text.numeric` | Tabellenzahlen: Stil-Varianten mit `tabular-nums` (optional) |

Pflicht sind: `heading.xl–sm`, `body.md`, `body.sm`, `label.md`, `caption`.

## 3. Skalenmethode

1. **Basis** = `text.body.md`: mindestens **16 px** (Profil Standard) bzw. **18–20 px** (Profil Erweitert).
2. **Verhältnis** wählt das Projekt nach Charakter und Dichte:

| Verhältnis | Wirkung | typisch für |
|---|---|---|
| 1.125 (große Sekunde) | ruhig, dicht | Dashboards, Software |
| 1.200 (kleine Terz) | ausgewogen | Apps, Dienstleistung |
| 1.250 (große Terz) | deutlich | Websites, Marketing |
| 1.333 (Quarte) | ausdrucksstark | Editorial, Marken mit starkem Auftritt |

3. **Primitive Stufen** `font.size.100` … `font.size.900` werden aus Basis × Verhältnis berechnet und auf ganze Pixel gerundet.
4. **Fluid:** Überschriften dürfen zwischen Mobil- und Desktopwert skalieren (`clamp()`). Lesetext bleibt fest.
5. Mobil wird die Skala oberhalb von `heading.md` gestaucht (z. B. Verhältnis eine Stufe kleiner).

## 4. Mindest- und Richtwerte

| Eigenschaft | Regel |
|---|---|
| Kleinste Schrift | 12 px absolut. Captions und Hilfstexte ≥ 14 px empfohlen |
| Zeilenhöhe Lesetext | 1.4–1.7 (längere Zeilen → mehr Zeilenhöhe) |
| Zeilenhöhe Überschriften | 1.05–1.3 |
| Zeilenlänge | 45–75 Zeichen |
| Absatzabstand | ≥ 0.75 × Schriftgröße |
| Versalien | nur für kurze Labels, mit +4–12 % Laufweite |
| Kursiv und Light-Schnitte | nicht für lange Texte unter 18 px |
| Ziffern | Tabellen und Preise mit `tabular-nums`. Ziffern in Daten und Nummern gut unterscheidbar (1/l/I, 0/O) |

## 5. Schriftwahl (Prüfliste für das Projekt)

- [ ] Zeichensatz: alle Sprachen des Projekts inkl. Umlaute, ß, Sonderzeichen, Währungen
- [ ] Lesbarkeit in kleinen Größen und auf schlechten Bildschirmen
- [ ] unterscheidbare Zeichen (Il1, 0O, rn/m)
- [ ] benötigte Schnitte (mindestens Regular, Bold; Kursiv bei Lesetext)
- [ ] Lizenz für **alle** Medien des Projekts (Web, App, Print, Video, Beschilderung, Gravur, Logo)
- [ ] Performance: variable Font oder wenige Schnitte, Subset, `font-display: swap`, Fallback-Stack mit ähnlichen Maßen
- [ ] Ersatzschrift für Office-Dokumente und Präsentationen festgelegt

Das Ergebnis der Prüfung steht in `projects/<p>/tokens/README.md`.
