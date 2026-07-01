# BD-16 - Team-Match-Basisdataset mit Spark bauen

## Epic

Epic 6 - Spark Feature Engineering und Final Dataset

## Notebook

`07_build_team_match_features.ipynb`

## Ziel

StatsBomb-Metriken, Match-Metadaten und Team/Gegner-Struktur in Spark zusammenfuehren.

## Aufgaben

- `team_match_statsbomb_metrics.parquet` mit Spark laden.
- Match-Metadaten ergaenzen: Turnier, Datum, Team, Gegner, Spielort und Land.
- Gegner-Zeilen korrekt verbinden.
- Output speichern: `data/silver/team_match_base.parquet`.

## Akzeptanzkriterien

- [x] Jede Zeile entspricht einem Team in einem Spiel.
- [x] Gegnerinformationen sind korrekt vorhanden.
- [x] Dataset ist mit Spark erzeugt und gespeichert.

## Umsetzung

- Notebook: `notebooks/07_build_team_match_features.ipynb`
- Input:
  - `data/bronze/team_match_statsbomb_metrics.parquet`
  - `data/bronze/statsbomb_matches.parquet`
- Verarbeitung:
  - Spark-DataFrames lesen die Bronze-Parquetdaten.
  - Match-Metadaten werden aus der kanonischen Match-Tabelle ergaenzt.
  - Gegnerzeilen werden per Self-Join auf `match_id` und `opponent_team_id` verbunden und validiert.
  - Zentrale Gegnermetriken werden als `opponent_*`-Spalten ausgegeben.
- Output:
  - `data/silver/team_match_base.parquet`
- Qualitaetscheck:
  - 628 Team-Match-Zeilen fuer 314 Spiele
  - keine doppelten `(match_id, team_id)`-Zeilen
  - jedes Spiel hat genau zwei Team-Zeilen

## Methodik

- DataFrame-orientierte Verarbeitung mit relationalen Operationen wie `select`, `join` und Aggregationen.
- Reproduzierbare Pipeline-Stufe von Bronze nach Silver mit expliziten Inputs, Outputs und Qualitaetschecks.

## Abhaengigkeiten

- BD-06
- BD-02
