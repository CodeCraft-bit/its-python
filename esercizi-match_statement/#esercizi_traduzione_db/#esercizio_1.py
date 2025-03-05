#esercizio_1

a = float(input("Inserisci un numero"))
b = float(input("Inserisci un numero"))

if a>b:
    c = (a**2 - b**2) ** (1/2)
    print(f"Il valore di c è: {c}")
else:
    print("Errore")