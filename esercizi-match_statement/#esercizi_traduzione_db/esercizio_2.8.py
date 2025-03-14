a:float = float(input("Inserisci un valore intero positivo A: "))
b:float = float (input("Inserisci un valore intero positivo B: "))
if a < b:
    if a > 0 and b > 0:
        if a % 1 == 0 and b % 1 == 0:
            sum:int = 0
            i:int = a
            while i <= b:
                sum += i
                i += 1
            print(f"La somma è {int(sum)}")
        else:
            print(f"{a}, {b} devono essere interi")
    else:
        print(f"{a}, {b} devono essere positivi")
else:
    print(f"{a} deve essere minore di {b}")

    











   
