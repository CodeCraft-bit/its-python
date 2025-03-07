#esercizio_7

pari:int = 0
dispari:int = 0

for i in range (10):
    n:int = int(input("Inserisci 1 numero: "))
    if n %2==0:
        pari += 1
    else:
        dispari += 1
        

print(f"Dei 10 numeri inseriti,{pari} e {dispari} sono dispari")

