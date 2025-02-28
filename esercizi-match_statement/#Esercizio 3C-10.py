#Esercizio 3C-10

def data (*args):

    match args:
        case (1,1):
            print(" Il 1/1 è Capodanno!")
        case (14,2):
            print("Il 14/2 è San Valentino!")
        case (2,6):
            print("Il 2/6 è Festa della Repubblica Italiana!")
        case (15,8):
            print("Il 15/8 è Ferragosto!")
        case (31/10):
            print("Il 31/10 è Halloween!")
        case (25/12):
            print("Il 25/12 è Natale!")
        case _:
            print("Nessuna festività importante in questa data")

giorno= int(input("Inserisci il giorno "))
mese= int(input("Inserisci il mese "))
data(giorno,mese)