# Les 2b

**Opdracht 1) Formules**

Open dit [programma](https://replit.com/@mevrHermans/Pidk-K3-M2-L2b-1). Gebruik nu formules om deze dingen te printen:

*   Het aantal aardbevingen in de dataset.

    Begin met deze code:

```sql
.header on
.mode column

.read database.sql

.print 'Aantal aardbevingen'
select count(__)
from earthquakes;
```

*   Gemiddelde magnitude.

    Begin met deze code:

```sql
.header on
.mode column

.read database.sql

-- .print 'Gemiddelde magnitude'
-- select __
-- from earthquakes;
```

* De minimale diepte. Schrijf deze query helemaal zelf.

**Opdracht 2) Conditionele formules**

Ook in deze opdracht werken we weer met de tabel van de aardbevingen, maar nu uit [dit programma](https://replit.com/@mevrHermans/Pidk-K3-M2-L2b-2).

Let op! Er zitten nu meerdere soorten in de dataset: earthquakes en Nuclear Explosions. Dat zie je in de Kolom **Soort.**

Maak formules voor deze zes berekeningen:

1.  Aantal rijen met magnitude groter dan 7

    Begin met deze code:

    ```sql
    .header on
    .mode column

    .read database.sql

    -- 1) Aantal Nuclear Explosions
    .print 'Aantal Nuclear Explosions'
    select *
    from earthquakes;
    ```
2. Aantal Nuclear Explosions
3. Gemiddelde magnitude van alle Nuclear Explosions
4. Gemiddelde latitude van alle Earthquakes
5. Gemiddelde longitude van alle Earthquakes
6. Aantal Earthquakes met magnitude groter dan 7

Tip: Voor query 6 heb je een 'and' nodig!

**Opdracht 3)**

Voer nu deze berekeningen uit voor een [dataset met toetsen](https://replit.com/@mevrHermans/Pidk-K3-M2-L2b-3).

:warning:Let op! Deze data is anders dan in het voorbeeld op de slides.

Maak formules voor deze zeven berekeningen:

1. Totaal van alle cijfers van toets 3
2. Gemiddelde cijfer van toets 2
3. Gemiddelde cijfer van de voldoendes van toets 3
4. Gemiddelde van de cijfers van meisjes voor toets 3
5. Aantal jongens in de klas
6. Aantal jongens met een onvoldoende
7. Aantal cijfers onder de 8 bij Gemiddelde

**Opdracht 4) Atletiekformules (X)**

Ook deze dataset hebben we eerder gezien in Excel, open deze [hier](https://replit.com/@mevrHermans/Pidk-K3-M2-L2b-4).

Maak formules voor deze zes berekeningen:

1\) Hoeveel kinderen zijn er gekwalificeerd?

2\) Wat is het gemiddelde aantal seconde dat alle kinderen over de hordeloop doen?

3\) Hoeveel kinderen doen er minder dan 50 minuten over de 10 kilometer?

4\) Wat is de gemiddelde afstand die meisjes halen met kogelstoten?

5\) Hoeveel jongens doen minder dan 5 minuten over de 1 kilometer?

6\) Wat is het aantal jongens dat niet gekwalificeerd is?

Vond je dit niet zo lastig? Maak dan deze extra sommen ook!

7\) Extra moeilijk: Wat is de snelste tijd op alledrie de afstanden bij elkaar? En wie heeft die snelste tijd behaald? Leg uit met commentaar hoe je het hebt uitgerekend.

8\) Extra extra moeilijk! Als we kijken naar het hordelopen en kogelstoten samen, wie doet het dan het allerbeste? En hoe heb je dat bepaald? Leg uit met commentaar hoe je het hebt uitgerekend.
