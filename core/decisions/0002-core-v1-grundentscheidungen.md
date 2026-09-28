# 0002 · Grundentscheidungen für Core v1.0

- **Status:** accepted · **Ebene:** PDS · **Datum:** 2026-09-28 · **Core-Version:** 1.0.0
- **Freigabe:** Auftrag des Nutzers vom 2026-09-28, Core v1.0 weitgehend autonom aufzubauen (Architektur, Dokumentation, Struktur). Markenentscheidungen sind davon ausgenommen und bleiben in den Projekten.

| # | Entscheidung | Begründung | Alternativen |
|---|---|---|---|
| 1 | **Architektur `core/` + `projects/<name>/`**. Die flache Struktur aus dem Digital-Legacy-Brief (§19) wird zur Struktur **eines Projekts**. `adapters/` und `build/` sind für später vorgesehen, in v1.0 nur als Konzept. | trennt Systematik und Marke. Die Analyse stammt aus dem Pilotprojekt. | flache Struktur je Projekt; getrennte Repositories (zu schwer für eine Person) |
| 2 | **Token-Format nach W3C Design Tokens Community Group** (`$value`, `$type`, Verweise `{…}`), Einheit px in den Dateien, rem in CSS | werkzeugneutral, später mit Style Dictionary o. ä. übersetzbar | Tailwind-Konfiguration als Quelle (bindet an ein Werkzeug), reines CSS |
| 3 | **Semantischer Vertrag in Core, Werte im Projekt** | Core-Komponenten funktionieren in jedem Projekt | Core liefert Beispielwerte (Gefahr eines Default-Stils) |
| 4 | **Keine Farb-, Schrift-, Radius- oder Schattenwerte in Core.** Neutrale Skalen (Abstand 4-px-Raster, Zielgrößen, Z-Index, Breakpoints, Dauern) als überschreibbare Defaults. | Core soll keinen Stil erzwingen | vollständiges Basis-Theme |
| 5 | **Accessibility-Baseline WCAG 2.2 AA**, Profil „Erweitert“ optional | aktueller Standard, rechtlich und praktisch sinnvoll | WCAG 2.1 AA; AAA als Pflicht (zu restriktiv) |
| 6 | **Englische Systemnamen**, Dokumentation auf Deutsch | Kompatibilität mit Werkzeugen und Code | deutsche Token-Namen |
| 7 | **Gates G0–G6** und **Prozess-Tiefe S/M/L** | Nutzer behält die Markenentscheidungen, kleine Projekte bleiben schlank | ein einheitlich schwerer Prozess |
| 8 | **Semantic Versioning** mit CHANGELOG, Ausnahmen im Projektlog | nachvollziehbar, ohne Bürokratie | keine Versionierung |
| 9 | **Unverbindliche Patterns** getrennt von Regeln | gute Ideen gehen nicht verloren, ohne zur Pflicht zu werden | alles in Core oder alles im Projekt |

## Folgen

- Digital Legacy bleibt als unfertiges, privates Pilotprojekt bestehen (nicht Teil des öffentlichen Repositorys). Seine Architektur-Analyse ist durch diese Entscheidung für Core umgesetzt.
- Adapter (CSS, Tailwind, React, shadcn, PPTX, DOCX) sind für eine spätere MINOR-Version vorgesehen.
