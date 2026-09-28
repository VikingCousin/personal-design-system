# Spacing & Sizing (Core)

## 1. Abstandsraster

**Basiseinheit 4 px.** Alle Abstände sind Vielfache von 4. Core liefert die Primitive-Skala als Default in [`defaults.tokens.json`](defaults.tokens.json):

| Token | px | Token | px |
|---|---|---|---|
| `space.0` | 0 | `space.8` | 32 |
| `space.1` | 4 | `space.10` | 40 |
| `space.2` | 8 | `space.12` | 48 |
| `space.3` | 12 | `space.16` | 64 |
| `space.4` | 16 | `space.20` | 80 |
| `space.5` | 20 | `space.24` | 96 |
| `space.6` | 24 | `space.32` | 128 |

Die Skala ist neutral. Wie **luftig oder dicht** eine Marke wirkt, entsteht über die Zuordnung auf der semantischen Ebene.

## 2. Semantische Abstände (Pflicht)

| Token | Bedeutung |
|---|---|
| `space.inset.xs / sm / md / lg / xl` | Innenabstand von Elementen (Button, Karte, Dialog) |
| `space.stack.xs / sm / md / lg / xl` | vertikaler Abstand zwischen gestapelten Elementen |
| `space.inline.xs / sm / md / lg` | horizontaler Abstand zwischen nebeneinanderliegenden Elementen |
| `space.layout.gutter` | Seitenrand (mobil ≥ 16 px) |
| `space.layout.section` | Abstand zwischen großen Seitenabschnitten |

**Regel:** Näher zusammen gehört zusammen (Gestaltgesetz der Nähe). Abstand innerhalb einer Gruppe < Abstand zwischen Gruppen.

## 3. Größen

| Token | Bedeutung | Default |
|---|---|---|
| `size.target.min` | minimale Touch-Zielgröße | 44 px (Profil Erweitert: 48 px) |
| `size.target.min-pointer` | Minimum für dichte, rein zeigergesteuerte Oberflächen | 24 px |
| `size.control.sm / md / lg` | Höhe von Buttons, Inputs, Selects | Projekt, Empfehlung 36 / 44 / 52 px; `md` ≥ `size.target.min` auf Touch |
| `size.icon.sm / md / lg / xl` | Icongrößen | 16 / 20 / 24 / 32 px |
| `size.container.sm / md / lg / xl` | maximale Inhaltsbreiten | Projekt, Empfehlung 640 / 768 / 1024 / 1280 px |
| `size.measure` | maximale Textzeilenlänge | 70ch |

Ein Control darf visuell kleiner sein als `size.target.min`, wenn seine **Klickfläche** (Padding oder Pseudo-Element) die Mindestgröße erreicht.

## 4. Dichte

Projekte mit datenreichen Oberflächen dürfen einen Modus **kompakt** definieren: Er überschreibt `space.inset.*`, `space.stack.*` und `size.control.*` mit kleineren Werten.
- Kompakt gilt nur für Zeigergeräte (`pointer: fine`). Auf Touch gilt immer die komfortable Dichte.
- `size.target.min-pointer` darf nicht unterschritten werden.
