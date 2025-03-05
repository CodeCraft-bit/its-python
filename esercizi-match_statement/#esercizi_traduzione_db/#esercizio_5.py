#esercizio_5
'''
n = int(input("Inserisci un numero: "))

if n < 2:
    print(f"Il numero {n} non è primo")
else:
    div = 2

    while True:
        if div < n:
            if n % div == 0:
                print(f"Il numero {n} non è primo")
                break
            else:
                div+=1
        else:
            print(f"Il numero {n} è primo")
            break
    '''

#modo 2


n = int(input("Inserisci un numero: "))

if n < 2:
    print(f"Il numero {n} non è primo")
else:
    div = 2

    while True:
        if div <= n**0.5:
            if n % div == 0:
                print(f"Il numero {n} non è primo")
                break
            else:
                div+=1
        else:
            print(f"Il numero {n} è primo")
            break