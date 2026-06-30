# Projekt-Scope: Turniere und Team-Match-Ebene

Dieses Dokument fixiert den fachlichen Scope fuer die Pipeline-Notebooks. Es ist der menschlich lesbare Vertrag zu `data/reference/tournament_scope.json`; die JSON-Datei ist die maschinenlesbare Quelle fuer Filter, Checks und Tabellen.


## Turnierliste

| scope_id | Turnier | StatsBomb Competition | Season | Erwartete Matches | Erwartete Team-Match-Zeilen |
| --- | --- | --- | --- | ---: | ---: |
| `world_cup_2018` | WM 2018 | FIFA World Cup | 2018 | 64 | 128 |
| `world_cup_2022` | WM 2022 | FIFA World Cup | 2022 | 64 | 128 |
| `euro_2020` | Euro 2020 | UEFA Euro | 2020 | 51 | 102 |
| `euro_2024` | Euro 2024 | UEFA Euro | 2024 | 51 | 102 |
| `afcon_2023` | AFCON 2023 | Africa Cup of Nations | 2023 | 52 | 104 |
| `copa_america_2024` | Copa America 2024 | Copa America | 2024 | 32 | 64 |

Gesamterwartung: 6 Turniere, 314 Matches und 628 Team-Match-Zeilen.

## Hauptanalyse-Ebene

Die Hauptanalyse-Ebene ist `team_match`: Ein reales Fussballspiel wird als zwei Beobachtungen modelliert, eine pro Team. Dadurch koennen Wetter, Elo-Differenz und Gegnerstaerke je Team interpretiert werden.

Pflichtschluessel fuer Pipeline-Tabellen:

| Feld | Bedeutung |
| --- | --- |
| `match_id` | eindeutige Spiel-ID aus StatsBomb |
| `competition_name` | Wettbewerb, z. B. `FIFA World Cup` |
| `season_name` | Saison/Jahr, z. B. `2022` |
| `team_name` | Team dieser Beobachtungszeile |
| `opponent_name` | Gegner in demselben Match |
| `match_date` | Spieldatum |
| `venue_name` | Spielort fuer Wetter- und Geocoding-Schritte |

Qualitaetsregel: Jede `match_id` muss nach dem Feature-Building genau zwei Zeilen haben. Abweichungen werden als Data-Quality-Problem behandelt.

## Zielmetriken

| Metrik | Definition |
| --- | --- |
| `team_xg` | Summe des Shot-xG eines Teams in einem Match |
| `shots` | Anzahl der Schuesse eines Teams |
| `xg_per_shot` | `team_xg / shots`, falls `shots > 0` |
| `passes` | Anzahl der Pass-Events eines Teams |
| `pass_completion_rate` | erfolgreiche Paesse / alle Paesse, falls `passes > 0` |
| `pressures` | Anzahl der Pressure-Events eines Teams |
| `counterpressures` | Anzahl der Counterpressure-Events eines Teams |
| `duels` | Anzahl der Duel-Events eines Teams |
| `long_ball_share` | lange Paesse / alle Paesse, falls `passes > 0` |

## Verwendung in Pipeline-Notebooks

Alle fachlichen Pipeline-Notebooks lesen den Scope aus `data/reference/tournament_scope.json`. Besonders wichtig ist das fuer:

- `01_ingest_statsbomb.ipynb`: filtert Match- und Eventdaten auf genau diese Turniere.
- `07_build_team_match_features.ipynb`: prueft `expected_team_match_rows` und die Regel 1 Match = 2 Team-Match-Zeilen.
- `08_join_final_dataset.ipynb` und Analyse-Notebooks: interpretieren alle Ergebnisse auf Team-Match-Ebene.
