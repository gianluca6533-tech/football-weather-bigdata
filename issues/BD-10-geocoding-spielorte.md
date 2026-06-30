# BD-10 - Geocoding fuer Staedte und Spielorte durchfuehren

## Epic

Epic 3 - Venue-, City- und Geocoding-Pipeline

## Notebook

`03_geocode_venues.ipynb`

## Ziel

Fuer jede Stadt Latitude und Longitude bestimmen, damit Open-Meteo Wetterdaten abgerufen werden koennen.

## Aufgaben

- Open-Meteo Geocoding API oder alternative Geocoding-Quelle verwenden.
- Pro Stadt/Land Latitude und Longitude bestimmen.
- Cache verwenden, damit Orte nicht mehrfach abgefragt werden.
- Fehlgeschlagene Lookups dokumentieren.
- Outputs speichern: `data/silver/venue_geocodes.parquet`, `data/cache/geocoding_cache.json`, `outputs/tables/geocoding_failures.csv`.

## Akzeptanzkriterien

- [x] Die meisten Spielorte haben Latitude und Longitude.
- [x] Wiederholtes Ausfuehren nutzt Cache.
- [x] Fehlende oder unsichere Geocodes sind sichtbar dokumentiert.

## Abhaengigkeiten

- BD-09
