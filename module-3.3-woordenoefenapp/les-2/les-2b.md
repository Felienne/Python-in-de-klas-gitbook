# Les 2b

De app die we gaan maken kent straks twee fases:&#x20;

1. Woorden selecteren
2. Woorden oefenen

In deze les gaan we alleen nog aan het stuk van woorden selecteren werken.&#x20;

**Opdracht 1) Stoppen met woorden laten zien**

Begin met [deze repl](https://replit.com/@mevrHermans/pidk-k3-m3-l2b1-1). Voeg nu en if-elif-in voor deze 3 gevallen:

1. Het anwoord is ja -> print **goed zo**
2. Het antwoord is nee -> print **jammer**
3. Het antwoord is stoppen -> stop de loop met `break`

**Opdracht 2) Antwoord opslaan in een dict**

Nu we weten welke woorden de gebruiker wel en niet kent, gaan we de antwoorden opslaan in een de dictionary die bij de rij hoort. Dat doen we in een nieuw veld: 'bekend'. Zo sla je iets in dat veld op:

`rij['bekend'] = 'ja'`

Sla nu ja op in het veld bekend als de gebruiker ja type en nee als hij nee typt. \
\
Je mag de prints laten staan als je wilt, dat kan handig zijn om te _debuggen_.

**Opdracht 3) Dict opslaan in een bestand**

Iedere rij in de ductionary heeft nu een extra veldje 'Bekend'. Dat wordt een extra kolom in het csv bestand.

Plak deze code onderaan je bestand, buiten de loop (dus zonder inspringen!)

Maak de code nu af door op de streepjes de kolommen in de vullen en een nieuwe bestandnaam

```
# sla de woorden weer op met ja of nee in de laatste kolom
headers = [____, _____, _____, _____] #vul hier de kolomnamen in, de bestaande kolommen PLUS 'Bekend'

with open(___, 'w') as csvfile: #kies hier een nieuwe bestandsnaam
  writer = csv.DictWriter(csvfile, fieldnames=headers)
  writer.writeheader()
  writer.writerows(woordlijst)
```

Voer de code uit en kijk of alles goed is gegaan, met andere woorden of jouw data in het nieuwe bestand staat. Zo ziet het er uit als alles goed is (maar bij jou kunnen de ja's en nee's natuurlijk op andere plekken staan)

![](<../../.gitbook/assets/image (13).png>)

In opdracht 1 heb je naar 3 mogelijkheden gekeken, maar soms maakt een gebruiker een typfout. Geef de melding "onbekende invoer" als de gebruiker iets invoert dat niet _ja_, _nee_ of _stoppen_ is.

