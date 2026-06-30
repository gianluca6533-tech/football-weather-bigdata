# Notebook-Konvention und Data Flow

Dieses Dokument legt fest, welches Notebook welchen Pipeline-Schritt abbildet. Die Notebooks sollen erst in den jeweiligen fachlichen Issues mit Code und Ergebnissen gefuellt werden. BD-03 definiert nur Konvention, Verantwortlichkeiten und erwartete Artefakte. Der finale Pipeline-Graph steht im zentralen `README.md`.

## Leitlinien

- Ein Notebook hat genau einen klaren Zweck: Ingestion, Transformation, Join oder Analyse.
- Jedes Notebook schreibt ein explizites Ergebnis in `data/`, `outputs/` oder `docs/`.
- Zwischenergebnisse werden nach Pipeline-Stufe abgelegt: `raw` fuer unveraenderte Quelldaten, `bronze` fuer technisch geladene Daten, `silver` fuer bereinigte und joinbare Daten, `gold` fuer finale Analyse- und Modellierungsdaten.
- Notebooks lesen nur aus vorherigen Stufen und schreiben nur in die eigene Zielstufe.
- Kafka- und Streaming-Schritte bleiben getrennt von Batch-Transformationen, damit Producer, Consumer und Spark-Logik einzeln testbar bleiben.
- Analyse-Notebooks lesen aus `data/gold/` und schreiben nur Praesentationsartefakte nach `outputs/`.

## Methodische Leitlinien

Die Aufteilung trennt Datenquellen, Transport, Transformation und Analyse klar voneinander:

- REST-API-Zugriffe und Web Scraping liegen in separaten Notebooks, damit externe Datenquellen einzeln reproduzierbar bleiben.
- Kafka Producer, Topic und Kafka Reader sind getrennte Pipeline-Schritte. Dadurch koennen Senden, Transport und Lesen unabhaengig geprueft werden.
- Der Kafka-Read-Schritt erzeugt einen stabilen Batch-Snapshot fuer die weitere Analyse, statt einen dauerhaft laufenden Stream vorauszusetzen.
- Feature-Building, Joins und Modellvorbereitung werden als DataFrame-orientierte Schritte mit expliziten Schemas geplant.
- Die Ausfuehrungsumgebung wird ueber Docker Compose und Umgebungsvariablen beschrieben, damit lokale und Cluster-Ausfuehrung dieselben Notebook-Vertraege nutzen.

## Pipeline-Uebersicht

![Data Pipeline Graph](../outputs/figures/DataGraph.png)

Der Graph ist bewusst als einfacher Pfeil aufgebaut: Links stehen Quellen und Lade-Notebooks, in der Mitte die Speicher- und Transformationsstufen, rechts Kafka/Spark, Gold-Dataset und Analyse-Outputs. Die PNG liegt unter `outputs/figures/DataGraph.png`. Die detaillierten Input-/Output-Vertraege stehen in der Tabelle darunter.

## Notebook-Vertrag

| Nr. | Notebook | Zweck | Input | Output |
| --- | --- | --- | --- | --- |
| 00 | `00_project_overview.ipynb` | Projektueberblick, Forschungsfrage, Pipeline-Vertrag, Turnier-Scope und Team-Match-Ebene dokumentieren. | `README.md`, `docs/notebook_data_flow.md`, Issue-Dateien | `docs/project_scope.md`, `data/reference/tournament_scope.json` |
| 01 | `01_ingest_statsbomb.ipynb` | StatsBomb Open Data technisch laden und als reproduzierbare Roh-/Bronze-Daten ablegen. | StatsBomb Open Data, Turnier-/Match-Scope aus BD-04 | `data/raw/statsbomb/`, `data/bronze/statsbomb_matches.parquet`, `data/bronze/statsbomb_events.parquet` |
| 01b | `01b_build_statsbomb_metrics.ipynb` | StatsBomb-Events mit Spark auf Team-Match-Metriken aggregieren. | `data/bronze/statsbomb_matches.parquet`, `data/bronze/statsbomb_events.parquet` | `data/bronze/team_match_statsbomb_metrics.parquet` |
| 02 | `02_scrape_elo_ratings.ipynb` | Elo-Ratings fuer relevante Teams und Spielzeitpunkte per Web Scraping sammeln. | Elo-Webquelle, Team-/Match-Liste aus `data/bronze/` | `data/raw/elo/elo_raw.parquet`, `data/bronze/elo_ratings.parquet`, Cache in `data/cache/elo/` |
| 02b | `02b_build_elo_features.ipynb` | Elo-Differenzen und Elo-Gruppen auf Team-Match-Ebene berechnen. | `data/bronze/team_match_statsbomb_metrics.parquet`, `data/bronze/elo_ratings.parquet` | `data/silver/team_match_elo_features.parquet`, `outputs/tables/bd08_missing_elo_values.csv` |
| 03 | `03_geocode_venues.ipynb` | Spielorte normalisieren und eindeutige Venue-/Location-Keys vorbereiten. | Match-/Venue-Daten aus `data/bronze/statsbomb_matches.parquet`, `data/reference/venue_city_overrides.csv` | `data/bronze/venues_unique.parquet`, `outputs/tables/bd09_venue_problem_cases.csv` |
| 03b | `03b_geocode_locations.ipynb` | Geokoordinaten fuer Wetterabfragen ermitteln und Lookup-Qualitaet dokumentieren. | `data/bronze/venues_unique.parquet` | `data/silver/venue_geocodes.parquet`, `data/cache/geocoding_cache.json`, `outputs/tables/geocoding_failures.csv` |
| 04 | `04_ingest_weather_openmeteo.ipynb` | Historische Wetterdaten je Spielort und Spielzeit via Open-Meteo laden. | `data/silver/venue_geocodes.parquet`, Match-Zeitpunkte | `data/raw/weather/openmeteo_raw.jsonl`, `data/bronze/weather_observations.parquet`, `outputs/tables/openmeteo_failures.csv` |
| 04b | `04b_build_weather_features.ipynb` | Wettervariablen fuer Analysen standardisieren und Wettergruppen bilden. | `data/bronze/weather_observations.parquet` | `data/silver/weather_features.parquet`, `outputs/tables/bd12_missing_weather_values.csv` |
| 05 | `05_kafka_producer_weather.ipynb` | Wetterdatensaetze aus Silver als Kafka-Messages in definierte Topics schreiben. | `data/silver/weather_features.parquet`, Kafka-Konfiguration aus `docs/kafka_topics.md` | Kafka Topic `weather.observations`, optional `outputs/tables/kafka_weather_sample.csv` |
| 06 | `06_spark_read_kafka_weather.ipynb` | Kafka-Wetterdaten mit Spark lesen, parsen und als strukturierte Wetterdaten speichern. | Kafka Topic `weather.observations`, Schema aus `docs/kafka_topics.md` | `data/silver/weather_from_kafka.parquet` |
| 07 | `07_build_team_match_features.ipynb` | StatsBomb-Teammetriken mit Match-Metadaten und validierter Gegnerstruktur zum Team-Match-Basisdataset zusammenfuehren. | `data/bronze/team_match_statsbomb_metrics.parquet`, `data/bronze/statsbomb_matches.parquet` | `data/silver/team_match_base.parquet` |
| 08 | `08_join_final_dataset.ipynb` | Team-Match-Basisdaten mit Wetter- und Elo-Features zum finalen Analyse-Dataset joinen. | `data/silver/team_match_base.parquet`, `data/silver/weather_from_kafka.parquet`, `data/silver/team_match_elo_features.parquet` | `data/gold/team_match_analysis_dataset.parquet`, `data/gold/team_match_analysis_dataset.csv` |
| 09 | `09_eda_weather_distribution.ipynb` | Wetterverteilungen und Plausibilitaet der Wettergruppen analysieren. | `data/gold/team_match_analysis_dataset.csv` | `outputs/figures/weather_temperature_histogram.png`, `outputs/figures/weather_feels_like_histogram.png`, `outputs/figures/weather_temperature_by_tournament.png`, `outputs/figures/rain_share.png`, `outputs/tables/bd19_weather_distribution_summary.csv` |
| 10 | `10_analysis_style_intensity.ipynb` | Zusammenhang zwischen Wetter, Teamstaerke und Spielstil-/Intensitaetsmetriken untersuchen. | `data/gold/team_match_analysis_dataset.parquet` | `outputs/figures/style_intensity_*`, `outputs/tables/style_intensity_results.csv` |
| 11 | `11_analysis_chance_quality_model.ipynb` | Chancenqualitaet und Regressionsmodelle fuer xG-/Shot-Quality-Metriken vorbereiten und vergleichen. | `data/gold/team_match_analysis_dataset.parquet` | `outputs/tables/model_comparison.csv`, `outputs/tables/model_incremental_comparison.csv`, `outputs/figures/model_r2_comparison.png`, `outputs/figures/model_coefficients.png` |

## Data-Flow-Regeln

| Stufe | Darf lesen aus | Darf schreiben nach | Typische Formate |
| --- | --- | --- | --- |
| Ingestion | externe Quellen, API, Scraping, Kafka | `data/raw/`, `data/bronze/`, `data/cache/` | JSON, CSV, Parquet |
| Normalisierung | `data/bronze/` | `data/silver/` | Parquet |
| Feature Engineering | `data/bronze/`, `data/silver/` | `data/silver/` | Parquet |
| Finaler Join | `data/silver/`, benoetigte Referenzdaten aus `data/bronze/` | `data/gold/` | Parquet |
| Analyse | `data/gold/` | `outputs/figures/`, `outputs/tables/` | PNG/SVG/PDF, CSV |
| Dokumentation | `outputs/`, `data/gold/`, `docs/` | `README.md`, `docs/` | Markdown, Bilder |

## Abgrenzung gegen ueberladene Notebooks

- `01` laedt nur StatsBomb-Daten; Team-Match-Metriken entstehen in `01b` und werden erst in `07` mit kanonischen Match-Metadaten verbunden.
- `02` scraped nur Elo-Daten; die Interpretation als `favorite`, `balanced` oder `underdog` entsteht in `02b`.
- `03` normalisiert nur Spielorte; API-Geocoding und Cache-Entscheidungen liegen in `03b`.
- `04` laedt Wetterdaten aus der API; die Analysevariablen und Wettergruppen entstehen in `04b`.
- Kafka-Produktion ist separat in `05`.
- `06` liest Kafka mit Spark; finale Joins passieren erst in `08`.
- `09`, `10` und `11` sind getrennte Analysefragen und schreiben eigene Ergebnisartefakte.
- Der finale Pipeline-Graph und die Abgabe-Story stehen im README; die eingebundene PNG-Datei liegt unter `outputs/figures/DataGraph.png`.
