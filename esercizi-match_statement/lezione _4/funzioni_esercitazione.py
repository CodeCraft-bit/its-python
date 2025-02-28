'''#1
sum:int = 0

for i in range (1,11):
    sum +=i
print(f"La somma da 1 a 10 è, {sum}")

#2
sum:int = 0

for i in range (20,38):
    sum +=i
print(f"La somma da 20 a 37 è, {sum}")

#3
sum:int=0

for i in range (35,50):
    sum +=i
print(f"La somma da 35 a 50 è, {sum}")'''

#4
def subtract(a:int, b:int):

    result:int = a - b
    return result
a = int(input("Inserisci un numero intero "))
b = int(input("Inserisci un numero intero "))
print(f"La sottrazione tra {a}, {b} è {subtract(a, b)}")
    

    

