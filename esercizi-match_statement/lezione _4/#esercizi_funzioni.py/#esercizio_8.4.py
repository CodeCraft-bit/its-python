#esercizio_8.4

def make_shirt(size:str="m",message:str="I love python")-> None:
    print(f"The size is {size}, the message printed is {message}")
make_shirt()


def make_shirt(size:str="l",message:str="I love music")-> None:
    print(f"The size is {size}, the message printed is {message}")
make_shirt()


def make_shirt(size:str="xs",message:str="I like chocolate")-> None:
    print(f"The size is {size}, the message printed is {message}")
make_shirt()


def make_shirt(size:str="xl",message:str="I'm happy")-> None:
    print(f"The size is {size}, the message printed is {message}")
make_shirt()

'''
print(type(make_shirt()))
'''