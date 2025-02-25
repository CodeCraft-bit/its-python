#esercizio 4_10+4_1
pizza_name = ["Margherita", "Patate", "Diavola"] 

for x in pizza_name:
    print (f"{x}") 

for x in pizza_name:
    print (f"I like {x} pizza")

m = len(pizza_name)//2

print (f"I really like {x} pizza, it's my favourite, it's the best ")
print (f"{pizza_name[:3]},questi sono i primi tre elementi della lista")
print (f"{pizza_name[m-1:m+2]}, questi sono gli elementi di mezzo")
print (f"{pizza_name[-3:]}, questi sono gli ultimi tre elementi")