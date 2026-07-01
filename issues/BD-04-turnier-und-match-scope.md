# BD-04 - Turnier- und Match-Scope definieren

## Epic

Epic 2 - Datenquellen vorbereiten

## Notebook

`00_project_overview.ipynb`

## Ziel

Festlegen, welche Turniere und Spiele analysiert werden.

## Scope

- WM 2018
- WM 2022
- Euro 2020
- Euro 2024
- AFCON 2023
- Copa America 2024

## Aufgaben

- [x] Turnierliste definieren.
- [x] Erwartete Match-Anzahl je Turnier dokumentieren.
- [x] Team-Match-Logik festlegen: 1 Spiel = 2 Team-Match-Zeilen.
- [x] Zielmetriken definieren: `team_xg`, `shots`, `xg_per_shot`, `passes`, `pass_completion_rate`, `pressures`, `counterpressures`, `duels`, `long_ball_share`.

## Umsetzung

- `notebooks/00_project_overview.ipynb` dokumentiert Forschungsfrage, Turnier-Scope, erwartete Gesamtgroesse, Team-Match-Vertrag und Zielmetriken.
- `docs/project_scope.md` ist die lesbare Scope-Dokumentation fuer spaetere Arbeitsschritte.
- `data/reference/tournament_scope.json` ist die maschinenlesbare Quelle, die spaetere Notebooks fuer Filter und Validierungen verwenden.
- Der Scope folgt einer strukturierten DataFrame-/Tabellenarbeit mit klaren Pipeline-Artefakten und Trennung von Ingestion, Transformation und Analyse.

## Akzeptanzkriterien

- [x] Projekt-Scope ist klar dokumentiert.
- [x] Alle spaeteren Notebooks verwenden dieselbe Turnierliste.
- [x] Team-Match-Ebene ist als Hauptanalyse-Ebene festgelegt.

## Abhaengigkeiten

- BD-03
