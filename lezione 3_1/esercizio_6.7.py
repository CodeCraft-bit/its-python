''''
persone = {
    "first_name": "Krys", 
    "last_name":"Braides",
    "age": "30",
    "city": "Milano"
    }
print(persone["first_name"])
print(persone["last_name"])
print(persone["age"])
print(persone["city"])'
'''
persone_1 = {
    "first_name": "Silvano", 
    "last_name":"Desimo",
    "age": "52",
    "city": "Roma"
    }
persone_2 = {
    "first_name": "Krys", 
    "last_name":"Braides",
    "age": "30",
    "city": "Milano"
    }
persone_3 = {
    "first_name": "Rachele",
    "last_name":"Fiore",
    "age": "23",
    "city": "Napoli"
    }
people = [persone_1, persone_2, persone_3]

for i in people:
    print(i)