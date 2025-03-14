x:int = ("Inserisci un valore x positivo: ")
sum:int = 0

if x > 0:
    for i in range(10):
        n:int = ("Inserisci 10 numeri sia positivi che negativi: ")
        if x%2==0:
            n > x/2
            sum += n
        elif n < x:
            sum +=n

    print(sum)
else:
    print(f"Errore {x} deve essere positivo")

