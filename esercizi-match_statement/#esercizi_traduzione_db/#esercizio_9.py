#esercizio_9

nome:str = input("Inserisci il nome del venditore: ").title()
vendite:int = int(input(f"Inserisci il numero di vendite del venditore {nome}"))
max_nome:str = nome
max:int = vendite
min:int = vendite
min_nome:str = nome

for i in range(19):
    new_nome:str = input("Inserisci il nome del venditore: ").title()
    new_vendite:int = int(input(f"Inserisci il numero di vendite del venditore {new_nome}"))
    if new_vendite > max:
        max_nome = new_nome
        max = new_vendite
    else:
        if new_vendite < min:
            min_nome = new_nome
            min = new_vendite

print(f"Il venditore {max_nome} ha il numero piu alto di vendite {max}")
print(f"Il venditore {min_nome} ha il numero piu basso di vendite {min}")