#Esercizio 3C-4

animali = str(input("Digita il nome di un animale"))

match animali:
    case  "cane"|"gatto"|"cavallo"|"elefante"|"leone":
        print("Mammiferi")
    case "serpente"|"lucertola"|"tartaruga"|"coccodrillo":
        print ("Rettilli")
    case "aquila"|"pappagallo"|"gufo"|"falco":
        print("Uccelli")
    case "squalo"|"trota"|"salmone"|"carpa":
        print("Pesci")
    case _:
        print("Non so dire in quale categoria classificare l'animale")

    
'''mammiferi=["cane, gatto, cavallo, elefante, leone"]
rettili=["serpente, lucertola, tartaruga, coccodrillo"]
uccelli=["aquila, pappagallo, gufo, falco"]
pesci=["squalo, trota, salmone, carpa"]

animali = str(input("Digita il nome di un animale "))

match animali:
    case animali if animali in mammiferi:
        print("Mammiferi")
    case animali if animali in rettili:
        print ("Rettilli")
    case animali if animali in uccelli:
        print("Uccelli")
    case animali if animali in pesci:
        print("Pesci")
    case _:
        print("Non so dire in quale categoria classificare l'animale")'''