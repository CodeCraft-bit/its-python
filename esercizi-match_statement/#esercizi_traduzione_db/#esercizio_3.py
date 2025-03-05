#esercizio_3

sum = 0
cont = 0


while True:
    n = float(input("Inserisci un numero: "))
    if n > 0:
        sum = sum+n
    cont = cont+1
    if cont==5:
        break
print(f"La somma dei numeri positivi è: {sum}")