# BD-15 - Spark liest Wetterdaten aus Kafka

## Epic

Epic 5 - Kafka-Integration

## Notebook

`06_spark_read_kafka_weather.ipynb`

## Ziel

Spark soll Daten aus Kafka lesen und weiterverarbeiten.

## Aufgaben

- `SparkSession` erstellen.
- Kafka Topic `weather.observations` lesen.
- JSON-Value parsen.
- Schema definieren.
- Deduplizierung ueber Message-Key oder Lookup-Key umsetzen.
- Output speichern: `data/silver/weather_from_kafka.parquet`.

## Akzeptanzkriterien

- [x] Spark liest erfolgreich aus Kafka.
- [x] Kafka-JSON wird in DataFrame-Spalten umgewandelt.
- [x] Deduplizierung ist umgesetzt.
- [x] Ergebnis wird als Parquet gespeichert.

## Umsetzung

- Notebook: `notebooks/06_spark_read_kafka_weather.ipynb`
- Input: Kafka Topic `weather.observations`
- Verarbeitung: Spark liest das Topic als Batch-Snapshot, parst JSON mit explizitem Schema und dedupliziert ueber `match_id`.
- Output:
  - `data/silver/weather_from_kafka.parquet`
  - `outputs/tables/kafka_weather_read_status.csv`
- Konfiguration:
  - `KAFKA_BOOTSTRAP_SERVERS`
  - `KAFKA_WEATHER_TOPIC`
  - `SPARK_MASTER`
  - `SPARK_KAFKA_PACKAGE`

## Abhaengigkeiten

- BD-14
