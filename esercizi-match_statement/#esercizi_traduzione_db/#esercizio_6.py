#esercizio_6

while True:
    n:int = int(input("Il numero inserito deve essere positivo: "))
    if n > 0:
        break

fattoriale:int = 1
i: int= 1
for i in range (1, n+1):
    fattoriale *= i

print(f" Il fattoriale di {n} è {fattoriale}")
















