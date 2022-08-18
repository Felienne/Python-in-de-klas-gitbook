# Les 1a

**De basisprincipes van C#**

In deze lessenserie gaan we C# gebruiken als voorbeeldtaal. C# is anders dan Python en JavaScript dat we tot nu toe gezien hebben. We leggen in het a deel van de les steeds wat basiskennis uit die jij in deel kan toepassen.

**Syntax**

De syntax van C# lijkt een beetje op javaScript, zo gebruiken we krulhaakjes om functies te maken en eindigen regels met een puntkomma. Maar... er zijn ook verschillen.

**Klassen en methodes**

In C# kan je niet "zomaar" code overal typen. Alle code moet in een methode staan (een soort functie) en die method hoort weer in een klasse. In dit programma zie je de klasse `Program` en de methode `Main`.&#x20;

<pre class="language-csharp"><code class="lang-csharp"><strong>class Program {
</strong><strong>  public static void Main() {
</strong>    Console.WriteLine("Hello World");
}</code></pre>

**Printen**

Printen doen we in C# met `Console.WriteLine("Hello World");`&#x20;

**Types**

Anders dan in Pythonen JavaScript moeten we in C# altijd vertellen welk type in een variabele gaat, hier zeggen we bijvoorbeeld dat text een string is.

<pre class="language-csharp"><code class="lang-csharp">class Program {
  public static void Main() {
<strong>    string text = "hallo!";
</strong>    Console.WriteLine (text);
}</code></pre>

**Tekst uit een bestand lezen**

In C# kunnen we vrij makkelijk een bestand uitlezen, dat gaat zo. We hoeven dus geen bestand aan te maken of with the gebruiken zoals in Python.

```csharp
string text = System.IO.File.ReadAllText("tweets.json");
```
