# Les 4b

**Opdracht 1: Haal je parameters naar boven**

We hebben nu al een paar "knopjes" gemaakt waar je aan kan draaien:

* temperatuur
* hoeveel je gaat splitsen
* (optioneel) hoeveel random opties je kiest&#x20;

We gaan de code wat opruimen, zo:

* Zet je parameters bovenaan de code, zodat je makkelijker kan spelen met de instellingen
* Print je parameters uit, zodat je bij je uitvoer goed kan zien welke instelling je gebruikt hebt

**Opdracht 2: Jullie eigen data zoeken**

We willen natuurlijk geen Alice in Wonderland uitspugen maar iets dat klinkt zoals jezelf. Het is nu echt tijd om naar jouw eigen data te gaan kijken!\
\
Ga op zoek naar de data die je kan vinden en zorg dat je die in een tekstformaat (.txt) zet. Denk aan:

* Email
* Verslagen op Google Drive
* Opdrachten op Magister
* Social media met tekst (Instagram, Twitter)

Kopieer natuurlijk niet met de hand, maar zoek naar export-opties. Veel systemen hebben zo'n optie.&#x20;

**Opdracht 3: Jullie eigen data inlezen**

Je hebt nu waarschijnlijk niet een bestand maar een aantal bestanden. Pas je code aan zodat `lines`niet alleen uit een bestand bestaat maar uit de regels van meerdere bestanden. Zo gaat ongeveer zo:

```python
directory = 'mijn-data'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    for regel in open(f).readlines():
        ___ # hier de code die je al had
```

**Opdracht 4: Kijk twee woorden vooruit**

Als we betere zinnen willen maken, moeten we verder vooruit kijken. Niet een woordje, maar twee. Dat doe je door steeds twee woordjes aan elkaar te plakken. Dat wordt samen de key in je dictionary.

Bekijk nu de uitvoer goed! Worden de zinnen beter? En hoe zien de statistieken eruit?

**Opdracht 5: Vooruitkijken met een parameter (extra!)**

Je kan nu niet makkelijk terug naar één woordje vooruit. Voeg ook een parameter toe voor het vooruit kijken zodat je makkelijk kan kiezen tussen een of twee woordjes vooruit.
