# Naming Conventions (Core)

## 1. Grundregeln

- **Sprache:** Token-, Komponenten-, Datei- und Variablennamen sind **englisch**. Inhalte und Dokumentation dürfen in der Projektsprache sein.
- **Schreibweise:** Kleinbuchstaben, Segmente mit Punkt getrennt, mehrteilige Segmente mit Bindestrich: `color.text.on-action`.
- **Keine Aussehensnamen auf der semantischen Ebene:** `color.action.primary.bg`, nie `color.green-button`.
- **Keine Markennamen außerhalb der Primitives:** `color.brand.500` ist erlaubt, `color.lebensband` in einer Komponente nicht.

## 2. Grammatik

```
{kategorie}.{konzept}.{rolle}.{variante}.{zustand}
```

Nicht jedes Segment ist immer nötig. Die Reihenfolge ist fest.

| Segment | Beispiele |
|---|---|
| kategorie | `color` `font` `text` `space` `size` `radius` `border` `shadow` `elevation` `opacity` `duration` `easing` `breakpoint` `z` |
| konzept | `bg` `text` `border` `action` `feedback` `focus` `overlay` `inset` `stack` `control` … |
| rolle | `primary` `secondary` `danger` `success` `warning` `error` `info` `muted` … |
| variante | `subtle` `strong` `on-action` `sm` `md` `lg` … |
| zustand | `hover` `active` `selected` `disabled` |

Beispiele: `color.action.primary.bg-hover`, `color.feedback.error.text`, `space.inset.md`, `size.control.lg`, `radius.control`, `z.modal`.

**Zustände** werden an das letzte Segment gehängt (`bg-hover`, `bg-active`) statt als eigenes Segment, damit die Tiefe flach bleibt.

## 3. Primitives

| Kategorie | Muster | Beispiel |
|---|---|---|
| Farbpaletten | `color.{palette}.{stufe}` mit Stufen 50, 100 … 900, 950 | `color.neutral.100`, `color.brand.700` |
| Schriftfamilien | `font.family.{rolle}` | `font.family.display`, `font.family.body`, `font.family.mono` |
| Schriftgrößen | `font.size.{stufe}` mit numerischen Stufen | `font.size.100` … `font.size.900` |
| Abstände | `space.{n}` in Vielfachen von 4 px | `space.4` = 16 px |

Paletten dürfen Projektnamen haben (`color.moss.500`), sie werden aber nur auf der Primitive-Ebene verwendet.

## 4. Component Tokens

```
{komponente}.{teil}.{eigenschaft}.{variante-oder-zustand}
```

Beispiel: `button.primary.bg`, `button.primary.bg-hover`, `input.border-invalid`, `card.padding`.

## 5. CSS-Variablen

- Aus `color.action.primary.bg` wird `--color-action-primary-bg`.
- Projekte dürfen ein kurzes Präfix setzen, um Konflikte zu vermeiden: `--acme-color-action-primary-bg`. Das Präfix steht im Projekt-README.

## 6. Komponenten und Dateien

- Komponentennamen: PascalCase im Code (`FormField`), kebab-case in Dateien (`form-field.md`).
- Projektkomponenten, die eine Core-Komponente erweitern, behalten den Core-Namen plus Zusatz (`ButtonIcon`, nicht `CircleThing`).
