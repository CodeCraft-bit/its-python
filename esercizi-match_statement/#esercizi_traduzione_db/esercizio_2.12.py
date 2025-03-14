n:int = int(input("Inserisci un numero: "))
for i in range (n):
    x:int = int(input("Inserisci un valore x"))
    y:int = int(input("Inserisci un valore y"))
    if x > 0 and y > 0:
        result = x*y
        print(result)
    elif x < 0 and y < 0:
        print("Errore")
    else:
        result = x - y
        print(result)