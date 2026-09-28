# 0001 · Audit der Core-Kandidaten aus dem Pilotprojekt Digital Legacy

- **Status:** accepted
- **Ebene:** PDS (Personal Design System)
- **Datum:** 2026-09-28
- **Core-Version:** 1.0.0
- **Quelle:** Kandidatenliste K1–K30 im Pilotprojekt (nicht Teil des öffentlichen Repositorys)

## Kontext

Digital Legacy war der Pilot bzw. Stresstest für das Personal Design System. Dabei wurden 30 mögliche universelle Regeln als `[CORE-KANDIDAT]` markiert. Vor dem Aufbau von Core v1.0 wurde jeder Kandidat einzeln geprüft. Maßstab war nicht, ob die Regel bei Digital Legacy gut funktioniert hat, sondern ob sie für ein beliebiges Projekt (SaaS, lokales Unternehmen, E-Commerce, App, persönliche Marke …) richtig ist.

## Kategorien

- **A · UNIVERSAL**: wird Teil von Core v1.0
- **B · PROJECT PATTERN**: wiederverwendbares Muster, nicht verbindlich. Liegt in `core/patterns/`.
- **C · DIGITAL-LEGACY-SPECIFIC**: bleibt ausschließlich beim Pilotprojekt

## Ergebnis

| # | Kandidat | Kat. | Umsetzung in Core / Begründung |
|---|---|---|---|
| K1 | Accessibility als Grundprinzip | **A** | `principles/accessibility.md`. Baseline WCAG 2.2 AA, Projekte dürfen verschärfen, nie absenken. |
| K2 | Token-Ebenen primitive → semantic → component | **A** | `tokens/architecture.md` |
| K3 | Semantischer Token-Vertrag | **A** | `tokens/contract.tokens.json`, `tokens/architecture.md` |
| K4 | Farben in mehreren Farbsystemen dokumentieren | **A (bedingt)** | `tokens/color.md`. HEX + OKLCH immer; CMYK, RAL und Pantone **nur**, wenn das Projekt Print oder physische Produkte hat. Grenzfall: Bei Digital Legacy war das zentral, bei einer reinen SaaS wäre es unnötige Last. Deshalb bedingt. |
| K5 | Farbrollen Brand / Semantic / UI / Material | **A (bedingt)** | `tokens/color.md`. Die Rolle „Material“ ist optional. |
| K6 | Entscheidungsbegründung mit 7 Prüffragen | **A** | `principles/design-principles.md`. Die Frage „digital UND physisch“ wird zu „in allen Medien des Projekts“. |
| K7 | Entscheidungsebenen PDS / PROJ / OPEN | **A** | `principles/documentation.md` |
| K8 | Aussagekennzeichnung FAKT / ABLEITUNG / ANNAHME / OFFEN | **A** | `principles/documentation.md`. Pflicht für strategische Dokumente, nicht für jede Spezifikation. |
| K9 | Component-Spezifikationsformat | **A** | `components/_spec-template.md` |
| K10 | Tonalität je Kontext als Matrix | **A (Methode)** | `principles/content-writing.md`. Die Methode ist universell, die konkreten Inhalte des Pilotprojekts bleiben **C**. |
| K11 | Schwierigstes Medium zuerst | **A (Methode)** | `process/creative-direction.md`. Allgemein formuliert: das restriktivste Anwendungsmedium des Projekts, z. B. Favicon, Fahrzeugbeschriftung, Stempel, Gravur. |
| K12 | Stress-Tests und Kriterien vor dem Sichten festlegen | **A** | `process/creative-direction.md` |
| K13 | Herkunftskennzeichnung KI / Original | **A (bedingt)** | `principles/content-writing.md`, `principles/quality-standards.md`: **Wenn** ein Produkt KI-erzeugte oder KI-bearbeitete Inhalte zeigt, wird die Herkunft erkennbar gemacht, nie nur über Farbe. Die dreistufige Systematik und Wortwahl von Digital Legacy bleiben **C**. |
| K14 | Nicht nur über Farbe kommunizieren | **A** | `principles/accessibility.md` |
| K15 | Reduzierte Bewegung, Bewegung nie inhaltstragend | **A** | `principles/interaction.md`, `tokens/motion.md` |
| K16 | Light und Dark bewusst gestalten | **A (bedingt)** | `tokens/color.md`. Ob ein Projekt Dark Mode anbietet, entscheidet das Projekt. **Wenn**, dann als eigener Entwurf. Grenzfall: Pflicht-Dark-Mode wäre für eine Handwerker-Landingpage Überlast. |
| K17 | Interne Systemsprache Englisch | **A** | `tokens/naming.md` |
| K18 | Brief als Source of Truth, Widersprüche dokumentieren | **A** | `process/project-workflow.md`, Agent Skill |
| K19 | Research-Agenda-Struktur | **A** | `process/project-template/research/RESEARCH-AGENDA.md` |
| K20 | Alltagssprache statt Technikjargon | **A (verallgemeinert)** | `principles/content-writing.md`: „Die Sprache der Nutzenden, nicht des Systems“. Für Fachprodukte ist das die Fachsprache der Nutzenden, deshalb verallgemeinert. |
| K21 | Internationale Anschlussfähigkeit | **A (Minimalform)** | `principles/content-writing.md`, `principles/responsive.md`: Inhalte von der Struktur trennen, Textexpansion tolerieren, keine Wortspiele als tragendes Element. Volle i18n bleibt Projektentscheidung. |
| K22 | Anrede als Regelwerk je Kontext | **A (Methode)** | `principles/content-writing.md`: Für Sprachen mit formeller/informeller Anrede muss das Projekt eine Regel festlegen. Welche, entscheidet das Projekt. |
| K23 | Entscheidungsstatus-Modell | **A** | `principles/documentation.md` |
| K24 | Nicht staffelbare Qualitäten bei Angebotsstufen | **B** | `patterns/README.md`. Nur relevant für Projekte mit gestaffelten Angeboten. Der Kern (Accessibility ist nie ein Premium-Feature) ist bereits durch K1 abgedeckt. |
| K25 | Offene Strategie-Entscheidungen in der Creative Direction neutral halten | **A** | `process/creative-direction.md` |
| K26 | Kennzeichnungssysteme aus Konventionen der Referenzwelt | **B** | `patterns/README.md`. Gute Methode, aber eine Gestaltungsstrategie, keine Pflicht. |
| K27 | Getrennte Bereiche über die Markenmetapher benennen | **B** | `patterns/README.md`. Setzt eine starke Markenmetapher voraus, die nicht jedes Projekt hat. |
| K28 | Style-Tile-Vergleichsformat | **A** | `process/creative-direction.md` |
| K29 | Explorationswerte ≠ Tokens | **A** | `principles/quality-standards.md`, `process/creative-direction.md` |
| K30 | Barrierefreie Untergrenze auch in Explorationen | **A (angepasst)** | `principles/accessibility.md`. Die Werte von Digital Legacy (Lesetext ≥ 20 px) waren für eine ältere Zielgruppe gewählt. Core übernimmt **16 px als Standard-Untergrenze** und stellt 18–20 px als Profil „Erweitert“ bereit. |

### Grenzfälle aus `05-core-vs-project.md` §C

| Thema | Kat. | Begründung |
|---|---|---|
| Sichtbarkeitsstufen (privat → öffentlich) | **B** | Als Muster „Sichtbarkeit immer anzeigen“ in `patterns/README.md`. Die Stufen selbst bleiben C. |
| Accessibility für ältere Nutzende | **A (als Profil)** | `principles/accessibility.md`: Profil „Erweitert“, das Projekte je nach Zielgruppe aktivieren |
| Markenmodi-Konzept | **A (als Methode, in K10)** | Kontexte mit eigener Tonalität gibt es in vielen Projekten (Marketing, App, Support, Rechnung) |
| Timeline- und Zeit-Komponenten | **C** | stark markengeprägt. Kann in einem späteren Projekt erneut Kandidat werden. |

### C · Ausschließlich Digital Legacy

Alle markenbezogenen Inhalte des Pilotprojekts, insbesondere: Kernidee, Prinzipien-Inhalte, Rollenmodell, Tonalität, physische Produkte, die drei Creative Directions mit Farben und Probeschriften, Stress-Test-Szenarien, Tabu-Motive, Projektkomponenten.

## Ausdrücklich NICHT übernommen

- keine Farben, Schriften, Formen, Materialien, Motive oder Layouts aus Digital Legacy
- kein Bezug auf ältere Zielgruppen als Standard (nur als optionales Profil)
- kein physisches Produkt, kein Print als Standard (nur als bedingte Regeln)

## Folgen

- Core v1.0 enthält alle A-Kandidaten in verallgemeinerter Form.
- B-Kandidaten stehen als unverbindliche Muster in `core/patterns/`.
- Die Kandidatenliste im Pilotprojekt verweist auf dieses Audit.
