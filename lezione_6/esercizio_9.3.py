class User:
    def __init__(self,first_name:str, last_name:str, gender:str, city:str) ->str:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
    def describe_user(self):
        return(f"First name: {self.first_name}, last name: {self.last_name}, gender: {self.gender}, city: {self.city}")
    def greet_user(self):
        return(f"Hi {self.first_name}, welcome to my world!")
    

alessio = User("Alessio","G","M","Norvegia")
rosa = User("Rosa","Rossa","F","Milano")
nicola = User("Nicola","Giallo","N","Livorno")

print(alessio.describe_user())
print(alessio.greet_user())

print(rosa.describe_user())
print(rosa.greet_user())

print(nicola.describe_user())
print(nicola.greet_user())