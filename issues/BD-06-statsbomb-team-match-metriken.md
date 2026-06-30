# BD-06 - StatsBomb-Events in Team-Match-Metriken aggregieren

## Epic

Epic 2 - Datenquellen vorbereiten

## Notebook

`01b_build_statsbomb_metrics.ipynb`

## Ziel

Aus Eventdaten eine Team-Match-Tabelle bauen.

## Aufgaben

- Pro Match und Team aggregieren: xG, Schuesse, xG pro Schuss, Paesse, erfolgreiche Paesse, Passquote, Pressures, Counterpressures, Duelle, Carries, lange Baelle und Long-Ball-Share.
- Sicherstellen, dass jedes Spiel genau zwei Team-Zeilen erzeugt.
- Output speichern: `data/bronze/team_match_statsbomb_metrics.parquet`.

## Akzeptanzkriterien

- [x] Jede Spiel-Team-Kombination hat eine Zeile.
- [x] Es gibt pro Spiel zwei Team-Zeilen.
- [x] Alle benoetigten Spielstil- und Chancenqualitaetsmetriken sind vorhanden.

## Abhaengigkeiten

- BD-05
