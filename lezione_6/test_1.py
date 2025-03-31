'''
def rounded_average(numbers: list[int]) -> int:
    average = sum(numbers) / len(numbers)
    return round(average)'
    '''

'''def convert_temperature(temperature:float, to_fahrenheit:float = True) -> float:
    if to_fahrenheit == True:
        temperature = (temperature*9/5)+32
    else:
        temperature = (temperature - 32)*5/9

    return temperature
    '''
'''def check_parentheses(expression: str) -> bool:
    for i in range (len(expression)):
        if expression[i] == "(" and expression.find(")", i) == -1:
            return False
    return True
'''

'''def count_isolated(lst:list[int]) -> int:
    c = 0
    for i in range (len(lst)):
        if i == 0:
            if lst[i] != lst[i + 1]:
                c += 1
        elif i == len(lst) - 1:
            if lst[i] != lst[i - 1]:
                c += 1

        else:
            if lst[i] != lst[i + 1] and lst[i] != lst[i - 1]:
                c += 1
    return c'''


'''def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    elements_to_remove = original_set - (set(elements_to_remove))'''

'''def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    c = dict1.copy()
    for key, value in dict2.items:
        if key in c:
            c[key]+=value
        else:
            c[key]=value
    return c
    '''





