while True:
    n:float = float(input("Inserisci un valore intero: "))
    if n % 1 == 0:
        break
if n > 0 and n <= 100:
    sum = 0
    for i in range(int(n)):
        if i % 2 == 0:
            sum += i
    print(sum)
elif n == 0 or n < 0:
    print("Errore")
else:
    sum = 0
    for i in range(int(n)):
        if i % 2 != 0:
            sum += i
    print(sum)
