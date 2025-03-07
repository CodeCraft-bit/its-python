#esercizio_10

r:int = int(input("Inserisci il reddito familiare: "))
m:int = int(input("Inserisci la media dei voti: "))

if r < 20000 and m > 27:
    print("Borsa di studio rifiutata (Motivo: reddito o media insufficiente)")
else:
    print("Borsa di studio approvata")


