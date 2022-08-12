# Les 7b

**Opdracht 1) Schakel je code uit en voeg de UI toe**

We gaan de User Interface (of UI, zeg: Joe-Ai) stap voor stap toevoegen. Open je code van vorige week en zet even alles uit. Dat doet je met ctrl-a (alles selecteren) en dan ctrl-? (alles op commentaar zetten)&#x20;



Zet nu deze code bovenaan. Deze regels maken een UI aan met een knop en een invoerveld.

{% code lineNumbers="true" %}
```python
# import time 

from tkinter import *

root = Tk()

root.title("Mijn rekenmachine")
root.geometry("500x200")

def rekenen():
  invoer = invoerveld.get()
  # hier moet natuurlijk jouw code gekoppeld worden
  
  uitvoerveld["text"] = "0"

invoerveld = Entry(root) 
invoerveld.place(x=0, y=10)

knop = Button(root)
knop["text"] = "Rekenen"
knop.place(x=0, y=60)
knop["command"] = Rekenen

uitvoerveld = Label(root)
uitvoerveld["text"] = "Berekening komt hier"
uitvoerveld.place(x=0, y=120)
```
{% endcode %}

Voer de code uit en zie dat je drie elementen in beeld hebt: een invoerveld, een knop en een uitvoerveld.&#x20;

Vind je de namen of plaatsen van de velden niet mooi? Verander dan de regels 17, 20, 21, 25 en 26.





