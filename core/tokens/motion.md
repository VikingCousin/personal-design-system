# Motion (Core)

> Core definiert **Dauerstufen, Kurvenrollen und Regeln**. Den Bewegungscharakter (ruhig, federnd, knapp) prägt das Projekt über die Werte.

## 1. Dauer

| Token | Default | Verwendung |
|---|---|---|
| `duration.instant` | 0 ms | sofortige Zustandswechsel, reduzierte Bewegung |
| `duration.fast` | 120 ms | Hover, Fokus, kleine Zustandswechsel |
| `duration.base` | 200 ms | Aufklappen, Einblenden kleiner Elemente |
| `duration.slow` | 320 ms | Dialog, Drawer, Seitenübergänge |
| `duration.deliberate` | 500 ms | bewusst langsame, erzählende Übergänge (sparsam) |

Größere und weiter wandernde Elemente bewegen sich länger. Nichts in einem Bedienablauf dauert länger als 500 ms.

## 2. Kurven

| Token | Rolle | Default |
|---|---|---|
| `easing.standard` | Bewegung innerhalb des Bildschirms | `cubic-bezier(0.2, 0, 0, 1)` |
| `easing.enter` | etwas erscheint (verlangsamt am Ende) | `cubic-bezier(0, 0, 0, 1)` |
| `easing.exit` | etwas verschwindet (beschleunigt) | `cubic-bezier(0.3, 0, 1, 1)` |
| `easing.linear` | Fortschritt, Ladebalken | `linear` |

Projekte dürfen die Werte ändern (z. B. federnd für eine verspielte Marke), aber nicht die Rollen.

## 3. Regeln

1. **Bewegung erklärt.** Sie zeigt Herkunft, Ziel oder Zusammenhang. Reine Dekoration ist in Abläufen nicht erlaubt, auf Marketingseiten sparsam.
2. **Reduzierte Bewegung:** Bei `prefers-reduced-motion: reduce` werden Bewegungen durch kurze Überblendungen ersetzt (≤ `duration.fast`) oder entfallen. Parallax, Autoplay und Zoom-Effekte entfallen ganz.
3. **Keine Information nur durch Bewegung.**
4. **Nichts blinkt** mehr als 3× pro Sekunde.
5. **Bewegte Inhalte über 5 s** lassen sich pausieren.
6. **Keine Layout-Sprünge:** animiert werden `transform` und `opacity`, nicht Breite, Höhe oder Position im Fluss.
