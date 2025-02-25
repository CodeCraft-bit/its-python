#esercizio_3C-00B

nome= str(input("Inserisci il tuo nome "))
genere= str(input("Inserisci il tuo genere, M per maschio, F per femmina"))

match genere:
    #Se il valore di gender è "m", stampare il nome e il genere come Maschio.
    case "m":
        print(f"{nome}, \n maschio ")
    #Se il valore di gender è "f", stampare il nome e il genere come Femmina.
    case "f":
        print(f"{nome}, \n femmina")
    #Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore, indicando che non è possibile generare un documento di identità.
    case _:
        print(f"Mi dispiace, non è possibile generare un documento d'identità")