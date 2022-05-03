# Les 3b

De app die we gaan maken kent straks twee fases:&#x20;

1. Woorden selecteren
2. Woorden oefenen

In deze les werken we nog even verder aan het selecteren van woorden, maar treffen we ook wat voorbereidingen voor het werken met de twee fases.

**Opdracht 1) Meerdere keren selecteren**

Ga verder met je replit van vorige les. Als je het programma nu nog eens uitvoert, moet je nog een keer zeggen van woorden of je ze al kent. Dat is natuurlijk gek, want we hebben al eens aangeven van de woorden of we ze kenden. Daarom maak je nu deze aanpassingen aan je programma.

1. Lees bij het beginnen niet het bestand `words.csv`in, maar `words-selectie.csv`
2. Haal in de for-lus niet alleen de kolom woord op met \['`woord']`  maar ook de kolom `bekend`. Vraag alleen aan de gebruiker of het woord bekend is, als de kolom bekend nog leeg is. Dat doe je met een `if`, vergelijk daarvoor bekend met `''`.

**Opdracht 2) Een functie maken**

We hebben al heel wat code gemaakt, en er komt binnenkort nog meer code bij! Tijd om te code die we tot nu toe gemaakt hebben, in een functie te zetten om de code beter georganiseerd te houden. Maak een functie en noem deze `selecteren`.&#x20;

**Opdracht 3) Kiezen tussen selecteren en oefenen**

Nu je een functie hebt gemaakt, moeten we die nog _aanroepen_. Aanroepen betekent de code in de functie opstarten. Vraag aan de gebruiker wat hij of zij wil doen, en zet dit in een if:

1. De gebruiker zegt **selecteren** of **s** -> roep de functie `selecteren`aan. Let op! Vergeet de ronde haakjes achter de naam van de functie niet.
2. De gebruiker zegt **oefenen** of **o** -> print **We gaan oefenen**

Het stukje code dat zegt dat we gaan oefenen breiden we volgende les verder uit.

**Opdracht 4) Vang verkeerde invoer af (extra)**

Ook hier kunnen we weer netjes controleren of de gebruiker wel het juiste heeft ingevoerd. Geef een goede melding bij onlogische invoer, en bedenk deze melding zelf.

