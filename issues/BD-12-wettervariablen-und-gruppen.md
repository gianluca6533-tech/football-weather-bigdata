# BD-12 - Wettervariablen bereinigen und Wettergruppen bilden

## Epic

Epic 4 - Open-Meteo Wetterdaten

## Notebook

`04_ingest_weather_openmeteo.ipynb`

## Ziel

Wetterdaten analysefaehig machen.

## Aufgaben

- Wetterdaten auf Match-Ebene bringen.
- Spalten standardisieren: `temperature_c`, `feels_like_c`, `rain_mm`, `rain_flag`.
- Temperaturgruppen bilden: `cold` bei `< 10 C`, `mild` bei `10-20 C`, `warm` bei `20-28 C`, `hot` bei `> 28 C`.
- Output speichern: `data/silver/weather_features.parquet`.

## Akzeptanzkriterien

- [x] Wetterdaten haben ein klares Schema.
- [x] Regen ist sowohl metrisch als auch als Ja/Nein-Flag vorhanden.
- [x] Temperaturgruppen sind korrekt gebildet.
- [x] Fehlende Wetterwerte sind dokumentiert.

## Abhaengigkeiten

- BD-11
