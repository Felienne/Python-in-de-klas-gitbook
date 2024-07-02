# Les 8b

**1) Gebruikersinformatie**

In deze laatste les gaan we gebruikers aan de app toevoegen, zodat er meerdere mensen mee kunnen oefenen. Volg deze stappen:

1. Maak een extra label en een invoerveld. Deze moeten in beeld komen bij het opstarten van de app.
2. Maak na het klikken op de ok-knop een bestand voor deze gebruiker: `words-username.csv` dus bijvoorbeeld: `words-henkie.csv`en open dat bestand.

Dat gaan we zo aanpakken: \
\
Sla eerst de naam van de gebruiker en de bijbehorende bestandsnaam op in globale variabelen, zodat je er in het hele programma bij kan. De globals moeten op een losse regels!

```python
  global gebruikersnaam
  gebruikersnaam = gebruikersnaamveld.get()
  global bestandsnaam
  bestandsnaam = f'words{gebruikersnaam}.csv'
```

Volg dan deze stappen:

* Importeer deze libraries:\
  `import os.path, shutil`
* Maak een bestandsnaam aan met de fstrings die we hebben geleerd:\
  `bestandsnaam = f'words{gebruikersnaam}.csv'`

Test nu je code uit en kijk of je f-string klopt!!!

* Kijk nu of het bestand bestaat met: \
  `if not os.path.exists(bestandsnaam):`&#x20;
* Zo nee, kopieer het originele bestand:\
  &#x20;   `shutil.copy("words.csv", bestandsnaam)`
* Gebruik overal in het programma nu `bestandsnaam`in plaats van `"words.csv"`!!!

Verder kan het programma blijven werken zoals het al werkt.

**1b) Wachtwoord erbij (extra)**

Wil je het nog mooier maken? Maak dan een tweede label en veldje voor een wachtwoord. Sla de wachtwoorden op in een nieuw bestand en zoek het goede wachtwoord op!\
\
Tip! Wil je dat het er echt mooi uitziet als een wachtwoord? Gebruik dan deze code:\
\
`wachtwoordveld = Entry(root, show="*")`



**2) Statistieken voor alle gebruikers tonen**

Nu je meerdere gebruikers hebt, kun je bij het tonenveld ook statistieken laten zien over de scores van alle gebruikers, relatief aan de huidige gebruiker! Bijvoorbeeld:

* Het moeilijkste woord voor alle gebruikers (alle fouten in alle files bij elkaar opgeteld)
* Hoeveel woorden een gemiddelde gebruiker goed heeft versus deze gebruiker
* Hoeveel zinnen een gemiddelde gebruiker ingevoerd heeft versus deze gebruiker
* De lengte van de langste zin van alle gebruikers versus de huidige gebruiker

**3) Sla ook een datum op bij ieder antwoord**&#x20;

Als je dit nog niet gedaan had, kun je nu het tonen-venster uitgebreider maken met datum-informatie. Dat doen we door ook de datum van vandaag op te slaan als iemand een antwoord invoert. Daarmee kan je nog veel meer statistieken maken zoals:

* Aantal antwoorden goed vandaag, deze week, deze maand
* Aantal antwoorden fout vandaag, deze week, deze maand
* Welk woord het allerlangst geleden fout beantwoord is&#x20;

Volg deze stappen om de datum in te voeren:

1. Zet boven aan je code `import time`
2. Voeg nu bij het antwoorden de code `datum = date.today()` in
3. Sla de variabele ook op in je csv file door de rij aan te passen
4. Sla de variabele ook op in je csv file door de headers aan te passen

En, omdat je nu meerdere gebruikers hebt, kun je daar ook informatie over laten zien, bijvoorbeeld:

* Hoeveel gebruikers er deze maand, week of dag hebben gespeeld
* Of de huidige gebruiker vaker of minder vaak oefende dan gemiddeld!

