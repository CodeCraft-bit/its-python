read_corso:str = input("Inserisci il nome del corso: ")
max_posti:int = 100

while True:
    opzione:str = input("Scegli tra le seguenti opzioni: iscrivi, annulla, visualizza, elimina, esci.")
    match opzione:
        case "iscrivi":
            if max_posti > 0:
                max_posti -= max_posti
            else:
                print("Non ci sono posti disponibili")
        case "annulla":
            if max < 100:
                max_posti += 1
            else:
                print("Tutti i posti sono già disponibili")
        case "visualizza":
            print(f"Il numero di posti è: {max_posti}")
            print(f"Il numero massimo di posti è: {100 - max_posti}")
        case "elimina":
            max_posti = 100
        case "esci":
            break
        case _:
            print(f"Opzione non valida, scegli tra quelle riportate in {opzione}")
