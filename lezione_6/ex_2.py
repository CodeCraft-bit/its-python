'''
Exercise 2 (Folder 9 ex_2.py)
1. Write a class called Student with the attributes name (str) and
studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too.'
'''

class Student:
    def __init__ (self, name:str, study_Program:str, age:int, gender:str):
        self.name = name
        self.study_Program = study_Program
        self.age = age
        self.gender = gender
    def printInfo(self):
        print(f"{self.name}, {self.study_Program}, {self.age}, {self.gender}")


rebecca = Student("Rebecca Dr.", "cybersecurity", 34, "F")
riccardo = Student("Riccardo L.", "hacking da bash", 52, "M")
federico = Student("Federico R.", "pittura rupestre", 18, "Bombombini Gusini")

riccardo.printInfo()
rebecca.printInfo()
federico.printInfo()


    