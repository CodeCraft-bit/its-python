#creo una variabile e do l'input per l'utente

neonati= int(input("Inserisci un numero"))


match neonati:
    #Se il numero inserito è 1, stampare "Congratulazioni!"
    case 1:
        print("Congratulazioni!")
    #Se il numero inserito è 2, stampare "Wow! Gemelli!"
    case 2:
        print("Wow!Gemelli!")
    #Se il numero inserito è 3, stampare "Wow! Tre!"
    case 3:
        print("Wow!Tre!")
    #Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
    case 4:
        print("Mamma mia Quattro!Wow!")
    #Se il numero inserito è 5, stampare "Incredibile! Cinque!"
    case 5:
        print("Incredibile!Cinque!")
    #Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito.
    case _:
        print(f"Non ci credo! {neonati} bambini!")
    
    