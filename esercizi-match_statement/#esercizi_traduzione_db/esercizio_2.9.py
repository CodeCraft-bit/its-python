while True:
    n:int = int(input("Inserisci un valore intero positivo: "))
    if n > 0:
        break
    else:
        print(f"{n} deve essere positivo")
        exit()

cont = 0
for i in range(10):
    x:int = int(input("Inserisci un numero intero: "))
    if x % n == 0:
        cont += 1
print(f"I numeri divisibili per {n} sono {cont}")