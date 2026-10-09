# Brand Kit · <Projektname>

> Ab Phase 5 (nach den Tokens). Vertrag und Generator: `core/brand-kit/README.md`.

- `brand-kit.json` ist die einzige Quelle. Werte stehen in `../tokens/`, hier nur Verweise, Regeln und Status.
- Alles bleibt `OPEN`, bis du es entscheidest. Freigabe des Kits mit Gate G4 („Tokens und Brand Kit“).
- Logos liegen im Projektordner `../assets/logos/` (nicht doppelt hier). Für den KI-Export nur Assets mit `"status": "ENTSCHIEDEN"`, `"ai_share": true` und `"rights_cleared": true`.

Erzeugen (aus dem Repository-Wurzelverzeichnis):
- Brand Kit: `python3 core/brand-kit/generator/build_brand_kit.py projects/<name>/brand-kit/brand-kit.json` → `dist/`
- AI Brand Context Pack: `python3 core/brand-kit/generator/export_ai_context.py projects/<name>/brand-kit/brand-kit.json` → `ai-pack/`

`dist/` und `ai-pack/` sind Ausgaben und werden nie von Hand bearbeitet.
