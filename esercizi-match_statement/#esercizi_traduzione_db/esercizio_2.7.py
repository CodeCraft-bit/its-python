cont:int = 0
sum = 0
while True:
    scelta:str = input("Vuoi inserire un voto: Si/ No")
    if scelta == "Si":
        while True:
            voto:int = int(input("Inserisci il voto: "))
            if voto > 0:
                cont +=1
                sum += voto
                break
            else:
                print("Errore")
    elif scelta == "No":
        if cont > 0:
            media = sum/cont
            print(f"La media è {media}")
        else:
            print("Nessun voto inserito")



