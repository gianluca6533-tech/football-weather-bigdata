# BD-09 - Spielorte und Laender aus Matchdaten extrahieren

## Epic

Epic 3 - Venue-, City- und Geocoding-Pipeline

## Notebook

`03_geocode_venues.ipynb`

## Ziel

Alle benoetigten Orte fuer Wetterabfragen identifizieren.

## Aufgaben

- Aus Matchdaten Spielort, Stadion, Stadt und Land extrahieren.
- Eindeutige Location Keys bilden: Stadt, Land und optional Stadion.
- Duplikate entfernen.
- Problemfaelle in einer Tabelle dokumentieren.
- Output speichern: `data/bronze/venues_unique.parquet`.

## Akzeptanzkriterien

- [x] Alle eindeutigen Spielorte sind vorhanden.
- [x] Gleiche Orte werden nicht mehrfach abgefragt.
- [x] Problemfaelle werden in einer Tabelle dokumentiert.

## Abhaengigkeiten

- BD-05
