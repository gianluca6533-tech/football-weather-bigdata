# BD-25 - Regressionsmodelle vergleichen

## Epic

Epic 8 - Modellierung und Vergleich Wetter vs. Teamstaerke

## Notebook

`11_analysis_chance_quality_model.ipynb`

## Ziel

Vergleichen, ob Wettervariablen, Elo oder Kombinationen davon mehr erklaeren.

## Aufgaben

- Modelle berechnen: nur Wetter, nur Elo, Wetter + Elo, Wetter + Elo + Tournament.
- R2 oder Adjusted R2 vergleichen und den Zusatznutzen von Wetter nach Elo separat ausweisen.
- Koeffizientenplot erstellen.
- Outputs speichern: `outputs/tables/model_comparison.csv`, `outputs/tables/model_incremental_comparison.csv`, `outputs/figures/model_r2_comparison.png`, `outputs/figures/model_coefficients.png`.

## Akzeptanzkriterien

- [x] Mindestens 3 Modellvarianten sind verglichen.
- [x] Ergebnis ist verstaendlich dokumentiert.
- [x] Modelloutput ist fuer Praesentation verwendbar.

## Abhaengigkeiten

- BD-24
