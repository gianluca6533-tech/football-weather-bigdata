# BD-11 - Open-Meteo Wetterdaten abrufen

## Epic

Epic 4 - Open-Meteo Wetterdaten

## Notebook

`04_ingest_weather_openmeteo.ipynb`

## Datenquelle

REST API

## Ziel

Historische Wetterdaten pro Match-Ort und Match-Datum abrufen.

## Wettervariablen

- Temperatur
- Gefuehlte Temperatur
- Regen oder Niederschlag

## Aufgaben

- Fuer jede Match-Location-Date-Kombination Wetter abrufen.
- Nur eindeutige Lookup Keys abfragen: Datum, Latitude, Longitude.
- API-Responses cachen.
- Wetterdaten in strukturierte Tabelle transformieren.
- Outputs speichern: `data/raw/weather/openmeteo_raw.jsonl` und `data/bronze/weather_observations.parquet`.

## Akzeptanzkriterien

- [x] Wetterdaten sind fuer Match-Orte und Matchdaten vorhanden.
- [x] API wird nicht unnoetig mehrfach aufgerufen.
- [x] Temperatur, gefuehlte Temperatur und Regen sind enthalten.
- [x] Fehlerhafte API-Abfragen werden dokumentiert.

## Abhaengigkeiten

- BD-10
