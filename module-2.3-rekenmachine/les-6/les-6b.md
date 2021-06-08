# Les 6b

 **Opdracht 1\) Ook de gedeeld door heeft voorrang**

* Deze opdracht wordt afgetekend als:

  Je ook sommen met een / goed kan uitrekenen. Gedeeld door komt ook voor + en -

  Misschien heb je deze opdracht vorige les al gedaan? Dan mag je deze nu overslaan. 

**Uitleg.** Sommen met een / nog niet goed, dan gaan we dat nu samen verbeteren. Kijk bijvoorbeeld eens naar deze som: 5 + 10 / 5

Daar moet 7 uitkomen want gedeeld door gaat voor. Dus eerst 10/5, dat is 2 en die 2 wordt dan opgeteld bij de 5. Maar in onze rekenmachine gaat dat niet goed. Wij gaan van links naar rechts, dus we krijgen 5 + 10 dat is 15 gedeeld door 5 is 3.



**Opdracht 5\) Ook de gedeeld door heeft voorrang \(extra\)**

Deze opdracht wordt afgetekend als:

* Je ook sommen met een / kan uitrekenen. Gedeeld door komt ook voor + en -

**Uitleg.** Ook delen gaat voor plus en min. Kun jij zorgen dat dat ook werkt in je rekenmachine? Dat is een pittige klus, maar wel heel leuk als het lukt. Weet je al hoe je dat gaat doen? Ga er dan maar voor!

Heb je nog geen idee? Deze stappen zou ik volgen:

1. Begin bij deze code `if '*' in som_onderdelen:`Die code kijkt nu alleen of er een \* in de som zit.
2. Zet in deze if nog een if die kijkt of er **ook** een / in de som\_onderdelen zit.
   1. Zo ja? Als er een \* en een / in de som zitten, moet je kijken welke er het meest vooraan staat, want die moet eerst. Dat kun je bekijken door wie de laagste index heeft.
   2. Zo nee? Dan ga je nog kijken of er in de som alleen een \* zit \(zoals we al deden\)
   3. Zit er geen keer in? Dan kijken nog even of er alleen een / in zit. Dat lijkt op de code die we al hadden maar dan voor de gedeeld door. 

Succes! En vergeet je code niet te testen met veel verschillende sommen.

