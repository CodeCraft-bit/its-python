#Esercizio 3C-2

voto_laurea_italiano = int(input("Inserisci il voto di laurea: "))

match voto_laurea_italiano:
    case voto_laurea_italiano if 106 <= voto_laurea_italiano <= 110: 
        print("GPA 4.0")
    case voto_laurea_italiano if 101 <= voto_laurea_italiano <= 105:
        print("GPA 3.7")
    case voto_laurea_italiano if 96 <= voto_laurea_italiano <= 100:
        print("GPA")
    case voto_laurea_italiano if 91 <= voto_laurea_italiano <= 95:
        print("GPA 3.0")
    case voto_laurea_italiano if 86 <= voto_laurea_italiano <= 90:
        print("GPA 2.7") 
    case voto_laurea_italiano if 81 <= voto_laurea_italiano <= 85:
        print("GPA 2.3")
    case voto_laurea_italiano if 76 <= voto_laurea_italiano <= 80:
        print("GPA 2.0")
    case voto_laurea_italiano if 70 <= voto_laurea_italiano <= 75:
        print("GPA 1.7")
    case voto_laurea_italiano if 66 <= voto_laurea_italiano <= 69:
        print("GPA 1.0")
    case _:
        print("Voto non valido")