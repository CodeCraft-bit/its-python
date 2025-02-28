#Esercizio 3C-9

def coordinate (*args):

    match args:
        case (0,0):
            print("Il punto si trova nell'origine")
        case (_,0):
            print("Il punto si trova sull'asse X")
        case (0,_):
            print("Il punto si trova nell'asse Y")
        case (x,y) if x > 0 and y > 0:
            print("Il punto si trova nel primo quadrante")
        case (x,y) if x < 0 and y > 0:
            print("Il punto si trova nel secondo quadrante")
        case (x,y) if x < 0 and y < 0:
            print("Il punto si trova nel terzo quadrante")
        case (x,y) if x > 0 and y < 0:
            print("Il punto si trova nel quarto quadrante")

x = float(input("Inserisci la coordinata x: "))
y = float(input("Inserisci la coordinata y: "))
coordinate (x,y)