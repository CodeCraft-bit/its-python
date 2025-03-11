#esercizio 5_10
current_users=["Claudio", "Roberto", "Renata", "Giorgia", "Luana"]
new_users=["Roberto", "RENATA", "Emanuele", "Giulia", "Flavio"]
current_users2=[]


for i in range(len(current_users)):
    current_users2.append(current_users[i].upper())


for i in range(len(new_users)):
    if new_users[i] in current_users:
        print("The name",new_users[i],"is not available")
    elif new_users[i] in current_users2:
        print("The name",new_users[i],"is not available")
    else:
        print("The name",new_users[i], "is available")    

