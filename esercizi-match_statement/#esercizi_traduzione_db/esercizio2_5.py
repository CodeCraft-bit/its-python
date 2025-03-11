n:str = ("Inserisci un numero intero positivo: ")

if n%1 == 0 and n > 0:
    sum:int = 0
    i = 1
else:
    print(f"Errore,{n} deve essere positivo")

while i <= n:
    sum = sum + i*i
    i += 1
print(f"La somma è {sum}")

