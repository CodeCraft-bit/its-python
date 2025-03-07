#esercizio_8

soglia:int = int(input())
cont:int = 0
while cont < 7:
    n: int = int(input())
    if n > soglia:
        print(f"{n} è maggiore di {soglia}")
    cont += 1