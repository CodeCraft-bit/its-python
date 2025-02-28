#Esercizio 3C-8

frase = input("Scrivi qui la tua frase ")
lunghezza = len(frase)

match frase:
    case frase if frase[-1] == "?" and lunghezza %2==0:
        print("Si")
    case frase if frase[-1] == "?" and lunghezza ==1:
        print("No")
    case frase if frase[-1] =="!":
        print("Wow!")
    case _:
        print(f"Tu dici {frase}")
