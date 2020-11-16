# Les 5b

**Opdracht 1 : Maak de variabele antwoord**

Deze opdracht wordt afgetekend als:

1. Je een variabele `antwoord` hebt gemaakt waarin de aangeklikte letter is opgeslagen.
2. De variabele ook uitgeprint wordt na het klikken

**Uitleg.** Fork de startcode op [https://repl.it/@mevrHermans/pidk-jaar-2-les-4-opdr-1](https://repl.it/@mevrHermans/pidk-jaar-2-les-3-opdr-1). Die code is nog niet helemaal goed, jij gaat die code zelf stap voor stap verbeteren.

In deze voorbeeldcode ****printen we nu de aangeklikte letter uit. Dat is prima, maar we willen de letter ook nog in een variabele opslaan. Want dan kunnen we straks kijken of het aangeklikte antwoord goed is. 

Volg deze stappen: 

1. Zet bovenaan je code, vóór de while lus, een nieuwe variabele`antwoord`op 'geen'. 
2. Zorg ook dat de variabele na het klikken verandert. Dat doet je door onder de regel `print('A')`deze regel te zetten:

```python
antwoord = 'A'
```

{% hint style="info" %}
Let op! Zorg dat deze regel op dezelfde manier ingesprongen is als de regel erboven!
{% endhint %}

3. print de variabele `antwoord`onderin de while lus.

**Opdracht 2 : Controleer het antwoord**

Deze opdracht wordt afgetekend als:

1. Er bij een goed antwoord 'goed' geprint wordt en bij een fout antwoord 'fout'

**Uitleg.**  Voeg een if toe aan je code, waarmee je kijkt of het antwoord goed is. Volg deze stappen:

1. Maak een variabele `goede_antwoord` waarin je het goede antwoord van de vraag opslaat
2. Kijk met een if of het antwoord van de speler, in `antwoord`hetzelfde is als `goede_antwoord`

**Opdracht 3 : Reset de variabele**

Deze opdracht wordt afgetekend als je:

1. Na een goed of fout antwoord, de variabele `antwoord`weer op 'geen' gezet wordt.

**Uitleg.** Als de speler het antwoord nu goed of fout heeft, dan blijft dat de hele tijd zo. Dat is natuurlijk niet leuk. Zeker niet bij een fout antwoord. Daarom moet de variabele `antwoord` weer op 'geen' gezet worden, zodat het nog een keer geprobeerd kan worden.

```python
    if A.get_rect().collidepoint(locatie_muis):
      print('A')
```

Zorg dat deze regels wel in de buitenste if blijven staan. Er staat al een stukje commentaar op de goede plek voor je klaar:

```python
#vul hier de if voor de B in
```

Verander de A's in de B, en kijk of je code werkt. Let op! Je moet de A op twee plekken veranderen. 

Doe dan hetzelfde voor de C en de D.

**Opdracht 4 \(Extra\)**

Deze opdracht wordt afgetekend als:

1. Je een extra plaatje in beeld krijgt

**Opdracht.** Je kunt ook zelf nog iets in beeld krijgen, bijv. een smiley, een foto van jezelf of een "ik weet het niet" knop voor de speler. Voeg jij zelf nog iets toe aan je programma? Volg deze stappen:

1. Zoek een plaatje en sla het op op je computer
2. Upload het plaatje in repl.it met de drie kleine stippeltjes
3. Laad het plaatje en sla het op in een variable
4. "Blit" de variabele op het scherm, doe dat in de `while` lus

**Opdracht 5 \(Extra\)**

Deze opdracht wordt afgetekend als:

1. De letters van plek kunnen veranderen.

**Uitleg.** De letters blijven nu op dezelfde plek staan als ze worden aangeklikt. Je kan de quiz nog moeilijker maken, en leuker, als de letters nadat ze zijn aangeklikt, ergens anders weer in beeld komen. Dat kan op een random \(willekeurige\) plak zijn.

**Opdracht 6 \(Extra\)**

Deze opdracht wordt afgetekend als:

1. Je zelf iets nieuws verzonnen hebt, en gemaakt

**Opdracht.** Ben je klaar? Verzin dan zelf nog iets leuks! Bijv:

* Een aftelklok van 10 seconden waarbinnen de speler moet klikken.
* Andere letters of plaatjes om op te klikken, bijv een Appel voor A en een Banaan voor B

Maar het mag ook iets heel anders zijn!

