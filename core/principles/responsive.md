# Responsive Design (Core)

> Gilt für alle digitalen Anwendungen eines Projekts. Breakpoint-Werte: [tokens/layout.md](../tokens/layout.md).

## Grundregeln

1. **Mobile first.** Zuerst wird die schmalste Ansicht gestaltet und gebaut, dann erweitert. Das kleinste unterstützte Viewport ist **320 px** breit.
2. **Inhalt bestimmt Umbrüche.** Breakpoints sind Richtwerte. Umgebrochen wird dort, wo das Layout bricht, nicht bei einem bestimmten Gerät.
3. **Komponenten reagieren auf ihren Container**, nicht auf das Fenster (Container Queries, wo möglich). Seitenlayouts reagieren auf den Viewport.
4. **Kein horizontales Scrollen der Seite.** Ausnahmen: Tabellen, Diagramme, Karten und Galerien in einem eigenen scrollbaren Bereich mit sichtbarem Hinweis.
5. **Gleicher Inhalt, andere Anordnung.** Mobil wird nichts Wesentliches weggelassen. Weniger Wichtiges darf eingeklappt, aber nicht versteckt werden.
6. **Touch und Zeiger gleichermaßen.** Hover ist nie der einzige Weg zu einer Funktion oder Information.
7. **Textexpansion einplanen.** Layouts vertragen 30–40 % längere Texte (Übersetzungen, lange deutsche Komposita, größere Schrift durch Nutzende).

## Layout-Regeln

| Thema | Regel |
|---|---|
| Zeilenlänge | Fließtext 45–75 Zeichen, max. ca. 80 |
| Seitenränder (Gutter) | mobil ≥ 16 px, darüber nach `space.layout.gutter` |
| Raster | Das Projekt definiert Spaltenzahl und Gutter je Breakpoint. Core-Empfehlung: 4 Spalten mobil, 8 Tablet, 12 Desktop |
| Bilder und Medien | flexibel (`max-width: 100%`), mit Seitenverhältnis-Reservierung gegen Layout-Sprünge |
| Tabellen | mobil: Scrollbereich, gestapelte Zeilen oder Spaltenauswahl. Entscheidung je Tabelle ([data.md](../components/data.md)) |
| Navigation | ab schmalen Breiten Menü-Button oder Tab-Bar. Die Hauptnavigation bleibt mit höchstens einem Tap erreichbar |
| Fixierte Elemente | Sticky Header oder Footer max. ca. 15 % der Viewport-Höhe auf Mobilgeräten; dürfen den Fokus nicht verdecken |
| Typografie | Überschriften dürfen fluid skalieren (`clamp()`), Fließtext bleibt ≥ Profil-Minimum |

## Prüfbreiten

Jede Seite bzw. jedes Template wird mindestens geprüft bei: **320 · 375 · 768 · 1024 · 1440 px** sowie mit **200 % Zoom**.

## Dichte (optional)

Projekte mit datenreichen Oberflächen (Dashboards, Tabellen) dürfen eine zweite Dichtestufe „kompakt“ definieren ([spacing-sizing.md](../tokens/spacing-sizing.md#4-dichte)). Auf Touch-Geräten gilt immer die komfortable Dichte.
