# BD-13 - Kafka Topics definieren

## Epic

Epic 5 - Kafka-Integration

## Notebook

`05_kafka_producer_weather.ipynb`

## Ziel

Kafka als zentralen Broker fuer mindestens eine Datenquelle verwenden.

## Vorgeschlagene Topics

- `weather.observations`
- Optional: `elo.ratings`
- Optional: `team.match.metrics`

## Aufgaben

- Topic-Namen definieren.
- Message-Key definieren, fuer Wetter z. B. `match_id` oder `weather_lookup_key`.
- Message-Schema dokumentieren.
- Entscheiden, welche Quelle ueber Kafka laeuft.
- Empfehlung umsetzen: Wetterdaten ueber Kafka schicken, weil jede Wetterbeobachtung als einzelne JSON-Message gut passt.

## Akzeptanzkriterien

- [x] Kafka Topic ist erstellt.
- [x] Message-Schema ist dokumentiert.
- [x] Topic ist im Data-Flow eingezeichnet.

## Umsetzung

- Aktives Topic: `weather.observations`
- Datenquelle ueber Kafka: bereinigte Wetterdaten aus `data/silver/weather_features.parquet`
- Message-Key: `match_id` als String, weil `match_id` im Wetterdatensatz eindeutig ist und spaeter direkt fuer Deduplizierung und Joins genutzt wird.
- Message-Format: JSON UTF-8 mit Schema in `docs/kafka_topics.md`
- Lokale Topic-Konfiguration: 1 Partition, Replication Factor 1 fuer den Single-Node-Broker aus `docker-compose.yml`
- Data-Flow: `04_ingest_weather_openmeteo.ipynb` -> `05_kafka_producer_weather.ipynb` -> Kafka Topic `weather.observations` -> `06_spark_read_kafka_weather.ipynb`

Hinweis: Kafka war lokal aktiv und das Topic wurde mit `kafka-topics.sh --create --if-not-exists` angelegt.

## Abhaengigkeiten

- BD-02
- BD-12
