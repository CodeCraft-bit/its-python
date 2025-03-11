#esercizio 5_9

usernames_list = ["Admin", "Krys", "Roberto", "Laura", "Giulia"]

if 'Laura' in usernames_list:
    print("Hello Laura, thank you for logging again")

if 'Krys' in usernames_list:
    print("Hello Krys, thank you for logging again")

if 'Admin' in usernames_list:
    print("Hello Admin, would you like to see a status report?")

usernames_list=[]

if len(usernames_list)==0:
    print("We need to find some users!")

print(usernames_list)

for x in len(usernames_list):
    usernames_list.pop(x)

print(usernames_list)