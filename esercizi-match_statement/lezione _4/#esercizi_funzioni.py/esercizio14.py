def make_car (model_name, manufacturer, **kwargs)->dict:
    s = {"model_name":model_name, "manufacturer":manufacturer}
    for key, value in kwargs.items():
        s[key]=value
    return s


car = make_car('subaru', 'outback', color='blue', tow_package=True) 
print(car)






