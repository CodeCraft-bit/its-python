numbers = []

for i in range(1, 10):
    numbers.append(i)

for i in numbers:
    if i == 1:
        print("1st")
    elif i == 2:
        print("2nd")
    elif i == 3:
        print("3rd")
    else:
        print(i,"th",sep = "")