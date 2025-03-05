#esercizio_8.5

def describe_city(city:str= "Roma", country:str= "Italia") -> None:
    print(f"The city {city} is in {country}")

describe_city("Milano", "Italia")
describe_city("Firenze", "Italia")
describe_city("Torino", "Italia")