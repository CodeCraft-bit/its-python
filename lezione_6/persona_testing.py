'''

#dal file persona.py importa la classe Persona 
from persona import Persona

rdr:Persona = Persona("Rebecca","De Rosa",25)

print(rdr)

print(rdr.name, rdr.lastname, rdr.age)

#sfrutta la funzione displayData della classe Persona per visualizzare in output i dati relativi alla persona rdr
rdr.displayData()

'''

#dal file persona2.py importa la classe Persona
from persona2 import Persona

rdr:Persona = Persona()

rdr.displayData()

print("--------------")

#imposto il nome della persona rdr
rdr.setName("Rebecca")
rdr.displayData()

#imposto il cognome della persona rdr
rdr.setLastname("De Rosa")

#imposto l'età della persona rdr
rdr.setAge(25)

print("--------------")

rdr.displayData()

print("--------------")

print(rdr.getName(), rdr.getLastname(), rdr.getAge())