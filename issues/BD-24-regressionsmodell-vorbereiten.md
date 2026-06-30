# BD-24 - Regressionsmodell vorbereiten

## Epic

Epic 8 - Modellierung und Vergleich Wetter vs. Teamstaerke

## Notebook

`11_analysis_chance_quality_model.ipynb`

## Ziel

Pruefen, was mehr erklaert: Wetter oder Teamstaerke.

## Modellidee

`team_xg ~ temperature + feels_like + rain + elo_diff + tournament`

## Aufgaben

- Analyse-Dataset fuer Regression vorbereiten.
- Kategoriale Variablen kodieren: Tournament und Rain Flag.
- Zielvariablen definieren: `team_xg`, optional `xg_per_shot`, optional `pass_completion_rate`, optional `pressures`.
- Fehlende Werte behandeln.
- Dokumentieren, dass Train/Test optional ist, da es um erklaerende Analyse geht.

## Akzeptanzkriterien

- [x] Modell-Dataset ist sauber vorbereitet.
- [x] Modellvariablen sind dokumentiert.
- [x] Ziel und Features sind klar getrennt.

## Abhaengigkeiten

- BD-18
