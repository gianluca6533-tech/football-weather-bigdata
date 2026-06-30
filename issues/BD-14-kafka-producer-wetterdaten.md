# BD-14 - Kafka Producer fuer Wetterdaten bauen

## Epic

Epic 5 - Kafka-Integration

## Notebook

`05_kafka_producer_weather.ipynb`

## Ziel

Bereinigte Open-Meteo Wetterdaten als Messages an Kafka senden.

## Aufgaben

- `weather_features.parquet` laden.
- Pro Wetterbeobachtung eine JSON-Message erzeugen.
- Message-Key setzen.
- Messages an Topic `weather.observations` senden.
- Sende-Status dokumentieren: Anzahl gesendete Messages, Anzahl Fehler und Beispiel-Message.

## Akzeptanzkriterien

- [x] Wetterdaten werden erfolgreich an Kafka gesendet.
- [x] Messages sind JSON-basiert.
- [x] Message-Key erlaubt spaetere Deduplizierung.
- [x] Notebook zeigt eine Beispiel-Message.

## Umsetzung

- Notebook: `notebooks/05_kafka_producer_weather.ipynb`
- Input: `data/silver/weather_features.parquet`
- Topic: `weather.observations`
- Message-Key: `match_id` als String
- Message-Value: JSON UTF-8 nach Schema aus `docs/kafka_topics.md`
- Konfiguration: `KAFKA_BOOTSTRAP_SERVERS`, lokal `kafka:29092`, Cluster spaeter `172.29.16.101:9092`
- Status-Artefakte:
  - `outputs/tables/kafka_weather_producer_status.csv`
  - `outputs/tables/kafka_weather_sample.csv`

## Abhaengigkeiten

- BD-13
