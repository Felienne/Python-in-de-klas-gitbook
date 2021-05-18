# Les 3a

**Replace()**

In de vorige les moesten we perse een spatie invoeren tussen de getallen en de operatoren (de symbolen zoals plus of keer). Dat is natuurlijk niet zo handig, want als je dat per ongeluk vergeet dan komt er een foutmelding.


Om dat op te lossen gaan we `replace()` leren. Replace is Engels voor vervangen. Met `replace()`kun je in een string een stukje tekst vervangen door een ander stukje tekst. 

Bijvoorbeeld, als je in de variabele `tekst` de tekst **hallo naam** hebt staan, en je doet daarna een `tekst.replace('naam', 'piet')` dan is de variabele tekst veranderd in **hallo piet**. Probeer deze code maar eens uit!

```
tekst = 'hallo naam'
tekst =  tekst.replace('naam', 'piet')


print(tekst)
```

**Sommen zonder spaties**

We kunnen  `replace()` gebruiken om de som een beetje voor te bereiden. Dat noemen we met een moeilijk woord "preprocessing". We zoeken in de som een operator op, en dan vervangen we die door de operator met spaties eromheen.


Dus de som `5+4` wordt dan: `5 + 4`. Omdat de som daarna mooi spaties heeft rondom de operator, kunnen we die nu met `split()`opdelen!

We doen dat in de opdrachten eerst even voor de plus, en daarna voor de andere operatoren.
