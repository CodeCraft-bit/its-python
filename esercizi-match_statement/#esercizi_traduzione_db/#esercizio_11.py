#esercizio_11

liberi:int = 20

while True:
    opzione:str = input("Dammi un comando tra prenota, libera, visualizza, esci").lower()
    match opzione:
        case "prenota":
            if liberi > 0:
                liberi -= 1
            else:
                print("Non ci sono posti liberi")
        case "libera":
            if liberi < 20:
                liberi += 1
            else:
                print("Tutti i posti sono già disponibili")
        case "visualizza":
            print(f"I posti liberi sono: {liberi}")
            print(f"I posti occupati sono {20-liberi} ")
        case "esci":
            break
        case _:
            print("Opzione non valida, riprova.")




