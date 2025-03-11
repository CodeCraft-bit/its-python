#esercizio_8.12

def crea_panino(*args) -> None:
    print(f"Hai ordinato un panino con questi ingredienti: ")
    for ingredienti in args:
        print(f"{ingredienti}")
       

crea_panino("pomodoro", "insalata", "cipolla")
crea_panino("formaggio", "prosciutto crudo")
crea_panino("tonno", "maionese")

