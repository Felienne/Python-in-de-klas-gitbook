# Les 4b

**Opdracht 1**

Deze opdracht wordt afgetekend als:

1. Je alle code voor A hebt veranderd zodat de rechthoek meedoet
2. Je dus A onderin in beeld krijgt als je op de A klikt.

**Uitleg.** Pak jouw code van vorige week. Om te kijken of er op een letter wordt geklikt gebruikte jij `A.get_rect().collidepoint()` om te kijken of er op de A werd geklikt. Dat werkte wel voor de A maar niet voor de andere letters. In de les heb je gezien hoe je dat moet verbeteren. Volg deze 5 stappen:

1. Maak bovenaan de code een nieuwe variabele
2. Sla in de variabele `A_rechthoek` de rechthoek van A op met `A.get_rect()`
3. Stel het midden van de letter a, `A_rechthoek.center` in op (100,100)
4. blit de A in `A_rechthoek`, in plaats van directe op een locatie zoals in je oude code
5. Gebruik in de if `get_rect().collidepoint()` in plaats van `A_rechthoek.collidepoint`

Als je klaar bent, ziet het  er zo uit als je op de A klikt:

![](<../../.gitbook/assets/image (3) (1).png>)

**Opdracht 2**

Deze opdracht wordt afgetekend als:

1. De letters B, C en D **ook** aangeklikt kan worden
2. Je de letter waarop geklikt is, onderin in beeld krijgt

Herhaal nu de 5 stappen voor alle andere letters. Let op deze dingen. Het kan helpen om ze af te strepen als je ze gedaan hebt:

* Kopieer de code die je in stap 1 gemaakt hebt, alle 5 de regels!
* Verander alle A's in B's. Ook in de variabelen!
* Verander de plaats waar de B komt met `B_rechthoek.center`. Anders komen alle letters op elkaar.

Zet de if-code op de juiste plek neer, en zorg dat deze regels wel in de buitenste if blijven staan. Er staat al een stukje commentaar op de goede plek voor je klaar:

```python
# vul hier code in om te kijken of er op de A geklikt is
```

**Opdracht 3**

Deze opdracht wordt afgetekend als:

1. Je een variabele `antwoord` hebt gemaakt waarin de aangeklikte letter is opgeslagen.

**Uitleg.** We printen nu de aangeklikte letter uit. Dat is prima, maar we willen de letter ook nog in een variabele opslaan. Want dan kunnen we straks kijken of het aangeklikte antwoord goed is. Zorg dat de letter in een variabele komt. Die variabele noemen we `antwoord`. Zet bovenaan je code de variabele op 'geen'. Zorg ook dat de variabele na het klikken verandert. Dat doet je door de regel `print('A')`te vervangen door:

```python
antwoord = 'A'
```

{% hint style="info" %}
Let op! Zorg dat deze regel op dezelfde manier ingesprongen is als de regel erboven!
{% endhint %}

Lukt deze opdracht nog niet? Dat is niet erg! In de volgende les bespreken we deze code samen.

**Opdracht 4 (Extra)**

Deze opdracht wordt afgetekend als:

1. Je een extra plaatje in beeld krijgt

**Opdracht.** Je kunt ook zelf nog iets in beeld krijgen, bijv. een smiley, een foto van jezelf of een "ik weet het niet" knop voor de speler. Voeg jij zelf nog iets toe aan je programma? Volg deze stappen:

1. Zoek een plaatje en sla het op op je computer
2. Upload het plaatje in repl.it met de drie kleine stippeltjes
3. Laad het plaatje en sla het op in een variable
4. "Blit" de variabele op het scherm, doe dat in de `while` lus

**Opdracht 5 (Extra)**

Deze opdracht wordt afgetekend als:

1. De letters van plek kunnen veranderen.

**Uitleg.** De letters blijven nu op dezelfde plek staan als ze worden aangeklikt. Je kan de quiz nog moeilijker maken, en leuker, als de letters nadat ze zijn aangeklikt, ergens anders weer in beeld komen. Dat kan op een random (willekeurige) plak zijn.

**Opdracht 6 (Extra)**

Deze opdracht wordt afgetekend als:

1. Je zelf iets nieuws verzonnen hebt, en gemaakt

**Opdracht.** Ben je klaar? Verzin dan zelf nog iets leuks! Bijv:

* Een aftelklok van 10 seconden waarbinnen de speler moet klikken.
* Andere letters of plaatjes om op te klikken, bijv een Appel voor A en een Banaan voor B

Maar het mag ook iets heel anders zijn!
