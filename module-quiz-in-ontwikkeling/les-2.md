# Les 2

#### Noot: bij deze les horen nog geen slides, want deze les is alleen in het computerlokaal gedaan vanwege een extra toets op 15 januari 2020.

#### Opdracht 1b-1\) Nu ook met klikken voor 1 dier

Deze opdracht wordt afgetekend als:

* Je pas tekst in beeld krijg als je op een plaatje klikt

**Opdracht.**  
  
Er komt nu tekst in beeld meteen als je een plaatje raakt. In het spel dat we voor het bedrijf gaan maken willen we ook dat er geklikt moet worden. Dat kan natuurlijk ook. Voeg deze code toe in je while True lus:

```text
knoppen = pygame.mouse.get_pressed()
```

Knoppen is nu een lijstje met knoppen die ingedrukt zijn. De eerste knop is de linkermuisknop. Nu kun je met knoppen\[0\] == 1 kijken of de muis is ingedrukt. Verander de if die je had in deze regel:

```text
  if knoppen[0] == 1 and zebra_rechthoek.collidepoint(locatie_muis):
      print('zebra')
```

#### Opdracht 2b-1\) Nu ook met klikken voor alle dieren of plaatjes

Deze opdracht wordt afgetekend als:

* Je de naam van alle drie jouw plaatjes print als erop geklikt wordt met de muis

**Opdracht.**  
In het programma tot nu toe heb je maar voor 1 plaatje gekeken of de muis erop klikt. Jij moet dit nu voor alledrie de plaatjes programmeren. Je hoeft voor nu alleen de naam van het plaatje te printen, zoals in het voorbeeld ook gedaan is.

#### 

#### Opdracht 3b-1\) Programmeer een actie

Deze opdracht wordt afgetekend als:

* Er iets gebeurt als je een plaatje aanklikt met de muis

**Opdracht.**  
Kies nu een actie die gebeurt als je een plaatje aanraakt. Je mag die actie zelf kiezen, bijv. het plaatje groter maken, bewegen, knipperen of wat je maar kan verzinnen.

#### Opdracht 4b-1\) Eigen stempeldoel

Deze opdracht wordt afgetekend als:

* Je zelf een doel hebt bedacht, en dat hebt uitgevoerd

**Uitleg.** Verzin zelf iets wat er nog bij kan in je programma. Een achtergrond? Een extra dier? Een kangaroe met een bokshandschoen? Bedenk iets en schrijf dat op.   
Voer het vervolgens netjes uit. Vraag wel eerst of mevr. Hermans of meneer van Ooijen je doel goed vindt.





