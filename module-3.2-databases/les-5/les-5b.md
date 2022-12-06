# Les 5b

**Opdracht 1a) Maak de tabel personen**

Deze tabel krijgt de kolommen: nummer, voornaam en geslacht. Kopieer deze code en vul deze zelf aan op de streepjes.

```sql
create table __(
  Persoonsnummer __,
  __ TEXT,
  __ TEXT
);
```

Tip! deze code print alle tabellen uit. Als je het goed doet, komt er **personen** in beeld.

```sql
.tables
```

**Opdracht 1b) Maak de andere metro-tabellen**

Maak nu de andere tabellen voor de metroreizen

Het moet er zo uitzien:

Tabel: **personen** met kolommen: nummer, voornaam en geslacht&#x20;

Tabel: **stations** met kolommen: nummer en naam&#x20;

Tabel: **reizen** met kolommen: persoonsnummer, datum, tijd, van, naar

Vul deze code weer aan op de streepjes:

```sql

CREATE TABLE personen(
  __ __,
  __ __,
  __ __
);

CREATE TABLE stations(
  __ __,
  __ __
);

CREATE TABLE reizen(
  __ __,
  datum DATE,
  tijd TIME,
  __ __,
  __ __
);
```

Gebruik weer .`tables` om je tabellen te bekijken om te zien of alles gelukt is. Als je het goed doet, komt er **personen reizen stations** in beeld.

**2) Data toevoegen**

Nu we de tabellen hebben gemaakt kunnen we de tabellen vullen met data. Werk verder in je programma van opdrachten 1a en 1b.

Begin met deze code, en voeg in iedere tabel nog minstens 5 rijen toe. Je mag de data zelf verzinnen of overnemen uit de [slides van les 3](https://slides.com/felienne/pidk-k3-m2-l3#/19).

```sql
insert into personen values(1, _, _);

insert into stations values(38, __);

insert into reizen values('09/06/20', '10:48:00', __, __, __);
```

:warning: Tip? Ben je klaar? Gebruik deze codes om je tabellen te bekijken:

```sql
-- select *
-- from personen;

-- select *
-- from stations;

-- select *
-- from reizen;
```



**Opdracht 3) Voetbaltabellen**

Begin nu een nieuw programma voor de voetbaldata.&#x20;

Maak daarin de drie tabellen aan voor de voetbalwedstrijden. Je moet nu zelf de kolommen allemaal invullen

Tabel: **teams**, kolommen: teamnummer en Naam

Tabel: **scheidsrechters**, kolommen: nummer en Naam

Tabel: **wedstrijden**, kolommen: date, time, scheidsrechtersnummer, team\_1, team\_2, goals\_1, goals\_2

Begin met deze code en vul de streepjes in:

```sql
CREATE TABLE teams(
  __
);

CREATE TABLE scheidsrechters(
  __
);

CREATE TABLE wedstrijden (
  __
);
```

Als je het goed doet, komt er na het commando `.tables` dit in beeld: **scheidsrechters teams wedstrijden**

**4) Tabellen vullen voetbal**

Vul nu ook de voetbaltabellen met data. Verzin de data zelf of gebruik de laatste echte wedstrijden uit de eredivisie of het WK!

**5) Even terug naar het koppelen van data (X)**

Ga terug naar je programma over de metrodata.&#x20;

Koppel nu jouw eigen drie tabellen van de metroreizen aan elkaar.

Koppel 1x reizen aan personen om de naam van reizigers op te zoeken, en 2x reizen aan stations om de namen van stations te zoeken.

Selecteer ook de juiste kolommen! Als je dan een select schrijft, moet er zoiets uitkomen (maar dan natuurlijk voor jouw eigen data):

**Jan, Nesselande, Beurs**
**Piet, Coolhaven, Oostplein**

:warning: Tip? Je moet stations twee keer in from zetten omdat het twee keer gekoppeld moet worden. Geef de tabel twee keer een andere naam.

