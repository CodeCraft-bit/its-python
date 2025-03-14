while True:
    n:float = float(input("Inserisci un numero intero: "))
    if n % 1 == 0:
        break
if n > 0:
    if n % 2 == 0:
        cont:int = 4
        result:int = 0
        while cont <= n:
            result += cont
            cont += 4
        print(result)
    else:
        cont:int = 1
        result:int = 1
        while cont <= n:
            result *= cont
            cont += 2
        print(result)
