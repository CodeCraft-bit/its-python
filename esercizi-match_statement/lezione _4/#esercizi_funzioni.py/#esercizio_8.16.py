import esercizio14 
esercizio14.make_car ('subaru', 'outback', color='blue', tow_package=True) 
from esercizio14 import make_car 
print(make_car('subaru', 'outback', color='blue', tow_package=True))
from esercizio14 import make_car as fn 
print(fn('subaru', 'outback', color='blue', tow_package=True))
import esercizio14 as mn 
print(mn.make_car('subaru', 'outback', color='blue', tow_package=True)) 
from esercizio14 import* 
print(esercizio14.make_car('subaru', 'outback', color='blue', tow_package=True))