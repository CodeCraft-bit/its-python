while True:
    x:float = float(input("Inserisci un numero intero positivo: "))    
    y:float = float(input("Inserisci un numero intero positivo: "))
    z:float = float(input("Inserisci un numero intero positivo: "))
    if x % 1 == 0 and x > 0:
        if y % 1 == 0 and y > 0:
            if z % 1 == 0 and z > 0:
                if (x+y+z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
                   print("Regole rispettate")
                else:
                   print("Regole non rispettate")
            else:
               print(f"{z} deve essere intero e positivo")
        else:
            print(f"{y} deve essere intero e positivo")
    else:
        print(f"{x} deve essere intero e positivo")
               
               