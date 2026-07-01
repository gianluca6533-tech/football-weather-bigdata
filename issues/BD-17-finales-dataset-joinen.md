# BD-17 - Wetter-, Elo- und StatsBomb-Daten joinen

## Epic

Epic 6 - Spark Feature Engineering und Final Dataset

## Notebook

`08_join_final_dataset.ipynb`

## Ziel

Alle Datenquellen in ein finales Analyse-Dataset verbinden.

## Aufgaben

- Team-Match-Basisdaten laden.
- Wetterdaten aus Kafka-Ergebnis joinen.
- Elo-Features joinen.
- Join-Keys pruefen: Match-ID, Datum, Team, Gegner und Location.
- Fehlende Werte analysieren.
- Outputs speichern: `data/gold/team_match_analysis_dataset.parquet` und `data/gold/team_match_analysis_dataset.csv`.

## Akzeptanzkriterien

- [x] Finales Dataset enthaelt StatsBomb-, Wetter- und Elo-Features.
- [x] Anzahl Zeilen ist plausibel.
- [x] Fehlende Werte sind dokumentiert.
- [x] Dataset ist fuer Analyse-Notebooks verwendbar.

## Umsetzung

- Notebook: `notebooks/08_join_final_dataset.ipynb`
- Input:
  - `data/silver/team_match_base.parquet`
  - `data/silver/weather_from_kafka.parquet`
  - `data/silver/team_match_elo_features.parquet`
  - `data/bronze/elo_ratings.parquet` fuer Provenienz- und Input-Checks
- Verarbeitung:
  - Spark-DataFrames lesen die Silver-/Bronze-Daten.
  - Join-Keys werden vorab auf Eindeutigkeit geprueft.
  - Wetterdaten werden ueber `match_id` auf beide Team-Match-Zeilen gejoint.
  - Elo-Features werden ueber `match_id` und `team_id` gejoint.
  - Datum, Stadion und Teamnamen werden nach dem Join plausibilisiert.
- Output:
  - `data/gold/team_match_analysis_dataset.parquet`
  - `data/gold/team_match_analysis_dataset.csv`
  - `outputs/tables/bd17_missing_values.csv`
  - `outputs/tables/bd17_join_quality_summary.csv`
- Qualitaetscheck:
  - 628 Team-Match-Zeilen fuer 314 Spiele
  - keine doppelten `(match_id, team_id)`-Zeilen
  - keine fehlenden Wetter- oder Elo-Joins
  - Missing Values sind spaltenweise dokumentiert

## Methodik

- DataFrame-orientierte Verarbeitung mit `select`, `join`, Aggregationen und expliziten Spaltenprojektionen.
- Reproduzierbare Pipeline-Stufe von Silver nach Gold mit dokumentierten Join-Checks und Missing-Value-Pruefungen.

## Abhaengigkeiten

- BD-08
- BD-15
- BD-16
