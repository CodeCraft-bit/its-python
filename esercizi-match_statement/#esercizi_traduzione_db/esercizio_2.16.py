dispari:int = 0
pari:int = 0
negativi:int = 0
positivi:int = 0

for i in range(10):
    while True:
        n:float = float(input("Inserisci un numero intero e diverso da zero: "))
        if n % 1 == 0 and n!=0:
            break
    if n > 0:
        positivi += 1
        if n % 2 == 0 and n > 20:
            pari +=1
    else:
        negativi += 1
        if n % 2 != 0 or n <-10:
            dispari += 1
print(positivi, negativi, pari, dispari)

