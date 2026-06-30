# BD-05 - StatsBomb-Daten laden und lokal speichern

## Epic

Epic 2 - Datenquellen vorbereiten

## Notebook

`01_ingest_statsbomb.ipynb`

## Datenquelle

Datei, JSON oder Parquet

## Ziel

StatsBomb-Daten als Event- und Match-Daten lokal in einer sauberen Rohdatenstruktur speichern.

## Aufgaben

- StatsBomb-Rohdaten laden.
- Competition- und Match-Daten fuer die ausgewaehlten Turniere filtern.
- Eventdaten pro Match laden.
- Rohdaten speichern: `data/raw/statsbomb/matches_raw.parquet` und `data/raw/statsbomb/events_raw.parquet`.
- Erste Qualitaetschecks durchfuehren: Anzahl Matches, Anzahl Events, fehlende Match-IDs, fehlende Teamnamen.

## Akzeptanzkriterien

- [x] StatsBomb Match- und Eventdaten sind lokal gespeichert.
- [x] Es gibt einen kurzen Datenqualitaets-Check im Notebook.
- [x] Die ausgewaehlten Turniere sind korrekt gefiltert.

## Abhaengigkeiten

- BD-04
