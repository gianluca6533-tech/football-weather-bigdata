# Praesentationsstruktur

Diese Outline bereitet die finale Praesentation fuer das Football-Weather-Big-Data-Projekt vor. Sie folgt der Forschungsfrage aus dem README:

> Wie haengen Wetterbedingungen und Teamstaerke mit Spielstil und Chancenqualitaet bei internationalen Fussballturnieren zusammen?

Die Story bleibt auf der Team-Match-Ebene: Ein reales Spiel wird als zwei Team-Beobachtungen modelliert. Dadurch koennen Wetter, Elo-Differenz, Spielstil und Chancenqualitaet aus Sicht jedes Teams verglichen werden.

## Folienspiegel

| Nr. | Folie | Kernaussage | Grafik oder Tabelle |
| --- | --- | --- | --- |
| 1 | Motivation und Forschungsfrage | Wetter wird als Kontextfaktor fuer Spielstil, Intensitaet und Chancenqualitaet untersucht; Teamstaerke dient als zentrale Kontrollgroesse. | `outputs/figures/DataGraph.png` |
| 2 | Datenbasis | Das Projekt verbindet StatsBomb-Eventdaten, Open-Meteo-Wetterdaten und Elo-Ratings zu einem finalen Team-Match-Dataset. | `outputs/figures/DataGraph.png`, `outputs/tables/data_quality_summary.csv` |
| 3 | Wetterverteilung | Die Spiele decken kuehle bis heisse Bedingungen ab; Regen ist vorhanden, aber seltener und daher vorsichtig zu interpretieren. | `outputs/figures/weather_temperature_histogram.png`, `outputs/figures/weather_temperature_by_tournament.png`, `outputs/figures/rain_share.png` |
| 4 | Spielstil nach Turnier | Turniere unterscheiden sich sichtbar in xG, Passquote, angekommenen Paessen und Pressingintensitaet. | `outputs/figures/xg_by_tournament.png`, `outputs/figures/pass_completion_by_tournament.png`, `outputs/figures/pressures_by_tournament.png` |
| 5 | Teamstaerke | Elo-Gruppen zeigen, ob Favoriten, ausgeglichene Teams und Aussenseiter unterschiedliche Spielprofile haben. | `outputs/figures/xg_by_elo_group.png`, `outputs/figures/pass_completion_by_elo_group.png`, `outputs/figures/successful_passes_by_elo_group.png` |
| 6 | Wetter und Intensitaet | Pressures und Duels werden als Intensitaetsmetriken gegen Temperatur- und Regenbedingungen gelesen. | `outputs/figures/temperature_vs_pressures.png`, `outputs/figures/pressures_by_temperature_group.png`, `outputs/figures/pressures_rain_vs_no_rain.png`, `outputs/figures/duels_by_temperature_group.png` |
| 7 | Wetter und Ballkontrolle | Passquote, erfolgreiche Paesse und Long-Ball-Share zeigen, ob Wetter eher Praezision, Volumen oder Spielanlage betrifft. | `outputs/figures/temperature_vs_pass_completion.png`, `outputs/figures/pass_completion_by_temperature_group.png`, `outputs/figures/pass_completion_rain_vs_no_rain.png`, `outputs/figures/long_ball_share_rain_vs_no_rain.png` |
| 8 | Wetter und Chancenqualitaet | `xg_per_shot` trennt Chancenqualitaet vom Schussvolumen; Regenvergleiche bleiben wegen kleiner Regen-Gruppe explorativ. | `outputs/figures/temperature_vs_xg_per_shot.png`, `outputs/figures/xg_by_temperature_group.png`, `outputs/figures/xg_rain_vs_no_rain.png`, `outputs/figures/shots_rain_vs_no_rain.png` |
| 9 | Wetter vs. Teamstaerke | Die Regressionsmodelle vergleichen Wettervariablen, Elo-Differenz und kombinierte Modelle; Adjusted R2 verhindert eine Ueberbewertung groesserer Feature-Sets. | `outputs/figures/model_r2_comparison.png`, `outputs/figures/model_coefficients.png`, `outputs/tables/model_comparison.csv` |
| 10 | Fazit | Wetter liefert beschreibende Kontextsignale, Teamstaerke erklaert im Modellvergleich aber deutlich mehr Varianz in `team_xg`; starke kausale Aussagen waeren nicht gerechtfertigt. | `outputs/tables/model_incremental_comparison.csv`, optionale Wiederholung von `outputs/figures/DataGraph.png` |

## Foliennotizen

### 1. Motivation und Forschungsfrage

Kernaussage: Internationale Turniere finden unter sehr unterschiedlichen klimatischen Bedingungen statt. Die Praesentation fragt nicht, ob Wetter Spiele allein entscheidet, sondern ob Wetter messbar mit Spielstil, Intensitaet und Chancenqualitaet zusammenhaengt.

Sprecher-Notizen:

- Forschungsfrage knapp einordnen: Wetterbedingungen und Teamstaerke werden gemeinsam betrachtet.
- Team-Match-Ebene erklaeren: Jedes Spiel wird aus Sicht beider Teams analysiert.
- Den Big-Data-Bezug ueber mehrere Quellen, Pipeline und reproduzierbare Artefakte setzen.

### 2. Datenbasis

Kernaussage: Die Analyse kombiniert drei Datenwelten: StatsBomb fuer Spielereignisse, Open-Meteo fuer Wetter und Elo-Ratings fuer relative Teamstaerke.

Sprecher-Notizen:

- StatsBomb liefert Events wie Schuesse, xG, Paesse, Pressures und Duels.
- Open-Meteo liefert Temperatur, gefuehlte Temperatur und Niederschlag am Spielort.
- Elo wird zu `elo_diff = team_elo - opponent_elo`; dadurch ist Teamstaerke immer relativ zum Gegner.
- Der Data-Quality-Output zeigt, dass der finale Join ohne fehlende Wetter- oder Elo-Werte laeuft.

### 3. Wetterverteilung

Kernaussage: Die Wetterdaten haben genug Streuung fuer eine explorative Analyse. Temperatur und gefuehlte Temperatur sind besonders brauchbar; Regen ist vorhanden, aber ungleich verteilt.

Sprecher-Notizen:

- Aus `bd19_weather_distribution_summary.csv`: Temperatur reicht von 12.2 bis 38.6 Grad Celsius, Median 25.5 Grad.
- Gefuehlte Temperatur reicht von 7.5 bis 37.6 Grad Celsius.
- Regen hat Median 0.0 mm und Mittelwert 0.10 mm; deshalb Regenbefunde defensiv formulieren.
- Wichtig: Fuer Wetterverteilung wird auf Match-Ebene dedupliziert, damit jedes Spiel nur einmal zaehlt.

### 4. Spielstil nach Turnier

Kernaussage: Die Turniere unterscheiden sich sichtbar in Spielstilmetriken. Diese Unterschiede sind wichtig, weil Wettereffekte sonst mit Turnierkontext verwechselt werden koennten.

Sprecher-Notizen:

- xG, Passquote und Pressures zeigen unterschiedliche Turnierprofile.
- Angekommene Paesse ergaenzen die Passquote, weil sie Ballkontroll-Volumen statt nur Praezision zeigen.
- Die Folie ist der Story-Anker vor den Wetterfolien: Erst zeigen, dass Spielstil ueberhaupt variiert.

### 5. Teamstaerke

Kernaussage: Teamstaerke ist ein zentraler Vergleichsfaktor. Favoriten, ausgeglichene Teams und Aussenseiter koennen sich in xG und Ballkontrolle unterscheiden.

Sprecher-Notizen:

- Elo-Gruppen sind keine absolute Wertung, sondern relativ zum Gegner.
- Diese Folie bereitet die Modellfolie vor: Wenn Elo viel erklaert, duerfen Wetterplots nicht ueberinterpretiert werden.
- Besonders passend: `xg_by_elo_group.png` und `successful_passes_by_elo_group.png`.

### 6. Wetter und Intensitaet

Kernaussage: Intensitaet wird ueber Pressures, Counterpressures und Duels operationalisiert. Die Plots zeigen explorative Muster, keine Kausalitaet.

Sprecher-Notizen:

- Scatterplots nutzen kontinuierliche Temperaturwerte; Boxplots verdichten Temperaturgruppen.
- Regen wird mit einer 0.5-mm-Schwelle gruppiert: bis 0.5 mm gilt als kein/kaum Regen, darueber als messbarer Regen.
- Kleine Regen-Gruppe betonen, damit die Interpretation nicht zu stark klingt.

### 7. Wetter und Ballkontrolle

Kernaussage: Ballkontrolle wird nicht nur ueber Passquote gelesen. Erfolgreiche Paesse, Carries und Long-Ball-Share zeigen, ob sich auch Spielanlage und Volumen veraendern.

Sprecher-Notizen:

- Passquote allein kann taeuschen, weil wenige sichere Paesse eine hohe Quote ergeben koennen.
- Erfolgreiche Paesse zeigen mehr Ballkontroll-Volumen.
- Long-Ball-Share ist eine gute Zusatzmetrik fuer Regen: Bei schwierigen Bedingungen koennte direkter gespielt werden.

### 8. Wetter und Chancenqualitaet

Kernaussage: Chancenqualitaet wird bewusst von Schussanzahl getrennt. `xg_per_shot` misst die durchschnittliche Qualitaet eines Abschlusses, `shots` das Volumen und `xg` die Kombination aus beidem.

Sprecher-Notizen:

- Temperatur vs. `xg_per_shot` ist der Kernplot fuer Chancenqualitaet.
- `xg_by_temperature_group.png` zeigt Team-xG, also Qualitaet plus Volumen.
- Regenplots sind praesentationsfreundlich, aber wegen weniger messbarer Regenfaelle vorsichtig zu lesen.

### 9. Wetter vs. Teamstaerke

Kernaussage: Im Modellvergleich erklaert Elo deutlich mehr Varianz in `team_xg` als Wettervariablen. Wetter bringt nach Kontrolle fuer Elo nur einen sehr kleinen Zusatzbeitrag.

Sprecher-Notizen:

- Aus `model_comparison.csv`: Wetter allein hat R2 0.0015, Elo allein R2 0.0752, Wetter plus Elo R2 0.0768.
- Adjusted R2 ist wichtig, weil groessere Modelle fuer zusaetzliche Variablen bestraft werden.
- Koeffizientenplot nur als Richtung und relative Staerke lesen, nicht als kausalen Effekt.

### 10. Fazit

Kernaussage: Das Projekt zeigt eine reproduzierbare Big-Data-Pipeline und eine vorsichtige Analyse. Wetter ist als Kontext sichtbar, Teamstaerke ist fuer `team_xg` im Modellvergleich klar staerker.

Sprecher-Notizen:

- Technisches Fazit: mehrere Quellen, Kafka/Spark-Schritt, Gold-Dataset, reproduzierbare Outputs.
- Fachliches Fazit: Wetterverteilung ist ausreichend fuer Exploration; Regen bleibt wegen geringer Haeufigkeit eingeschraenkt.
- Methodisches Fazit: Die Analyse zeigt Zusammenhaenge, keine kausalen Beweise.
- Abschluss-Satz: Die staerkste Praesentationsbotschaft ist nicht "Wetter entscheidet Spiele", sondern "Wetter ist Kontext, Teamstaerke bleibt der deutlich staerkere Erklaerungsfaktor".

## Quellen im Projekt

- `README.md`: Forschungsfrage, Datenquellen, Pipeline-Idee.
- `docs/notebook_data_flow.md`: Notebook-Vertrag und Data-Flow-Regeln.
- `docs/project_scope.md`: Turnier-Scope und Team-Match-Ebene.
- `issues/BD-19-wetterverteilung-analysieren.md` bis `issues/BD-25-regressionsmodelle-vergleichen.md`: Analyse- und Modellierungsanforderungen.
- `notebooks/09_eda_weather_distribution.ipynb`: Wetterverteilung.
- `notebooks/10_analysis_style_intensity.ipynb`: Spielstil, Teamstaerke, Intensitaet und Ballkontrolle.
- `notebooks/11_analysis_chance_quality_model.ipynb`: Chancenqualitaet und Modellvergleich.
