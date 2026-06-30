# BD-07 - Elo-Ratings per Web Scraping holen

## Epic

Epic 2 - Datenquellen vorbereiten

## Notebook

`02_scrape_elo_ratings.ipynb`

## Datenquelle

Web Scraping

## Ziel

Teamstaerke vor dem Spiel ueber Elo-Ratings ergaenzen.

## Aufgaben

- Geeignete Elo-Quelle definieren.
- HTML-Struktur analysieren.
- Elo-Daten fuer relevante Teams und Datumsbereiche scrapen.
- Rohdaten speichern: `data/raw/elo/elo_raw.parquet`.
- Bereinigte Elo-Tabelle mit Teamname, Datum und Elo-Rating erstellen.
- Output speichern: `data/bronze/elo_ratings.parquet`.

## Akzeptanzkriterien

- [x] Elo-Daten sind aus einer Webquelle gescraped.
- [x] Scraping-Logik ist im Notebook dokumentiert.
- [x] Teamnamen und Datumsfelder sind bereinigt.
- [x] Elo-Daten koennen spaeter mit Matchdatum und Team gematcht werden.

## Abhaengigkeiten

- BD-04
