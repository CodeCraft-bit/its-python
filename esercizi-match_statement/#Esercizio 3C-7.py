#Esercizio 3C-7

teste = 0

croci = 0

for i in range (8):
    x = input("Inserisci t per testa e c per croce").lower()
    match x:
        case "t":
            teste +=1
        case "c":
            croci +=1
        case _:
            print("Errore!")

percentuali_teste: float= teste/8 * 100
percentuali_croci: float= croci/8 * 100

print(f"Totale teste {teste}\n percentuale teste {percentuali_teste}")
print(f"Totale croci {croci}\n percentuali croci {percentuali_croci}")
        