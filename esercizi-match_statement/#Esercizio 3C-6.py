#Esercizio 3C-6

mammiferi=["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili=["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli=["aquila", "pappagallo", "gufo", "falco"]
pesci=["squalo", "trota", "salmone", "carpa"]
animal_type:str = ""

habitatList = ["Terra," "Acqua", "Aria"]
habitat= input("Digita l'habitat in cui vive l'animale ").title()
animali = input("Digita il nome di un animale ").lower()


animal_info:dict ={
    "Terra":["cane", "gatto", "cavallo", "elefante", "leone", "serpente", "lucertola", "tartaruga", "coccodrillo"],
    "Acqua":["squalo", "trota","salmone", "carpa"],
    "Aria":["aquila", "pappagallo", "gufo", "falco"]
    } 



match animali:
    case animali if animali in mammiferi:
        animal_type= "mammiferi"
        
        match habitat:
            case habitat if habitat in animal_info and animali in animal_info[habitat]:
                print(f"L'animale {animali} può vivere nell'habitat {habitat}")

match animali:
    case animali if animali in rettili:
        animal_type= "rettili"
        
        match habitat:
            case habitat if habitat in animal_info and animali in animal_info[habitat]:
                print(f"L'animale {animali} può vivere nell'habitat {habitat}")

match animali:
    case animali if animali in uccelli:
        animal_type= "uccelli"
        
        match habitat:
            case habitat if habitat in animal_info and animali in animal_info[habitat]:
                print(f"L'animale {animali} può vivere nell'habitat {habitat}")

match animali:
    case animali if animali in pesci:
        animal_type= "pesci"
        
        match habitat:
            case habitat if habitat in animal_info and animali in animal_info[habitat]:
                print(f"L'animale {animali} può vivere nell'habitat {habitat}")
    




