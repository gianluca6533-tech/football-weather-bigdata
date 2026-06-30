# Kafka Topic Specification

Dieses Dokument definiert die Kafka-Schnittstelle fuer Epic 5. Producer, Topic
und Consumer werden als getrennte Rollen behandelt. Fuer dieses Projekt laeuft
zuerst nur die Wetterquelle ueber Kafka, weil jede Match-Wetterbeobachtung gut
als einzelne JSON-Message modellierbar ist.

## Verbindungsdaten

| Umgebung | Bootstrap Server | Verwendung |
| --- | --- | --- |
| Docker/Jupyter | `kafka:29092` | Notebooks im Jupyter-Container |
| Host | `localhost:9092` | lokale CLI-Checks vom Rechner |
| Cluster | `172.29.16.101:9092` | Kafka-Broker in der Cluster-Umgebung |

Notebooks lesen den Bootstrap Server aus `KAFKA_BOOTSTRAP_SERVERS` und fallen
standardmaessig auf `kafka:29092` zurueck.

## Topic-Katalog

| Topic | Status | Producer | Consumer | Zweck |
| --- | --- | --- | --- | --- |
| `weather.observations` | aktiv | `05_kafka_producer_weather.ipynb` | `06_spark_read_kafka_weather.ipynb` | eine bereinigte Wetterbeobachtung pro Match |

Optionale Erweiterungen wie `elo.ratings` oder `team.match.metrics` werden nicht
fuer die Mindestanforderung benoetigt. Im Projekt wird bewusst nur ein Namensstil
verwendet. Deshalb wird `weather_observations` nicht parallel als zweites Topic
angelegt.

## Topic `weather.observations`

### Topic-Konfiguration

| Einstellung | Wert | Begruendung |
| --- | --- | --- |
| Partitions | `1` | reproduzierbare lokale Ausfuehrung und einfache Reihenfolge fuer die Abgabe |
| Replication Factor | `1` | Single-Node-Kafka aus `docker-compose.yml` |
| Retention | Broker-Default | Datensatz ist klein und kann aus Parquet reproduziert werden |
| Value Format | JSON UTF-8 | standardisiertes, in Spark mit Schema parsbares Message-Format |

Erstellung lokal:

```bash
docker compose exec -T kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create --if-not-exists \
  --topic weather.observations \
  --partitions 1 \
  --replication-factor 1
```

Pruefung lokal:

```bash
docker compose exec -T kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --describe --topic weather.observations
```

### Message-Key

Der Kafka-Key ist `match_id` als String, zum Beispiel `"7525"`.

Gruende:

- `match_id` ist in den vorhandenen Wetterdaten eindeutig. Die erwartete Anzahl
  kommt aus `data/reference/tournament_scope.json` und betraegt im aktuellen Scope 314
  Zeilen bzw. 314 unterschiedliche Match-IDs.
- Spark kann im Kafka-Read-Schritt mit `match_id` deduplizieren und direkt gegen
  Team-Match-Features joinen.
- `weather_lookup_key` ist fuer API-Caching nuetzlich, aber nicht eindeutig pro
  Match: mehrere Matches koennen denselben Ort/Tag-Key teilen.

### JSON-Value-Schema

Der Producer liest `data/silver/weather_features.parquet` und sendet pro Zeile
eine JSON-Message mit diesem stabilen Schema:

| Feld | Typ | Pflicht | Beschreibung |
| --- | --- | --- | --- |
| `match_id` | integer | ja | eindeutige StatsBomb-Spiel-ID |
| `match_date` | string | ja | Spieldatum im Format `YYYY-MM-DD` |
| `kick_off` | string | ja | Kickoff-Zeit aus StatsBomb |
| `kickoff_timestamp` | string | ja | kombinierter Kickoff-Zeitstempel als ISO-8601-String |
| `weather_time` | string | ja | ausgewaehlter Open-Meteo-Stundenzeitstempel als ISO-8601-String |
| `hours_from_kickoff` | number | ja | Abstand der Wetterstunde zum Kickoff |
| `weather_lookup_key` | string | ja | Cache-/API-Key aus Datum, Latitude und Longitude |
| `stadium_id` | integer | ja | StatsBomb-Stadion-ID |
| `stadium_name` | string | ja | Stadionname |
| `city_name` | string | ja | Stadt des Spielorts |
| `country_name` | string | ja | Land des Spielorts |
| `latitude` | number | ja | Geokoordinate des Spielorts |
| `longitude` | number | ja | Geokoordinate des Spielorts |
| `openmeteo_timezone` | string | ja | von Open-Meteo verwendete Zeitzone |
| `temperature_c` | number | ja | Temperatur in Grad Celsius |
| `feels_like_c` | number | ja | gefuehlte Temperatur in Grad Celsius |
| `precipitation_mm` | number | ja | Niederschlag in Millimetern |
| `rain_mm` | number | ja | Regenmenge in Millimetern |
| `rain_flag` | boolean | ja | `true`, wenn `rain_mm > 0` |
| `temperature_group` | string | ja | `cold`, `mild`, `warm` oder `hot` |
| `weather_missing_flag` | boolean | ja | markiert fehlende Wetterwerte |
| `tournament_short_name` | string | ja | Kurzname des Turniers |
| `competition_name` | string | ja | Wettbewerb |
| `season_name` | string | ja | Saison |
| `schema_version` | string | ja | aktuell `weather_observation.v1` |

`weather_request_url` bleibt absichtlich ausserhalb der Kafka-Message. Die URL
ist fuer Debugging in der Silver-Tabelle hilfreich, aber fuer Spark-Parsing,
Join und Analyse nicht notwendig.

Beispiel-Message:

```json
{
  "match_id": 7525,
  "match_date": "2018-06-14",
  "kick_off": "15:00:00.000",
  "kickoff_timestamp": "2018-06-14T15:00:00",
  "weather_time": "2018-06-14T15:00:00",
  "hours_from_kickoff": 0.0,
  "weather_lookup_key": "2018-06-14__55.75204__37.61781",
  "stadium_id": 255,
  "stadium_name": "Stadion Luzhniki",
  "city_name": "Moscow",
  "country_name": "Russia",
  "latitude": 55.75204,
  "longitude": 37.61781,
  "openmeteo_timezone": "Europe/Moscow",
  "temperature_c": 15.5,
  "feels_like_c": 12.7,
  "precipitation_mm": 0.0,
  "rain_mm": 0.0,
  "rain_flag": false,
  "temperature_group": "mild",
  "weather_missing_flag": false,
  "tournament_short_name": "WM 2018",
  "competition_name": "FIFA World Cup",
  "season_name": "2018",
  "schema_version": "weather_observation.v1"
}
```

### Producer-Vertrag

`05_kafka_producer_weather.ipynb`:

- liest `data/silver/weather_features.parquet`,
- erstellt das Topic mit AdminClient oder prueft, ob es existiert,
- kann das Topic mit `KAFKA_RESET_WEATHER_TOPIC=true` vor einem lokalen Demo-Lauf neu anlegen,
- serialisiert Zeitstempel als ISO-8601-Strings,
- sendet `key=str(match_id)` und JSON-Value an `weather.observations`,
- dokumentiert gesendete Messages, Fehleranzahl und eine Beispiel-Message.

### Consumer-Vertrag

`06_spark_read_kafka_weather.ipynb`:

- liest `weather.observations` ueber Spark Kafka Source,
- castet `key` zu `match_id`,
- parst `value` mit explizitem Spark-Schema,
- dedupliziert ueber `match_id`,
- weist wiederholte Producer-Laeufe im Status als entfernte Duplikate aus,
- schreibt `data/silver/weather_from_kafka.parquet`.
