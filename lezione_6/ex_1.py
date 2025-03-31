'''Exercise 1
1. Copy the code and print the age of
bob (using the dot notation)
2. Create an if-statement that prints
the name of the oldest of the two
Persons
3. Create three other Persons. Make
a list called people with all 5
Persons.
4. Make a loop that finds and prints
the youngest person’s name'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)
if bob.age > alice.age:
    print("Bob è più grande di Alice")
else:
    print("Alice è più grande di Bob")

riccardo:Person = Person("Riccardo L.", 15)
federico:Person = Person("Federico R.", 11)
domenico:Person = Person("Domenico C.", 5)

people:list[Person] = [riccardo,federico,domenico,alice,bob]

min:float = float("inf") 
min_name:str = ""

for person in people:
    if person.age < min:
        min = person.age
        min_name = person.name
print(f"{min_name} è il più piccolo della lista")



