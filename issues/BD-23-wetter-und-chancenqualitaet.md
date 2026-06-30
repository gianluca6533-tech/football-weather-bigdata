# BD-23 - Wetter und Chancenqualitaet analysieren

## Epic

Epic 7 - Explorative Analyse und Visualisierungen

## Notebook

`11_analysis_chance_quality_model.ipynb`

## Ziel

Untersuchen, ob Wetter eher mit Chancenqualitaet als mit Toren zusammenhaengt.

## Metriken

- Team-xG
- Shots
- xG pro Schuss
- Open-Play-xG, falls verfuegbar

## Aufgaben

- Scatterplot Temperatur vs. xG pro Schuss erstellen.
- Scatterplot gefuehlte Temperatur vs. xG pro Schuss erstellen.
- Boxplot xG nach Temperaturgruppe erstellen.
- Boxplot xG bei Regen vs. kein Regen erstellen.
- Optional Shots bei Regen vs. kein Regen visualisieren.
- Outputs speichern: `outputs/figures/temperature_vs_xg_per_shot.png`, `outputs/figures/feels_like_vs_xg_per_shot.png`, `outputs/figures/xg_by_temperature_group.png`, `outputs/figures/xg_rain_vs_no_rain.png`, `outputs/figures/shots_rain_vs_no_rain.png`.

## Akzeptanzkriterien

- [x] Chancenqualitaet wird getrennt von reiner Schussanzahl betrachtet.
- [x] Wettervergleiche sind sichtbar.
- [x] Notebook enthaelt kurze Interpretation.

## Abhaengigkeiten

- BD-18
- BD-19
