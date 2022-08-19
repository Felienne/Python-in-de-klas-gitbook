# Les 1b

### Opdracht 1

Deze opdracht wordt afgetekend als:

1. Je minstens 10 vragen in je code hebt staan
2. Je voor iedere vraag minstens 3 antwoordopties hebt bedacht

Voor deze opdracht ga je je weer verdiepen in je quiz van voor de vakantie. Kun je je code nog vinden op repl.it? Zoek je quizvragen van voor de vakantie op \(of verzin nieuwe!\). Maak nu voor voor iedere vraag minstens een aantal antwoordopties. Die opties zijn mogelijke antwoorden op de vraag. Het moeten natuurlijk wel een beetje zinnige opties zijn, dat een speler echt moet denken welke er goed zijn! Sla je opties op in een tweede lijst `opties` zoals je ook in de startcode ziet.

### Startcode

```python
import random

quizvragen = ['vraag 1', 'vraag 2'] #vul hier jouw vragen in!
opties = ['A)... B)...', 'A)... B)...'] #vul hier jouw antwoorden in!

#deze code hoef je niet aan te passen, die is alleen om je lijsten te testen
#als het goed is kun je deze code wel prima lezen natuurlijk...!

vraagnummer = random.randint(0, len(quizvragen)-1)
print(quizvragen[vraagnummer])
print("Kies uit")
print(opties[vraagnummer])
```

