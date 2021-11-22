# Les 1b

**Opdracht 1) Fork de startcode **

Deze opdracht wordt afgetekend als:

* Je naar [https://repl.it/@mevrHermans/simulatie-start](https://repl.it/@mevrHermans/simulatie-start) bent gegaan
* Je dit programma 'geforkt' hebt met de fork knop

Klik op het potloodje naast de naam van het programma. Klik dan op de grijze knop met fork erop. Je hebt nu een kopie van het programma gemaakt. Dat wordt vanzelf opgeslagen zodat je er steeds aan door kan werken.

![](../../.gitbook/assets/Les1-Afb1.png)

**Opdracht 2) Stel het veld in**

Deze opdracht wordt afgetekend als:

* Je simulatie werkt en alles in beeld komt

**Uitleg. **Er staat al wat code voor je klaar, je hoeft het alleen aan te passen.

```
breedte = 600
hoogte = __
​
screen = pygame.display.set_mode((breedte, hoogte))
​
schildpad = pygame.image.load('schildpad.png')
```

Als eerste pas je de grootte van het scherm aan bij hoogte en breedte. Je hoeft alleen een getal op de streepjes te zetten. Kijk eens goed naar het scherm. Wat is meer, de grootte of de breedte? Als de breedte 800 is wat zou dan (ongeveer) de hoogte zijn? Vul en getal in en probeer je code uit.

**Opdracht 3) Programmeer de honger-variabele**

Deze opdracht wordt afgetekend als:

* De honger van het dier (in de variabele `honger`) steeds hoger wordt.

**Uitleg.** Er is al een variabele honger aangemaakt, en die wordt ook al geprint, dat zie er zo uit:

![](<../../.gitbook/assets/image (4).png>)

Maar de variabele blijft nu steeds op 0 staan. Dat ga jij nu aanpassen.&#x20;

In de code staat al `# maak honger hier eentje meer` . Op die plek ga jij de variabele `honger` eentje meer maken. Weet je nog hoe dat moet?

**Opdracht 4) Beëindig de simulatie**

Deze opdracht wordt afgetekend als:

* De simulatie stopt als de honger van het dier 100 is geworden.&#x20;

De simulatie gaat nu eindeloos door. Dat klopt natuurlijk niet, als een dier geen voedsel vindt, dat moet de simulatie stoppen. Er staat al wat code voor je klaar, de while lus bijvoorbeeld, die stopt al vanzelf als de variabele `dier_leeft` op `False` gezet wordt.

Ga naar de regel code waar dit staat: `# als de honger meer is dan 100, zet dier_leeft dan op False`

Maak daar een if die kijkt of `honger` meer is dan 100. Als het meer is, zet de variabele dier\_leeft dan op False.

{% hint style="info" %}
Denk aan de hoofdletter bij False. Met een kleine letter werkt het niet.
{% endhint %}

**Opdracht 5) Doe onderzoek voor jouw eigen simulatie**

Deze opdracht wordt afgetekend als:

* Je een dier hebt gekozen die in jouw simulatie voor gaan komen
* Je voldoende onderzoek hebt gedaan over de snelheid en leefsituatie van het dier. Denk bijvoorbeeld aan: snelheid, leefstijl (alleen of in een groep), voedsel, waterbehoefte.
* Je deze informatie hebt samengevat in je schrift of in een bestand op de computer

**Uitleg**

Later in de lessen gaan we de schildpad en de krop sla veranderen in een dier die jij mag kiezen. Ga nu informatie gaan zoeken over dieren. Kies een dier uit en een voedsel van dat dier. Zoek ook informatie uit over de leeromgeving van je dier.

#### **Opdracht 6) **Laad je eigen plaatjes in

Deze opdracht wordt afgetekend als:

* Je je eigen dierenplaatje hebt gezocht en ingeladen in je simulatie
* Je de namen van de variabeles netjes hebt aangepast naar jouw dier en voedsel.

**Uitleg** Je hebt als het goed is al een dier gekozen. Zoek nu op internet goede plaatjes op van dat dier.

**Let op!** Je mag plaatjes niet zomaar pakken.

Denk aan de Google-regels van mevr. Hermans en stel je zoekresultaten in via Tools - Usage Rights - Labeled for reuse.

Upload de plaatjes naar je simulatie en pas de code aan zodat die plaatjes worden ingeladen.

Pas ook de variabelenamen aan! Het is niet netjes als er `schildpad_rechthoek` in jouw code staat, staat terwijl je bijv. een antilope inlaadt. Daar kun je van in de war raken.



