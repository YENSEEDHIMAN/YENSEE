#PROGRAM 1
class parrot:
    Name=""
    Age=0
parrot1=parrot()
parrot1.Name="Mithu"
parrot1.Age=3
print(f"{parrot1.Name} is {parrot1.Age} years old")
print()

#PROGRAM 2
class person:
    name=""
    age=0
person1=person()
person1.name=str(input("Enter your name: "))
person1.age=int(input("Enter your age: "))
print(f"Your name is {person1.name} and your age is {person1.age}")

#PROGRAM 3
class car:
    name=""
    manufactur_year=""
car1=car()
car1.name=str(input("enter the car name: "))
car1.manufactur_year=str(input("This car manufactur in: "))
print(f"{car1.name} is manufacture in:{car1.manufactur_year} ")
print()

#PROGRAM 4
class car:
    name=""
    car_price=0
car1=car()
car1.name=str(input("Enter the car name: "))
print("Enter the range")
print("1:1-5L")
print("2:5-10L")
print("3:10-15L")
while True:
    car_price=int(input("Enter the number 1, 2, 3 : "))
    if car_price in [1,2,3]:
        car1.car_price=car_price
        break
    else:
        print("Invalid Valid: Please Choose from 1,2,3")
if car1.car_price in [1,2,3]:
    print(f"Yes ! {car1.name} is available in the selected range")
else:
    print("Sorry ! Not available")
print()

#PROGRAM 5
class car:
    name=""
    car_price=0
car1=car()
while True:
    name=str(input("Enter the car name:  "))
    if name in ["Honda","Audi","Tata","Maruti","Kia","Swift","Skoda","Mahindra","Thar"]:
        car1.name=name
        break
    else:
        print("Invalid Valid: Please Choose from Honda, Audi, Tata, Maruti, Kia, Swift, Skoda,Mahindra, Thar")
print("Enter the range")
print("1: 1-5L")
print("2: 5-10L")
print("3: 10-15L")
while True:
    car_price=int(input("Enter the number 1, 2, 3 : "))
    if car_price in [1,2,3]:
        car1.car_price=car_price
        break
    else:
        print("Invalid Valid: Please Choose from 1,2,3")
if car1.car_price in [1,2,3]:
    print(f"Yes ! {car1.name} is available in the selected range")
else:
    print("Sorry ! Not available")
print()

#PROGRAM 6
class Animal:
    def eat(Self):
        print("i can eat")
    def sleep(Self):
        print("i can sleep")
class Dog(Animal):
    def bark(Self):
        print("i can bark")
Animal1=Animal()
Dog1=Dog()
Animal1.eat()
Animal1.sleep()
Dog1.bark()
Dog1.eat()
print()

#PROGRAM 7
class person:
    name=""
    age=0
person1=person()
person1.name="Khushi"
person1.age="20"
print(f"{person1.name} is my name and i am {person1.age} years old")
print()


#PROGRAM 8
class Car:
    def show_brand(self,brand):
        print(f"Brand name :{brand} ")
brand1=Car()
brand1.show_brand("TATA")


#PROGRAM 9
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def show_balance(self):
        print(f"Hello {self.holder}, your bank balance is: ${self.balance}")


valid_accounts = {
    "John": (1001, 5000),
    "Aarti": (1002, 7500),
    "Rupali": (1003, 6200),
    "Khushi": (1004, 8100),
    "Tia": (1005, 4500),
    "Anaya": (1006, 9900),
    "Anika": (1007, 7300),
    "Shiv": (1008, 5400),
    "Misthi": (1009, 8800)
}

holder = input("Enter your name: ")
account_num = int(input("Enter your account number: "))

if holder in valid_accounts and account_num == valid_accounts[holder][0]:
    balance = valid_accounts[holder][1]
    account1 = BankAccount(holder, balance)
    account1.show_balance()
else:
    print("Error: Name and Account Number do not match!")


