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