# Präsentationsstruktur

Diese Outline bereitet die finale Präsentation für das Football-Weather-Big-Data-Projekt vor. Sie folgt der Forschungsfrage aus dem README:

> Wie haengen Wetterbedingungen und Teamstärke mit Spielstil und Chancenqualität bei internationalen Fußballturnieren zusammen?

Die Story bleibt auf der Team-Match-Ebene: Ein reales Spiel wird als zwei Team-Beobachtungen modelliert. Dadurch können Wetter, Elo-Differenz, Spielstil und Chancenqualität aus Sicht jedes Teams verglichen werden.

## Folienspiegel

| Nr. | Folie | Kernaussage | Grafik oder Tabelle |
| --- | --- | --- | --- |
| 1 | Titel und Forschungsfrage | Wetter und Teamstärke werden gemeinsam betrachtet: Wie haengen sie mit Spielstil und Chancenqualität zusammen? | GitHub-Link, Gruppennamen |
| 2 | Daten und Analyseaufbau | StatsBomb-Events, Open-Meteo-Wetter und Elo-Ratings werden zu einem Team-Match-Dataset verbunden. | `outputs/figures/presentation_analysis_flow.png` |
| 3 | Datensatz und Scope | Turniere, Matches und Team-Match-Zeilen geben Kontext, bevor Ergebnisse interpretiert werden. | `outputs/figures/presentation_dataset_scope.png` |
| 4 | Wetter im Datensatz | Temperatur variiert sichtbar zwischen Turnieren; Regen ist vorhanden, aber eine kleine Gruppe. | `outputs/figures/presentation_weather_distribution.png`, optional `outputs/figures/rain_share.png` |
| 5 | Teamstärke | Favoriten erzeugen im Median mehr xG als Außenseiter; Elo ist der Vergleichsanker. | `outputs/figures/presentation_xg_by_elo_group.png` |
| 6 | Wetter und Intensität | Pressures nach Temperaturgruppe zeigen Median und Streuung lesbarer als ein Scatterplot. | `outputs/figures/presentation_pressures_by_temperature_group.png` |
| 7 | Wetter und Ballkontrolle | Passquote und Long-Ball-Share zeigen, ob Wetter eher Präzision oder Spielanlage beruehrt. | `outputs/figures/presentation_ball_control_weather.png` |
| 8 | Wetter und Chancenqualität | Team-xG unterscheidet sich zwischen Temperaturgruppen nur vorsichtig interpretierbar. | `outputs/figures/presentation_xg_by_temperature_group.png` |
| 9 | Modellvergleich | Elo erklärt für Team-xG und erfolgreiche Pässe deutlich mehr Varianz als Wetter. | `outputs/figures/presentation_model_r2_comparison.png`, `outputs/tables/model_comparison.csv` |
| 10 | Fazit | Wetter ist als Kontext sichtbar, aber Teamstärke ist der stärkere Erklärungsfaktor. | `outputs/tables/model_incremental_comparison.csv` |

## Foliennotizen

### 1. Motivation und Forschungsfrage

Kernaussage: Internationale Turniere finden unter sehr unterschiedlichen klimatischen Bedingungen statt. Die Präsentation fragt nicht, ob Wetter Spiele allein entscheidet, sondern ob Wetter messbar mit Spielstil, Intensität und Chancenqualität zusammenhängt.

Sprecher-Notizen:

- Forschungsfrage knapp einordnen: Wetterbedingungen und Teamstärke werden gemeinsam betrachtet.
- Team-Match-Ebene erklaeren: Jedes Spiel wird aus Sicht beider Teams analysiert.
- Den Big-Data-Bezug ueber mehrere Quellen, Pipeline und reproduzierbare Artefakte setzen.

### 2. Datenbasis

Kernaussage: Die Analyse kombiniert drei Datenwelten: StatsBomb für Spielereignisse, Open-Meteo für Wetter und Elo-Ratings für relative Teamstärke.

Sprecher-Notizen:

- StatsBomb liefert Events wie Schuesse, xG, Paesse, Pressures und Duels.
- Open-Meteo liefert Temperatur, gefuehlte Temperatur und Niederschlag am Spielort.
- Elo wird zu `elo_diff = team_elo - opponent_elo`; dadurch ist Teamstärke immer relativ zum Gegner.
- Der Data-Quality-Output zeigt, dass der finale Join ohne fehlende Wetter- oder Elo-Werte laeuft.

### 3. Wetterverteilung

Kernaussage: Die Wetterdaten haben genug Streuung für eine explorative Analyse. Temperatur und gefuehlte Temperatur sind besonders brauchbar; Regen ist vorhanden, aber ungleich verteilt.

Sprecher-Notizen:

- Aus `bd19_weather_distribution_summary.csv`: Temperatur reicht von 12.2 bis 38.6 °Celsius, Median 25.5 Grad.
- Gefuehlte Temperatur reicht von 7.5 bis 37.6 °Celsius.
- Regen hat Median 0.0 mm und Mittelwert 0.10 mm; deshalb Regenbefunde defensiv formulieren.
- Wichtig: Für Wetterverteilung wird auf Match-Ebene dedupliziert, damit jedes Spiel nur einmal zählt.

### 4. Spielstil nach Turnier

Kernaussage: Die Turniere unterscheiden sich sichtbar in Spielstilmetriken. Diese Unterschiede sind wichtig, weil Wettereffekte sonst mit Turnierkontext verwechselt werden koennten.

Sprecher-Notizen:

- xG, Passquote und Pressures zeigen unterschiedliche Turnierprofile.
- Angekommene Paesse ergaenzen die Passquote, weil sie Ballkontroll-Volumen statt nur Präzision zeigen.
- Die Folie ist der Story-Anker vor den Wetterfolien: Erst zeigen, dass Spielstil ueberhaupt variiert.

### 5. Teamstärke

Kernaussage: Teamstärke ist ein zentraler Vergleichsfaktor. Favoriten, ausgeglichene Teams und Außenseiter können sich in xG und Ballkontrolle unterscheiden.

Sprecher-Notizen:

- Elo-Gruppen sind keine absolute Wertung, sondern relativ zum Gegner.
- Diese Folie bereitet die Modellfolie vor: Wenn Elo viel erklärt, duerfen Wetterplots nicht ueberinterpretiert werden.
- Besonders passend: `xg_by_elo_group.png` und `successful_passes_by_elo_group.png`.

### 6. Wetter und Intensität

Kernaussage: Intensität wird ueber Pressures, Counterpressures und Duels operationalisiert. Die Plots zeigen explorative Muster, keine Kausalitaet.

Sprecher-Notizen:

- Scatterplots nutzen kontinuierliche Temperaturwerte; Boxplots verdichten Temperaturgruppen.
- Regen wird mit einer 0.5-mm-Schwelle gruppiert: bis 0.5 mm gilt als kein/kaum Regen, darueber als messbarer Regen.
- Kleine Regen-Gruppe betonen, damit die Interpretation nicht zu stark klingt.

### 7. Wetter und Ballkontrolle

Kernaussage: Ballkontrolle wird nicht nur ueber Passquote gelesen. Erfolgreiche Paesse, Carries und Long-Ball-Share zeigen, ob sich auch Spielanlage und Volumen veraendern.

Sprecher-Notizen:

- Passquote allein kann taeuschen, weil wenige sichere Paesse eine hohe Quote ergeben können.
- Erfolgreiche Paesse zeigen mehr Ballkontroll-Volumen.
- Long-Ball-Share ist eine gute Zusatzmetrik für Regen: Bei schwierigen Bedingungen koennte direkter gespielt werden.

### 8. Wetter und Chancenqualität

Kernaussage: Chancenqualität wird bewusst von Schussanzahl getrennt. `xg_per_shot` misst die durchschnittliche Qualitaet eines Abschlusses, `shots` das Volumen und `xg` die Kombination aus beidem.

Sprecher-Notizen:

- Temperatur vs. `xg_per_shot` ist der Kernplot für Chancenqualität.
- `xg_by_temperature_group.png` zeigt Team-xG, also Qualitaet plus Volumen.
- Regenplots sind praesentationsfreundlich, aber wegen weniger messbarer Regenfaelle vorsichtig zu lesen.

### 9. Wetter vs. Teamstärke

Kernaussage: Im Modellvergleich erklärt Elo deutlich mehr Varianz in `team_xg` und `successful_passes` als Wettervariablen.

Sprecher-Notizen:

- Aus `model_comparison.csv`: Bei Team-xG hat Wetter allein R² 0.0032 und Elo allein R² 0.0752; bei erfolgreichen Pässen hat Wetter allein R² 0.0288 und Elo allein R² 0.2625.
- Adjusted R² ist wichtig, weil groessere Modelle für zusätzliche Variablen bestraft werden.
- Koeffizientenplot nur als Richtung und relative Staerke lesen, nicht als kausalen Effekt.

### 10. Fazit

Kernaussage: Das Projekt zeigt eine reproduzierbare Big-Data-Pipeline und eine vorsichtige Analyse. Wetter ist als Kontext sichtbar, Teamstärke ist für `team_xg` im Modellvergleich klar stärker.

Sprecher-Notizen:

- Technisches Fazit: mehrere Quellen, Kafka/Spark-Schritt, Gold-Dataset, reproduzierbare Outputs.
- Fachliches Fazit: Wetterverteilung ist ausreichend für Exploration; Regen bleibt wegen geringer Haeufigkeit eingeschraenkt.
- Methodisches Fazit: Die Analyse zeigt Zusammenhaenge, keine kausalen Beweise.
- Abschluss-Satz: Die stärkste Präsentationsbotschaft ist nicht "Wetter entscheidet Spiele", sondern "Wetter ist Kontext, Teamstärke bleibt der deutlich stärkere Erklärungsfaktor".

## Quellen im Projekt

- `README.md`: Forschungsfrage, Datenquellen, Pipeline-Idee.
- `docs/notebook_data_flow.md`: Notebook-Vertrag und Data-Flow-Regeln.
- `docs/project_scope.md`: Turnier-Scope und Team-Match-Ebene.
- `issues/BD-19-wetterverteilung-analysieren.md` bis `issues/BD-25-regressionsmodelle-vergleichen.md`: Analyse- und Modellierungsanforderungen.
- `notebooks/09_eda_weather_distribution.ipynb`: Wetterverteilung.
- `notebooks/10_analysis_style_intensity.ipynb`: Spielstil, Teamstärke, Intensität und Ballkontrolle.
- `notebooks/11_analysis_chance_quality_model.ipynb`: Chancenqualität und Modellvergleich.
- `notebooks/12_final_presentation_graphics.ipynb`: Finale Präsentationsgrafiken und Fazit-Story.
