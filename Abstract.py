# from abc import  *
# class Car(ABC):
#     def __init__(self,reg_no):
#         self.reg_no = reg_no
#
#     def fuel(self):
#         print("please open the diesel tank",self.reg_no)
#         print("fill in the petrol")
#
#     @abstractmethod
#     def steering(self):
#         pass
#
#     @abstractmethod
#     def vehicle_tyepe(self):
#         pass
#
#
# class Maruthi(Car):
#
#     def steering(self):
#         print("This is old structured steering")
#
#     def vehicle_tyepe(self):
#         print("This is an manual gear type")
#
#
# class Santro(Car):
#
#     def steering(self):
#         print("This is new structured steering")
#
#     def vehicle_tyepe(self):
#         print("This is an automatic car")
#
#
#
# a = Maruthi(1000)
# a.fuel()
# a.steering()
# a.vehicle_tyepe()
#
# b=Santro(1200)
# b.fuel()
# b.steering()
# b.vehicle_tyepe()


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for i in range(nr_letters):
    password.append(random.choice(letters))

for k in range(nr_symbols):
    password.append(random.choice(symbols))

for j in range(nr_numbers):
    password.append(random.choice(numbers))
for i in password:
    print(i,end='')


