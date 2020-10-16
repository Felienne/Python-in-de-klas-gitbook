import random

quizvragen = ['vraag 1', 'vraag 2'] #vul hier jouw vragen in!
opties = ['A)... B)...', 'A)... B)...']  #vul hier jouw antwoorden in!

# deze code hoef je niet aan te passen, die is alleen om je lijsten te testen
# als het goed is kun je deze code wel prima lezen natuurlijk...!
vraagnummer = random.randint(0, len(quizvragen)-1)

print(quizvragen[vraagnummer])
print("Kies uit")
print(opties[vraagnummer])

