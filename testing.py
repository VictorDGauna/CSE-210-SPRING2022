

#--------------------------PRACTICA DE CLASES Y HERENCIAS


class Person:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
class Student(Person):
    
    def __init__(self, name):
        super().__init__(name)
        
student = Student("chau")
name = student.get_name()      

print(Student("hola").get_name())
print (name)        
print ( Person("salud").get_name())