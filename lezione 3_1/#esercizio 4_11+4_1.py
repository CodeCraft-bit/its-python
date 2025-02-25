#esercizio 4_11+4_1
pizza_name = ["Margherita", "Patate", "Diavola"] 

for x in pizza_name:
    print (f"{x}") 

for x in pizza_name:
    print (f"I like {x} pizza")

print (f"I really like {x} pizza, it's my favourite, it's the best ")
print(pizza_name[:])
friend_pizzas = pizza_name[:]
print(friend_pizzas)

pizza_name.insert (2,"Capricciosa")
print (pizza_name)

friend_pizzas.insert (3,"Salsiccia")
print (friend_pizzas)

print ("My favourite pizzas are")

for z in pizza_name:
    print(z)

print("My friend's favourite pizzas are")

for x in friend_pizzas:
    print(x)