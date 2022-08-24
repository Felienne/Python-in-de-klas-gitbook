# Les 1b

**1) Maak een  nieuw C# bestand op repl.it**&#x20;

Klink in replit op Create en maak een nieuw C# bestand aan. Let op dat je de gewone C# kiest en niet mono.&#x20;

![](https://www.dropbox.com/s/uc0fx1cfojy6y1k/Screen%20Shot%202022-08-18%20at%203.26.34%20PM.png?raw=1)

**2) Lees een bestand in!**

Download dit bestand met [een tweet in jsonformaat](https://www.dropbox.com/s/8jykdfbamhkc59l/tweet.json?dl=0) en voeg het toe aan je replit. Gebruik de code uit deel a om de tweets in het bestand in te lezen. Print de inhoud van het bestand uit zodat je kunt zien of het goed gegaan is.

**3) Vertaal het bestand in json**

We hebben het bestand nu als tekst ingelezen maar het is een json file en we kunnen het dus in een keer inlezen in een dictionary (zoals we die ook kennen uit Python en JavaScript).

Zet bovenaan je bestand deze code om een module te importeren:

```csharp
using System.Text.Json;
```

Nu kunnen we de json zo inlezen. Zoek in deel a of op internet op hoe je een bestand inleest als je het niet meer weet.

```csharp
// lees hier het bestand in en zorg dat in inhoud ervan in de variabele text komst

var jsonObject = JsonDocument.Parse(text);
Console.WriteLine (jsonObject);
```

Anders dan in Python kunnen we het object niet goed zien in C#. We kunnen wel een veld opvragen, probeer dat maar eens:

```csharp
var tweetText = jsonObject.RootElement.GetProperty("full_text");
Console.WriteLine (tweetText);
```

**4) Wat zit er allemaal op een tweet?**

Nu we een tweet kunnen inlezen wordt het tijd om eens te bekijken wat er allemaal op zit! Lees de json eens door en zoek uit of je deze dingen kan printen:

* Hoe vaak een tweet is geretweet
* Of een andere user genoemd is in de tweet (een _mention_ heet dat)
* Of er een foto bij zat
* Vanaf welke plaats of locatie de tweet is verstuurd

Denk ook al eens na over wat je met deze data zou kunnen doen!

**5) Nu met meer tweets**

De code dit je tot nu toe hebt geschreven werkt maar voor een tweet. Nu ga jij het mogelijk maken om het voor meerdere tweets te doen. Volg daarvoor deze stappen:

* Download [dit bestand](https://www.dropbox.com/s/l7d8d1301ba7b2z/tweets.json?dl=0) en voeg het toe aan je project
* Lees de inhoud van het bestand in, regel per regel
  * Hiervoor heb je een for lus nodig. Je kan twee dingen doen: zelf opzoeken op internet hoe dat moet, of nu overschakelen op de online videos hieronder, dan komt het vanzelf langs!
* Parse iedere regel los met de json parser en verwerk de inhoud



**Hierna: Meer leren over C#**

Nu je ongeveer weet wat we gaan doen met C# is het tijd om ons wat meer in de taal te verdiepen. Volg [deze cursus van Microsoft](https://docs.microsoft.com/nl-nl/learn/paths/csharp-first-steps/?WT.mc\_id=dotnet-35129-website\&ns-enrollment-type=Collection\&ns-enrollment-id=yz26f8y64n7k07) op je eigen tempo.
