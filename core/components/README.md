# Components (Core)

> Core definiert **Architektur, Verhalten, Zustände, Accessibility und Token-Abhängigkeiten** typischer Komponenten. Core definiert **kein Aussehen**. Das Aussehen entsteht aus den Tokens des Projekts.
> Eine Core-Komponente ist daher eine **Spezifikation**, kein fertiger Code. Projekte setzen sie in ihrer Technik um (HTML/CSS, React, shadcn/ui, Figma …).

## 1. Katalog

| Datei | Komponenten |
|---|---|
| [actions.md](actions.md) | Button · Link |
| [forms.md](forms.md) | Form Field · Input · Textarea · Select · Checkbox · Radio · Switch |
| [containers.md](containers.md) | Card · Modal/Dialog · Drawer · Accordion |
| [navigation.md](navigation.md) | Navigation · Tabs · Breadcrumb · Pagination |
| [feedback.md](feedback.md) | Alert · Toast · Tooltip · Badge · Empty State · Loading State · Error State |
| [data.md](data.md) | Table |
| [_spec-template.md](_spec-template.md) | Vorlage für jede neue Komponente (Core oder Projekt) |

## 2. Schichten

```
Core-Spezifikation  →  Projekt-Umsetzung      →  Projekt-Erweiterung
(Verhalten, States,    (Tokens des Projekts,      (eigene Varianten oder
 A11y, Tokens-Rollen)   Technik des Projekts)      eigene Komponenten)
```

| Schicht | Ort | Darf |
|---|---|---|
| Core-Spezifikation | `core/components/` | Rollen, Verhalten, Pflicht-Zustände und A11y festlegen |
| Projekt-Umsetzung | `projects/<p>/components/` bzw. Code | Tokens belegen, Technik wählen, **Aussehen** frei gestalten |
| Projekt-Erweiterung | `projects/<p>/components/<name>.md` | Varianten ergänzen, projektspezifische Komponenten bauen |

## 3. Zustandsmodell

| Zustand | Auslöser | Pflicht für |
|---|---|---|
| `default` | — | alle |
| `hover` | Zeiger darüber (`@media (hover: hover)`) | alle interaktiven |
| `focus-visible` | Tastaturfokus | alle interaktiven |
| `active` | gedrückt | Button, Link, Tab, Item |
| `selected` / `checked` | ausgewählt | Tabs, Checkbox, Radio, Switch, Listen, Tabellenzeilen |
| `disabled` | nicht verfügbar | Controls |
| `read-only` | sichtbar, nicht änderbar | Formularelemente |
| `loading` | Vorgang läuft | Button, Form, Container |
| `invalid` | Validierungsfehler | Formularelemente |
| `empty` | keine Daten | Listen, Tabellen, Container |
| `expanded` / `collapsed` | auf- oder zugeklappt | Accordion, Navigation, Select |

Jede Spezifikation listet die für sie relevanten Zustände. Ein Zustand darf nie **nur** über Farbe erkennbar sein.

## 4. Variantenlogik

Varianten werden entlang **weniger, unabhängiger Achsen** gebildet:

| Achse | Werte (Beispiel Button) | Regel |
|---|---|---|
| **Hierarchie / Emphasis** | primary · secondary · tertiary (ghost) | pro Bereich höchstens **eine** primary |
| **Intention / Tone** | neutral · danger (· success, falls nötig) | Intention ≠ Hierarchie |
| **Größe** | sm · md · lg | `md` ist Standard; Touch-Ziel beachten |
| **Form** (optional) | mit Text · nur Icon · Text + Icon | nur Icon → zugänglicher Name Pflicht |

Neue Achsen oder Werte in einem Projekt werden in dessen Komponentenspezifikation begründet. Varianten, die nur Farbe ändern und keine Bedeutung haben, werden vermieden.

## 5. Wann ein Projekt eine Komponente erweitert

| Situation | Vorgehen |
|---|---|
| Nur anderes Aussehen | **keine** Erweiterung. Tokens des Projekts belegen. |
| Zusätzliche Variante mit eigener Bedeutung (z. B. Button „booking“) | Projekt-Spec `projects/<p>/components/button.md` mit Verweis auf Core, nur die Abweichung beschreiben |
| Neues Verhalten auf Basis einer Core-Komponente (z. B. Datumsauswahl als Select-Erweiterung) | eigene Projektkomponente nach [_spec-template.md](_spec-template.md), Basis angeben |
| Völlig neue, markenspezifische Komponente (z. B. Buchungskalender, Produktkonfigurator) | eigene Projektkomponente nach Vorlage |
| Core-Regel passt nicht | **Ausnahme** dokumentieren ([governance.md](../process/governance.md#ausnahmen)), ggf. Core-Kandidat melden |

Projektkomponenten dürfen Core-Pflichten (Zustände, A11y, Zielgrößen) nicht unterschreiten.

## 6. Allgemeine Pflichten für alle Komponenten

- semantisches HTML-Element zuerst (`button`, `a`, `input`, `dialog`, `table` …)
- zugänglicher Name für jedes interaktive Element
- sichtbarer Fokus mit `color.focus.ring`, `border.width.focus`, `border.offset.focus`
- Zielgröße ≥ `size.target.min` auf Touch
- keine Rohwerte, nur Tokens
- funktioniert mit 200 % Zoom und langen Texten (keine fixen Breiten für Text)
- respektiert `prefers-reduced-motion`
