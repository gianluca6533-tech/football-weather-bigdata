# BD-02 - Docker-Compose-Umgebung aufbauen

## Epic

Epic 1 - Projekt-Setup und Architektur

## Ziel

Eine lokale Umgebung mit Jupyter, Kafka und Spark vorbereiten.

## Aufgaben

- `docker-compose.yml` erstellen.
- Services definieren: Jupyter Notebook, Kafka Broker, Spark Master/Spark Worker oder Spark lokal im Jupyter Container.
- Volumes fuer `notebooks/`, `data/` und `outputs/` mounten.
- Pruefen, ob Jupyter Kafka und Spark erreichen kann.

## Akzeptanzkriterien

- [x] `docker compose up` startet die Umgebung.
- [x] Jupyter ist im Browser erreichbar.
- [x] Kafka ist erreichbar.
- [x] Eine `SparkSession` kann in einem Notebook gestartet werden.
- [x] Datenordner sind im Notebook sichtbar.

## Umsetzung

- `docker-compose.yml` im Projektroot erstellt.
- Jupyter nutzt das Image `jupyter/pyspark-notebook`, ergaenzt um gemountete Projektordner.
- Spark wird lokal im Jupyter-Container gestartet.
- Kafka laeuft als Single-Node-Broker im KRaft-Modus.
- `notebooks/environment_check.ipynb` prueft Datenordner, Kafka-Port und SparkSession aus Jupyter heraus.

## Verifikation

- `docker compose config --quiet` erfolgreich.
- `jq empty notebooks/environment_check.ipynb` erfolgreich.
- `docker compose up -d` konnte lokal noch nicht vollstaendig ausgefuehrt werden, weil der Docker-Daemon nicht erreichbar war: `Cannot connect to the Docker daemon`.

## Abhaengigkeiten

- BD-01
