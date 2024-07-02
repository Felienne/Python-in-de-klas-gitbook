# Les 4b

**1) Personen en metroreizen (herhaling)**

Voor deze opdracht koppel je de tabellen Personen en Reizen aan elkaar zodat we goed kunnen zien wie er wanneer geeft gereisd. Er staat al wat code voor je klaar in [deze repl](https://replit.com/@mevrHermans/Pidk-K3-M2-L3b-1).

**2) Stations en metroreizen (herhaling)**

Voor deze opdracht koppel je de tabellen Personen en Stations aan elkaar zodat we goed kunnen zien wie waarnaar toe geeft gereisd.

Je kan deze opdracht op 2 niveau's doen, kies zelf:

* Makkelijk: Koppel alleen de kolom Van

```sql
.print 'Reizen en Stations'
select *
from reizen, stations
-- where reizen.__ == stations.__
```

:warning:Tip! Kopieer deze code en, en run eerst de code zonder regel 4, en kijk hoe welke kolommen bij elkaar horen.

**3) Personen en metroreizen (X)**

Voor sommigen van deze opdrachten moet je koppelen én ook formules gebruiken!

Pluis zelf uit hoe dit moet. Maak dan deze queries:

1. Het aantal reizen gemaakt door meisjes
2. Het aantal reizen naar Poortugaal
3. Het aantal reizen van en naar Poortugaal
4. De naam van de persoon die het vaakst naar Delfshaven is gereisd
5. In welke tijdsperiode reizen jongens het vaakst?

* Nacht (van 00:00 tot 6:00)
* Ochtend (van 06:00 tot 12:00)
* Middag (van 12:00 tot 18:00)
* Avond (van 18:00 tot 0:00)

**4)** **Queries over de voetbaldata (X)**

Voor sommigen van deze opdrachten moet je koppelen én ook formules gebruiken! Pluis zelf uit hoe dit moet. Schrijf dan deze queries:

1. Het aantal keren gelijkspel
2. Het gemiddelde verschil tussen de scores Tip: Daarvoor moet je de absolute waarde berekenen omdat soms de een groter is en dan de ander. Dat kan met ABS()
3.  Het grootste verlies dat Scheidsrechter nummer 3 gefloten heeft

    Tip: Dit kan met of zonder koppelen, kies zelf wat je wilt

    Koppelen is natuurlijk moeilijker, dus leuker!
4. De grootste winst van Ado (Nu moet je wel koppelen!)
5. De naam van de scheidsrechter die het vaaks verlies gefloten heeft
6. De naam van de club die het vaakst gewonnen heeft
7. De naam van de club die het vaakst verloren heeft op zondag
8. De naam van de club die het vaakst verloren heeft op zondagavond (na 18:00 noemen we avond)
