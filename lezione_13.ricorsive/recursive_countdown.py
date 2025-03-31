def countdown(n:int) -> None:
    if n < 0:         #caso base o di arresto
        print("Error! Inserted number is negative!")

#countdown(-5)
    elif n == 0:
        print(0)     #n = 0 è il nostro caso base o di arresto necessario per interrompere la ricorsione

    else:
        print(n)
        countdown(n-1) #questo gestisce la ricorsione

countdown(5)
