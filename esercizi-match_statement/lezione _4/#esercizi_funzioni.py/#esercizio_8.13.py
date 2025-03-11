def build_profile(first_name,last_name,**kwargs)-> str:
    s = {}
    string:str = f"{first_name} {last_name}, "
    for key, value in kwargs.items():
        s[key]=value
    for key,value in s.items():
        string+= f"{key} {value}, "
    return(string[:-2])

print(build_profile("Rebecca", "De Rosa", anni=25, hair="brown", color="red"))


