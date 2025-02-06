def my_func():                              
    print("Hello World")
my_func()

def my_func(name):
    print("hello "+name)
my_func("YENSEE")
my_func("RUPALI")

def my_func(name,empid):
    print("hello "+name, "your employee id is: "+empid)
my_func("Yensee","3967")

def my_func(name,empid,city):
    print("hello "+name)
    print("Your empid is: "+empid)
    print("You live in "+city)
my_func("Yensee","3967","Ambala City")

def my_func(name,empid,city):
    print("hello "+name)
    print("Your empid is: "+empid)
    print("You live in "+city)
my_func(city="Ambala CIty",empid="3967",name="Yensee")

def my_func(city="Ambala"):
    print("I am from "+city)
my_func("Kurukshetra")
my_func("Karnal")
my_func()
my_func("Jalandhar")


def my_func(x):
    return 5*x
print(my_func(15))
print(my_func(6))
print(my_func(75))

def my_func(x,y):
    return x+y
print(my_func(5,6))
print(my_func(50,60))
print(my_func(85,75))



square= lambda x: x*x
print(square(5))

add=lambda x,y: x+y
print(add(5,6))


def local_func(a,b,c):              #local variable
    return a*b*c
print(local_func(5,6,5))

a=500                                  #global variable
def master_func(a):
    print()  
master_func(a)
print(a)

x=200
def my_func1():
    x=500
    print(x)
my_func1()
print(x)