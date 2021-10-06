# Les 4a

**Opdracht 1**

Bekijk de code uit de slides, alleen voor de letter A.

```python
A = pygame.image.load("A.png")

while True:

  screen.blit(A, (0, 0))

  pygame.event.get()
  locatie_muis = pygame.mouse.get_pos()
  knoppen = pygame.mouse.get_pressed()

  if knoppen[0] == 1:
    if A.get_rect().collidepoint(locatie_muis):
      print('A')
      
  time.sleep(0.5) #even wachten op de volgende klik!
```

Weet jij nog wat er niet goed is aan deze code? Waarom werkt het niet altijd.

**Opdracht 2**

Welke regels moeten er aangepast worden zodat de code wel goed werkt? Schrijf de regelnummers op.

