# Token-Architektur (Core)

## 1. Drei Ebenen

```
PRIMITIVE          →   SEMANTIC                      →   COMPONENT
(Rohwerte)             (Rolle / Bedeutung)                (Verwendung in einer Komponente)

color.green.600    →   color.action.primary.bg       →   button.primary.bg
font.family.serif  →   text.heading.lg (Composite)   →   card.title.text
space.4            →   space.inset.md                →   card.padding
```

| Ebene | Frage | Wer definiert Namen | Wer definiert Werte | Wer darf sie verwenden |
|---|---|---|---|---|
| **Primitive** | Welche Rohwerte gibt es? | Projekt | Projekt (Core liefert Defaults für neutrale Skalen) | **nur** semantische Tokens |
| **Semantic** | Wofür wird ein Wert benutzt? | **Core** (Pflicht-Vertrag) + Projekt (Ergänzungen) | Projekt (verweist auf Primitives) | Komponenten, Templates, Layouts |
| **Component** | Wie sieht Teil X von Komponente Y aus? | Core (für Core-Komponenten) + Projekt (für eigene Komponenten) | verweist auf Semantic, nur selten direkt auf Primitive | nur diese Komponente |

**Regeln**
1. Komponenten und Templates verwenden **nie** Primitive direkt und **nie** Rohwerte (`#3366CC`, `13px`).
2. Semantische Namen beschreiben die **Rolle**, nie das Aussehen (`color.feedback.error.text`, nicht `color.red`).
3. Component Tokens entstehen nur, wenn eine Komponente bewusst von der semantischen Ebene abweichen oder einzeln anpassbar sein soll. Sonst verweist die Komponente direkt auf Semantic.
4. Jeder Verweis zeigt eine Ebene nach unten: component → semantic → primitive.

## 2. Der Vertrag

Core legt in [`contract.tokens.json`](contract.tokens.json) die **Pflicht-Tokens** der semantischen Ebene fest (Namen, Typ, Bedeutung, keine Werte).

- Jedes Projekt **muss** alle Pflicht-Tokens mit Werten belegen. Dadurch funktionieren alle Core-Komponentenspezifikationen in jedem Projekt.
- Projekte **dürfen** eigene semantische Tokens ergänzen (z. B. `color.status.booked`, `color.data.series-1`). Ergänzungen folgen der [Namensgrammatik](naming.md).
- Projekte **dürfen keine** Pflicht-Tokens umbenennen oder mit anderer Bedeutung belegen.
- Optionale Gruppen im Vertrag (z. B. `color.material`, `color.data`) werden nur belegt, wenn das Projekt sie braucht.

## 3. Dateiformat

- **Format:** JSON nach dem Modell des W3C Design Tokens Community Group Formats (`$value`, `$type`, `$description`, Verweise als `{pfad.zum.token}`). Das Format ist werkzeugneutral und lässt sich später mit Build-Werkzeugen (z. B. Style Dictionary) in CSS, Tailwind, iOS oder Android übersetzen.
- **Einheiten:** `px` in den Token-Dateien (eindeutig, werkzeugneutral). Beim Übersetzen nach CSS werden Schriftgrößen und Abstände in `rem` umgerechnet (Basis 16 px), damit Nutzer-Schriftgrößen wirken.
- **Farben:** HEX als `$value`, weitere Farbräume in `$extensions.pds` (siehe [color.md](color.md#6-farbdokumentation)).

Beispiel:

```json
{
  "color": {
    "action": {
      "primary": {
        "bg": { "$type": "color", "$value": "{color.brand.700}", "$description": "Hintergrund der Hauptaktion" }
      }
    }
  }
}
```

## 4. Dateien im Projekt

```
projects/<p>/tokens/
├── README.md                    Übersicht, Kontrastpaare, Farbtabellen, Schriftlizenzen
├── primitives.tokens.json       Rohwerte: Paletten, Schriftfamilien, Skalen
├── semantic.tokens.json         Pflicht-Vertrag + Ergänzungen (Standard- bzw. Hellmodus)
├── semantic.dark.tokens.json    optional: nur Abweichungen im Dunkelmodus
└── components.tokens.json       optional: Component Tokens
```

Build-Ausgaben (CSS-Variablen, Tailwind-Konfiguration …) liegen später in `projects/<p>/build/` und werden nie von Hand bearbeitet.

## 5. Modi und Themes

- **Modus** = Variante derselben Marke (hell, dunkel, hoher Kontrast, kompakt). Modi überschreiben nur semantische Tokens.
- **Theme** = Untermarke oder Kunde (z. B. White-Label). Themes überschreiben Primitives und ggf. semantische Tokens.
- Komponenten wissen nichts von Modi oder Themes, sie verwenden nur semantische bzw. Component Tokens.

## 6. Wann Tokens entstehen

Tokens werden erst angelegt, wenn die visuelle Richtung des Projekts vom Nutzer gewählt ist (Gate G3, siehe [project-workflow.md](../process/project-workflow.md)). Werte aus Explorationen und Prototypen sind **Arbeitswerte** und werden nicht ungeprüft übernommen.
