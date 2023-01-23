# Parser Earleya
## Przykładowe użycie
Do uruchomienia wystarczy użyć
```
   python main.py 
```

A następnie podać wymagane dane:
```
Podaj alfabet, rodzielony przecinkami (np. a, b, c): 1, 0
Podaj symbole nieterminalne, rodzielone przecinkami (np. A, B, C): S, A
Podaj listę produkcji w postacji: A -> b. Produkcje oddziel przecinkami: S -> 0, S -> 1, S -> A, A -> 1, A -> 0, A -> 0A0, A -> 1A1
Podaj symbol startowy: S
Podaj słowo: 01110
```

Jako wynik otrzymamy kroki wykonywane przez algorytm + informację czy słowo należy do podanej gramatyki, czy nie

```
Przewidywanie: S -> *0 [0, 0]
Przewidywanie: S -> *1 [0, 0]
Przewidywanie: S -> *A [0, 0]
Wczytywanie, S -> 0* [0, 1]
...
i = 5
Uzupełnianie S -> A* [0, 5]
Uzupełnianie A -> 1A*1 [3, 5]
Uzupełnianie S' -> S* [0, 5]
Należy do podanej gramatyki
```
