# BD-26 - Data Pipeline Graph erstellen

## Epic

Epic 9 - Storytelling, Data-Flow und Abgabe

## Dokument

`README.md`

## Ziel

Den gesamten Datenfluss visuell darstellen.

## Pipeline

- StatsBomb JSON/Parquet -> Team-Match-Metriken
- Elo Web Scraping -> Elo Features
- Venue Geocoding -> Location Dimension
- Open-Meteo API -> Wetter Features
- Wetter Features -> Kafka Topic
- Spark liest Kafka -> Wetter DataFrame
- Spark Joins -> Final Dataset
- Analyse-Notebooks -> Visualisierungen und Findings

## Aufgaben

- Data-Flow-Diagramm erstellen.
- Quellen, Transformationen und Outputs darstellen.
- Notebook-Namen im Graph erwaehnen.
- Pipeline-Graph und kurze Erklaerung im zentralen `README.md` einbinden.

## Akzeptanzkriterien

- [x] Der Data-Flow ist vollstaendig sichtbar.
- [x] Kafka und Spark sind klar eingezeichnet.
- [x] Jedes Notebook ist im Pipeline-Graph verortet.

## Ergebnis

Der finale Pipeline-Graph liegt als PNG unter `outputs/figures/DataGraph.png` und ist im zentralen `README.md` eingebunden. Dieselbe Grafik steht zusaetzlich in `docs/notebook_data_flow.md`, wo darunter die detaillierten Notebook-Vertraege mit Inputs und Outputs dokumentiert sind.

## Abhaengigkeiten

- BD-17
- BD-25
