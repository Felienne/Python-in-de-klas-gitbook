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

Nu we weten welke woorden de gebruikeer wel en niet kent, gaan we de antwoorden opslaan in een de dictionary die bij de rij hoort. Dat doen we in een nieuw veld: 'bekend'. Zo sla je iets in dat veld op:

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

![](https://previews.dropbox.com/p/thumb/ABc-3mVSSgarLtuJKF1dlau-SSK0hl\_y8AZ3LxW9YXFJrhmEZ5pgkg6hjR-TNIl0pH3tdV0OUxEOdfwEzQAz9vyUwIT8TTK4mWbEZMAmgZdIWFsr8DdoU5WrcbezY-WMt8gXwkN-fUtRxNjwlbgNOQF1Wog4Ls\_itZO88qUBSxV4NCdoscK8UfA3ze6ZXmk2IezWxU7Xe9axIdzEXgrv6r8XnR1SnyGh7ocizHCzgIahyCa9w92uYnwftQCLkQDtfARjhsjZhCFffJcX4oKvGKykPWxbA4C\_Krgu0Z-63mz\_M\_Zem0CWhWJf2PBtrPd-IRQVpYD0ZBTygaZboH2m4eTTxAwAf\_IlwmfzvRvNKxJBifByFbv3Lu9d3rfUpPtZ3ps/p.png)

**Opdracht 4) Vang verkeerde invoer af (extra)**

In opdracht 1 heb je naar 3 mogeijkheden gekeken, maar soms maakt een gebruiker een typfout. Geef de melding "onbekende invoer" als de gebruiker iets onvpert dat niet ja, nee of stoppen is.

