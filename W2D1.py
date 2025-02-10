class cricket:
    name=""
    players=0
cricket1=cricket()
cricket1.name="Indian"
cricket1.players=13
print(f"{cricket1.name} team has {cricket1.players} players. ")


class student:
    name=""
    marks=0
student1=student()
student1.name=str(input("Enter the Student name: "))
student1.marks=int(input("Enter you marks: "))
print(f"{student1.name} has obtained {student1.marks} from 500")


class student:
    name=""
    marks=0
student1=student()
student1.name=str(input("Enter the Student name: "))
student1.marks=int(input("Enter you marks: "))
if student1.marks > 500 or student1.marks < 0:
    print("Enter valid marks (0-500).")
else:
    print(f"{student1.name} has obtained {student1.marks} out of 500")


class Cricket:
    teamName=None
    def setTeamName(self,name):
        self.teamName=name
    def getTeamName(self):
       return self.teamName
c=Cricket()
c.setTeamName("India")
print(c.getTeamName())

class Cricket:
    teamName="India"
    @classmethod
    def getTeamName(cls):
        return cls.teamName
print(Cricket.getTeamName())


class Cricket:
    teamName = 'India'  
    @staticmethod
    def utility():
        print("This is a static method.")
c1 = Cricket()
c1.utility()
Cricket.utility()

class Example:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"My name is {self.name} and my age is {self.age}")
obj=Example("Ishu",18)
obj.show()


class Example:
    name = "Default Name"  
    age = 0  
    def __init__(self, name, age):
        Example.name = name  
        Example.age = age
    @classmethod
    def show(cls):  
        print(f"My name is {cls.name} and my age is {cls.age}")
obj = Example("Alice", 25)
Example.show() 

class Example:
    @staticmethod
    def show(name, age): 
        print(f"My name is {name} and my age is {age}")
Example.show("Alice", 25)  

class Animal:
    def sound(self):
        print("Animal makes different sounds.")
class dog(Animal):
    def bark(self):
        print("Dog barks")
d=dog()
d.sound()
d.bark()


class Animal:
    def sound(self):
        print("Animal makes different sounds.")
class dog(Animal):
    def bark(self):
        print("Dog barks")
class cat(dog):
    def meow(self):
        print("Cat meows.")

c=cat()
c.sound()
c.bark()
c.meow()

class Father:
    def show_father(self):
        print("Father's Care")
class Mother:
    def show_mother(self):
        print("Mother's Love")
class Child(Father,Mother):
    def show_child(self):
        print("Children's Future")
c=Child()
c.show_father()  
c.show_mother()  
c.show_child()

class Addition:
    def add(self,a,b):
        return a+b
class Multiplication(Addition):
    def mul(self,a,b):
        return a*b
class Power(Multiplication):
    def pow(self,a,b):
        return a**b
p=Power()

x=int(input("Enter the value of A: "))
y=int(input("Enter the value of B: "))

print(f"Addition of {x} and {y} is equal to {p.add(x,y)}")
print(f"Multiplication of {x} and {y} is equal to {p.mul(x,y)}")
print(f"Power of {x} and {y} is equal to {p.pow(x,y)}")


class Addition:
    def add(self, a, b):
        return a + b
class Subtraction:
    def subtract(self, a, b):
        return a - b
class MathOperations(Addition, Subtraction):
    def multiply(self, a, b):
        return a * b   
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero!"
        return a / b
obj = MathOperations()

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"Addition of {x} and {y}: {obj.add(x, y)}")         
print(f"Subtraction of {x} and {y}: {obj.subtract(x, y)}")  
print(f"Multiplication of {x} and {y}: {obj.multiply(x, y)}")  
print(f"Division of {x} by {y}: {obj.divide(x, y)}")       


class math():
    def add(self,a,b,c=0):
        return a+b+c    #overloading method  #compile time polymorphism
obj=math()
print(obj.add(2,3))
print(obj.add(5,6,9))  #overload c=9 insted of c=0

class MathOperations:
    def calculate(self, a, b):
        return a + b  # 
class Subtract(MathOperations):
    def calculate(self, a, b):  # Overriding method         #run time polymorphism
        return a - b  # Subtraction instead of addition
add_obj = MathOperations()
sub_obj = Subtract()

print("Addition (10 + 5):", add_obj.calculate(10, 5))  
print("Subtraction (10 - 5):", sub_obj.calculate(10, 5)) 

class student:                    
    def __init__(self,name,marks):
        self.name=name                        #public attribute
        self.marks=marks                      #public attribute
    def display(self):                        # public method
        print(f"{self.name} has obtained {self.marks} marks.")
s1=student("Ishu",56)
s1.display()
print(s1.name)
print(s1.marks)


class Student:
    def __init__(self, name, marks):
        self._name = name    # Protected attribute
        self._marks = marks  # Protected attribute

    def _display(self):  # Protected method
        print(f"{self._name} has obtained {self._marks} marks.")

s1 = Student("Ishu", 56)

print(s1._name)   
print(s1._marks) 
s1._display()     


class Student:
    def __init__(self, name, marks):
        self.__name = name   # Private attribute
        self.__marks = marks # Private attribute
    def __display(self):  # Private method
        print(f"{self.__name} has obtained {self.__marks} marks.")
    def show(self):  # Public method to access private method
        self.__display()
s1 = Student("Ishu", 56)
s1.show()  


from abc import ABC, abstractmethod
class calculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def sub(self,a,b):
        pass
class simplecalculator(calculator):
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
calc = simplecalculator()
print(calc.add(10, 5))      
print(calc.sub(10, 5))  

import datetime

mydate = datetime.datetime.now()

print("__str__() string: ", mydate.__str__())
print()
print("str() string: ", str(mydate))
print()
print("__repr__() string: ", mydate.__repr__())
print()
print("repr() string: ", repr(mydate))