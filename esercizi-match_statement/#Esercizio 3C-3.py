#Esercizio 3C-3

oggetti = []

for i in range(3):
    oggetti.append(input("Inserisci un oggetto"))


match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print ("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")