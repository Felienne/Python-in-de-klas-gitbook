# Les 6b

** Opdracht 1) Ook de gedeeld door heeft voorrang**

Deze opdracht wordt afgetekend als:

* Je ook sommen met een / goed kan uitrekenen. Gedeeld door komt ook voor + en -

**Uitleg. **Sommen met een / nog niet goed, dan gaan we dat nu samen verbeteren. Kijk bijvoorbeeld eens naar deze som: 5 + 10 / 5

Daar moet 7 uitkomen want gedeeld door gaat voor. Dus eerst 10/5, dat is 2 en die 2 wordt dan opgeteld bij de 5. Maar in onze rekenmachine gaat dat niet goed. Wij gaan van links naar rechts, dus we krijgen 5 + 10 dat is 15 gedeeld door 5 is 3.

We gaan dit samen in stapjes doen. Volg deze stappen:

1. Begin bij deze code `if '*' in som_onderdelen:`Die code kijkt nu alleen of er een \* in de som zit.
2. Zet in deze if nog een if die kijkt of er **ook** een / in de `som_onderdelen` zit.
   1. Zo ja? Als er een \* en een / in de som zitten, moet je kijken welke er het meest vooraan staat, want die moet eerst. Dat kun je bekijken door wie de laagste index heeft.
   2. Zo nee? Dan ga je nog kijken of er in de som alleen een \* zit (zoals we al deden)
   3. Zit er geen keer in? Dan kijken nog even of er alleen een / in zit. Dat lijkt op de code die we al hadden maar dan voor de gedeeld door.&#x20;

Succes! En vergeet je code niet te testen met veel verschillende sommen.

**Opdracht 2)  Met of zonder kommagetal?**

Deze opdracht wordt afgetekend als:

* Je kommagetallen uitprint met een punt, maar gehele getallen zonder punt

**Uitleg. **Tot nu hebben we steeds alle getallen afgerond. Dus als je 10/5 uitrekende, kreeg je mooi 2. Maar als je 10/3 deed, dan kreeg je 3. Dus geen 3.333333.... . Dat gaan we nu oplossen!

Laten we eens beginnen met het weghalen van de `round` in deze regel code:

```
  som_onderdelen.insert(begin, str(round(antwoord)))
```

Probeer dat eens en kijk wat er gebeurt. 10/3 wordt nu 3.333333 dus dat is prima! Maar nu krijgen we bij 10/2 5.0 en dat is weer niet zo mooi. Dat moet gewoon 5 worden!

Dat gaan we oplossen door te kijken of het afgerond getal en het getal zelf hetzelfde zijn. Voor 2 is dat zo want 2.0 is hetzelfde getal als 2. Maar voor 3.333333 is dat niet zo want dan is het afgeronde getal 3. Zet deze code onder de regels met `pop()`.

```
  if round(antwoord) == antwoord:
    antwoord = round(antwoord)
```



