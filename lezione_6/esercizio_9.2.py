class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str) ->str:
        self.restaurante_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        return(f"Restaurant name is {self.restaurante_name} and the cuisine type is {self.cuisine_type}")
    def open_restaurant(self):
        return("The restaurant is open")
    
aperifish = Restaurant("Aperifish", "Japanese")
print(aperifish.describe_restaurant())
print(aperifish.open_restaurant())

casa_dolce = Restaurant("Casa_dolce", "Italian")
susi = Restaurant("Susi", "Thai")
ambo = Restaurant("Ambo", "African")

print(casa_dolce.describe_restaurant())
print(casa_dolce.open_restaurant())

print(susi.describe_restaurant())
print(susi.open_restaurant())

print(ambo.describe_restaurant())
print(ambo.open_restaurant())