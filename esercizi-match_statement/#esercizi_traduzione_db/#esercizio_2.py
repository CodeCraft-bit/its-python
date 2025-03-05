#esercizio_2

max = float(input("Inserisci il primo numero: "))
i = 1

while i < 4:
    i+=1
    n = float(input("Inserisci un numero: "))
    if n > max:
        max = n
print(f"Il massimo valore è: {max}")


#repeat

max = float(input("Inserisci il primo numero: "))
i = 1

while True:
    i+=1
    n = float(input("Inserisci un numero: "))
    if n > max:
        max = n
    if i==4:
        break
    
print(f"Il massimo valore è: {max}")


#for

max = float(input("Inserisci il primo numero: "))

for i in range(3):
    n = float(input("Inserisci un numero: "))
    if n > max:
        max = n
print(f"Il massimo valore è: {max}")
