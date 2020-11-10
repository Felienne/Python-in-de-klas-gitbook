# Les 3b

**Opdracht 1**

Deze opdracht wordt afgetekend als:

1. Je de vier letters weer in beeld hebt

**Uitleg.** Fork de startcode op [https://repl.it/@mevrHermans/pidk-jaar-2-les-2-opdr-1](https://repl.it/@mevrHermans/pidk-jaar-2-les-3-opdr-1). Die code is nog niet helemaal goed, jij gaat die code zelf stap voor stap verbeteren. Je begint net als vorige week maar met 1 letter. Zet jij alle vier de letters weer op een mooie plek?

**Opdracht 2**

Deze opdracht wordt afgetekend als:

1. Alle vier de letters aangeklikt kunnen worden
2. Je de letter waarop geklikt is, onderin in beeld krijgt

**Uitleg.** Als je nu op de letter A klikt, komt er A in beeld onderin, onder de PyGame codes.

![](../../.gitbook/assets/image%20%283%29.png)

Dat willen we graag voor alle letters, en dat ga jij programmeren. Kopieer deze twee regels code:

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

**Opdracht 3**

Deze opdracht wordt afgetekend als:

1. Je een variabele `antwoord` hebt gemaakt waarin de aangeklikte letter is opgeslagen.

**Uitleg.** We printen nu de aangeklikte letter uit. Dat is prima, maar we willen de letter ook nog in een variabele opslaan. Want dan kunnen we straks kijken of het aangeklikte antwoord goed is. Zorg dat de letter in een variabele komt. Die variabele noemen we `antwoord`. Zet bovenaan je code de variabele op 'geen'. Zorg ook dat de variabele na het klikken verandert. Dat doet je door onder de regel `print('A')`deze regel te zetten:

```python
antwoord = 'A'
```

{% hint style="info" %}
Let op! Zorg dat deze regel op dezelfde manier ingesprongen is als de regel erboven!
{% endhint %}

Lukt deze opdracht nog niet? Dat is niet erg! In de volgende les bespreken we deze code samen.

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

