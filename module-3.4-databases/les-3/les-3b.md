# Les 3b

**1) Personen en metroreizen**

Voor deze opdracht koppel je de tabellen Personen en Reizen aan elkaar zodat we goed kunnen zien wie er wanneer geeft gereisd. Er staat al wat code voor je klaar in [deze repl](https://replit.com/@mevrHermans/Pidk-K3-M2-L3b-1).

**2) Stations en metroreizen**

Voor deze opdracht koppel je de tabellen Personen en Stations aan elkaar zodat we goed kunnen zien wie waarnaar toe geeft gereisd.&#x20;

Je kan deze opdracht op 2 niveau's doen, kies zelf:

* Makkelijk: Koppel alleen de kolom Van

```sql
.print 'Reizen en Stations'
select *
from reizen, stations
-- where reizen.__ == stations.__
```

:warning:Tip! Kopieer deze code en, en run eerst de code zonder regel 4, en kijk hoe welke kolommen bij elkaar horen.

* Moeilijker: Koppel de tabel Stations twee keer en toon de naam van Van en van Naar.

```sql
.print 'Reizen en Stations'
select Naam, stations_van.Naam, __.Naam
from reizen, stations as stations_van, stations as __


```

:warning:Tip: Je moet stations twee keer in from zetten omdat het twee keer gekoppeld moet worden. -- Geef de tabel twee keer een andere naam, dat doe je met een `as`.



**3) Scheidsrechters en namen**

Voor deze opdracht gaan we met een nieuwe dataset werken. De database vind je [hier](https://replit.com/@mevrHermans/Pidk-K3-M2-L3b-3). Die dataset hebben we ook in Excel al gezien, het zijn voetbalwedstrijden met clubs en scheidsrechters.

Voor deze opdracht koppel je wedstrijden aan scheidsrechters. Er staat nu geen code klaar, die schrijf je zelf.



**4) Teams koppelen**

Voor deze opdracht koppel je wedstrijden aan team.&#x20;

Ook deze opdracht kan je opdracht op 2 niveau's doen, kies zelf:

* Makkelijk: Koppel alleen de kolom Team 1&#x20;
* Moeilijker: Koppel twee en toon de naam van Team 1 en van Team 2.

Er staat nu geen code klaar, maak de queries zelf.





