class Person:
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display_info(self):
        return f"My name is {self.name} and i'm {self.age} years old and My gender is {self.gender}"
    
        
person1 = Person("Etienne TUYIHAMYE", 22, "Male")
person2 = Person("Avink judi", 19, "Female")
 
print(person1.display_info())
print(person2.display_info())