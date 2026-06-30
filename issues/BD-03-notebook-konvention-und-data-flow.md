# BD-03 - Notebook-Konvention und Data-Flow-Struktur festlegen

## Epic

Epic 1 - Projekt-Setup und Architektur

## Ziel

Festlegen, welches Notebook welchen Schritt der Pipeline abbildet.

## Aufgaben

- [x] Notebook-Namensschema definieren:
  - `00_project_overview.ipynb`
  - `01_ingest_statsbomb.ipynb`
  - `02_scrape_elo_ratings.ipynb`
  - `03_geocode_venues.ipynb`
  - `04_ingest_weather_openmeteo.ipynb`
  - `05_kafka_producer_weather.ipynb`
  - `06_spark_read_kafka_weather.ipynb`
  - `07_build_team_match_features.ipynb`
  - `08_join_final_dataset.ipynb`
  - `09_eda_weather_distribution.ipynb`
  - `10_analysis_style_intensity.ipynb`
  - `11_analysis_chance_quality_model.ipynb`
  - finaler Data-Flow-Graph im `README.md`
- [x] Fuer jedes Notebook Input, Output und Zweck dokumentieren.
- [x] Pipeline-Uebersicht fuer `00_project_overview.ipynb` fachlich vorbereiten.
- [x] Sicherstellen, dass kein einziges Notebook ueberladen ist.

## Umsetzung

- Notebook-Konvention und Data Flow sind in `docs/notebook_data_flow.md` dokumentiert.
- Die Dokumentation nutzt die Kursressourcen zu Web APIs/Web Scraping, Kafka, Spark Streaming und Spark DataFrames als Referenz fuer die Trennung der Pipeline-Schritte.
- Die eigentlichen Pipeline-Notebooks bleiben fuer BD-03 bewusst ohne fachlichen Inhalt; sie werden in den nachfolgenden Issues erstellt bzw. gefuellt.

## Akzeptanzkriterien

- [x] Jedes Notebook hat einen klaren Zweck.
- [x] Jedes Notebook speichert ein Ergebnis.
- [x] Der Data-Flow ist nachvollziehbar.
- [x] Es gibt kein einzelnes ueberladenes Notebook.

## Abhaengigkeiten

- BD-01
