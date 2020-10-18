# Les 2b

**Opdracht 1**

Deze opdracht wordt afgetekend als:

1. Het scherm netjes ingesteld is op 600 bij 800 
2. De achtergrondkleur van het veld zwart is
3. De kleur van de tekst wit is

**Uitleg.** Fork de startcode op [https://repl.it/@mevrHermans/pidk-jaar-2-les-2-opdr-1](https://repl.it/@mevrHermans/pidk-jaar-2-les-2-opdr-1). Die code is nog niet helemaal goed, jij gaat die code zelf stap voor stap verbeteren.

Voor de eerste opdracht ga jij de instellingen goed zetten. Stel de grootte van het scherm in op 600 hoog en 800 breed. Zet ook de beide kleuren goed. Dat gaat met RGB \(Rood Groen Blauw\) codes. Ken je die nog uit het eerste jaar? Als de de getallen goed instelt krijg je een zwarte achtergrond met witte letters erop. Probeer je code uit om te kijken of het goed is!

**Startcode**

Het startprogramma is [online](https://repl.it/@mevrHermans/pidk-jaar-2-les-2-opdr-1) te vinden. Deze code kun je voor alle opdrachten van deze week gebruiken.

**Opdracht 2**

Deze opdracht wordt afgetekend als:

1. Je vier letters in beeld hebt
2. Die letters netjes op de hoeken van het scherm staan

**Uitleg.** De code zet nu een letter A op het scherm, maar we willen alle vier de letters in beeld. Dan kunnen spelers er straks op klikken.   
  
We doen de letter B stap voor stap. Er zijn twee regels in de code die je moet kopiëren op de letter B ook in beeld te krijgen. Dat zijn deze twee regels. Ten eerste:

```python
A = pygame.image.load("A.png")
```

Deze regels laadt het plaatje "A.png" in en slaat het plaatje op in de variabele A. Verander beide A's en B's.  
Alleen deze regel is nog niet genoeg om de B op het scherm te krijgen. Probeer de code maar eens, er staat nog steeds alleen een A. Deze regel, in de `while` lus is ook nog nodig:

```python
  screen.blit(A, (0, 0))
```

Deze regel code zet de variable A op het scherm, op plekje \(0,0\). \(0, 0\) betekent links bovenaan. 

{% hint style="info" %}
**Let op!** Verander de A in een B, maar verander ook de getallen!! Als je de getallen op \(0, 0\) laat staan, zie je alleen de B, die op de A geplakt wordt.
{% endhint %}

**Opdracht 3 \(Extra\)**

Deze opdracht wordt afgetekend als:

1. Je iets extra's in beeld krijgt

**Opdracht.** Je kunt ook zelf nog iets in beeld krijgen, bijv. een smiley, een foto van jezelf of een "ik weet het niet" knop voor de speler. Voeg jij zelf nog iets toe aan je programma? Volg deze stappen:

1. Zoek een plaatje en sla het op op je computer
2. Upload het plaatje in repl.it met de drie kleine stippeltjes
3. Laad het plaatje en sla het op in een variable
4. "Blit" de variabele op het scherm, doe dat in de `while` lus

