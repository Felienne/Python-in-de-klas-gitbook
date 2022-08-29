# Les 2b

**1) Nu met meer tweets**

De code dit je tot nu toe hebt geschreven werkt maar voor één tweet. Nu ga jij het mogelijk maken om het voor meerdere tweets te doen.&#x20;

Volg daarvoor deze stappen:

* Zet code die je al hebt om in een functie die de tekst van één json object inleest en de tekst van de tweet uitprint. Een functie ziet er zo uit in C#:

```csharp
  public static void ConvertOneTweetToJSON(string text) {
   
    // zet hier de code die één string (opgeslagen in de variabele text) omzet 
    // in json formaat 
    // print voor het gemak ook de tekst van de tweet naar de console

  }
```

* Download nu [dit bestand](https://www.dropbox.com/s/5b9fj0v5by0reu9/tweets.json?dl=0) en voeg het toe aan je project
*   Lees de inhoud van het bestand in, regel per regel

    \
    Hiervoor heb je een `foreach` lus nodig. \
    \
    Je kan twee dingen doen: \
    &#x20;    1\. zelf opzoeken op internet hoe dat moet, of\
    &#x20;    2\. nu overschakelen op de online videos hieronder, dan komt het vanzelf langs!
* Is het gelukt om een loop te gebruiken in C#?\
  \
  Parse dan iedere regel los met de json parser en verwerk de inhoud

{% hint style="info" %}
Krijg je deze foutmelding:\
\
Unhandled exception. System.Text.Json.JsonReaderException: '{' is invalid after a single JSON value. Expected end of data. LineNumber: 1 | BytePositionInLine: 0.

\
Dan probeer je meerdere tweets tegelijk in te lezen in json, dat werkt niet! Doe eht regel per regel.
{% endhint %}

**2) Plan je project**

In periode 1 en 2 gaan we aan de slag met een Twitter dataset. Begin al eens met nadenken over wat je met deze data zou kunnen doen! Denk bijvoorbeeld over wat voor soort tweets jij in wilt lezen, iets over films, voetbal of iets heel anders?&#x20;

En wat ga jij met de data doen? Plotten op een wereldkaart? Tekstanalyse op wat mensen zeggen ?

**Hierna: Meer leren over C#**

Nu je ongeveer weet wat we gaan doen met C# is het tijd om ons wat meer in de taal te verdiepen. Volg [deze cursus van Microsoft](https://docs.microsoft.com/nl-nl/learn/paths/csharp-first-steps/?WT.mc\_id=dotnet-35129-website\&ns-enrollment-type=Collection\&ns-enrollment-id=yz26f8y64n7k07) op je eigen tempo.



