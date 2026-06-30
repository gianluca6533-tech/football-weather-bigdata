# BD-18 - Data Quality Checks fuer finales Dataset

## Epic

Epic 6 - Spark Feature Engineering und Final Dataset

## Notebook

`08_join_final_dataset.ipynb`

## Ziel

Sicherstellen, dass das finale Dataset verlaesslich ist.

## Aufgaben

- Pruefen: doppelte Team-Match-Zeilen, fehlende Match-IDs, fehlende Wetterwerte, fehlende Elo-Werte, unrealistische Temperaturen, negative xG-Werte und Passquoten ausserhalb `0-1`.
- Kritische Fehler bereinigen oder begruenden.
- Data-Quality-Summary speichern: `outputs/tables/data_quality_summary.csv`.

## Umsetzung

Die Data-Quality-Regeln werden in `08_join_final_dataset.ipynb` nach dem finalen Join ausgefuehrt. Die Summary wird als `outputs/tables/data_quality_summary.csv` gespeichert.

Geprueft werden:

- doppelte Team-Match-Zeilen
- fehlende Match-IDs
- fehlende Wetterwerte
- fehlende Elo-Werte
- unrealistische Temperaturen ausserhalb `-30` bis `55` Grad Celsius
- negative xG-Werte
- Passquoten ausserhalb `0-1`

Kritische Befunde fuehren zu einer Assertion. Wenn keine Befunde auftreten, dokumentiert die Summary fuer jede Regel `status = pass` und begruendet, dass keine Bereinigung noetig war.

## Akzeptanzkriterien

- [x] Qualitaetsprobleme sind sichtbar.
- [x] Kritische Fehler werden bereinigt oder begruendet.
- [x] Finales Dataset ist analysebereit.

## Abhaengigkeiten

- BD-17
