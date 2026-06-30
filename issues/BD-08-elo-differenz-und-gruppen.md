# BD-08 - Elo-Differenz und Elo-Gruppen berechnen

## Epic

Epic 2 - Datenquellen vorbereiten

## Notebook

`02_scrape_elo_ratings.ipynb` oder `08_join_final_dataset.ipynb`

## Ziel

Fuer jede Team-Match-Zeile die Teamstaerke relativ zum Gegner berechnen.

## Aufgaben

- Elo vor dem Spiel pro Team bestimmen.
- Gegner-Elo bestimmen.
- `elo_diff = team_elo - opponent_elo` berechnen.
- Elo-Gruppen bilden: `favorite` bei `elo_diff > 75`, `balanced` bei `-75 <= elo_diff <= 75`, `underdog` bei `elo_diff < -75`.
- Output speichern: `data/silver/team_match_elo_features.parquet`.

## Akzeptanzkriterien

- [x] Jede Team-Match-Zeile hat `team_elo`, `opponent_elo` und `elo_diff`.
- [x] Elo-Gruppe ist nachvollziehbar berechnet.
- [x] Fehlende Elo-Werte werden dokumentiert.

## Abhaengigkeiten

- BD-06
- BD-07
