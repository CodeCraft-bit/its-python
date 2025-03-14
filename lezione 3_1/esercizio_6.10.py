favorite_numbers = {
    "Silvano":"8",
    "Rebecca":"21",
    "Rachele":"7",
    "Silvia":"5",
    "Luca":"3"
      }
'''
for key in favorite_numbers:
    print(key,favorite_numbers[key])'
    '''

favorite_numbers["Silvano"] = [8, 6]
favorite_numbers["Rebecca"] = [21,4]
favorite_numbers["Rachele"] = [7,10]
favorite_numbers["Silvia"] = [5,1]
favorite_numbers["Luca"] = [3,11]

for key in favorite_numbers:
    print(key,favorite_numbers[key])