# Offentliga CMS och webbpubliceringsverktyg

Statistik över myndigheters och kommuners CMS och webbpubliceringsverktyg.
Denna analys är genomförd med syftet att undersöka vilka webbverktyg som används
på svenska kommuner och myndigheter.


## Resultat

Hela analysen finns redovisad i Jupyter-anteckningsboken `CMSdataanalys.ipynb`.

*Sammanfattning:*

* Det vanligaste webbpubliceringsverktyget hos kommuner är:
  * Sitevision (JSP) - 44.5%
  * EPIserver - 30.3%
  * Wordpress - 6.6 %



* Det vanligaste webbpubliceringsverktyget hos myndigheter är:
  * EPiServer 6.2 %
  * Drupal 2.6 %
  * SharePoint 1.8 %



## Insamlingsmetod

För att skanna kommunerna och myndigheternas hemsidor har jag använt
[WebAPP Information Gatherer](https://github.com/jekyc/wig) som jag har kört
mot de båda listorna över kommuners (`kommunURLs.txt`) och myndigheters
(`myndighetURLs.txt`) hemsidor.

För att snabba upp insamlingen kan man använda concurrent futures, se
skriptet `wigconcurrentmyndigheter.py`.


## Ytterligare data

* `data/MyndigheterLinks.csv` - Myndigheternas länkstrukturer.
* `data/MyndigheterNetwork.gexf` - Myndigheternas hemsidor som länknätverk. Kan öppnas med [Gephi](https://gephi.org) 
