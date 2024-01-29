# class Student:
#     def __init__(self,n=" ",m=0):
#         self.name = n
#         self.marks = m
#
#     def details(self):
#         print(f"my name is {self.name}")
#         print(f"my marks are {self.marks}")
#
#     def calculate(self):
#         if (self.marks >= 600):
#             print("First grade")
#         elif (self.marks >= 500):
#             print("Second Grade")
#         elif (self.marks >= 350):
#             print("Third grade")
#         else:
#             print("Fail")
#
# n = int(input("enter the numbers"))
#
# i = 0
# while i < n :
#     name = input("enter the name")
#     marks = int(input("enter the marks"))
#
#     Sreekar = Student(name,marks)
#     Sreekar.details()
#     Sreekar.calculate()
#     i+=1


# class Student:
#
#     def set_name(self,name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_marks(self,marks):
#         self.marks = marks
#
#     def get_marks(self):
#         return self.marks
# n = int(input("enter the numbers"))
# i=0
# while i<n:
#     s=Student()
#     name = input("enter the name")
#     s.set_name(name)
#     marks = input("enter the marks")
#     s.set_marks(marks)
#
#     print(f"my name is {s.get_name()}")
#     print(f"my marks are {s.get_marks()}")
#     i+=1


# class Birds:
#     wings = 2
#
#     @classmethod
#     def birds_wings(cls,name):
#         print(f"The name is {name} and has {cls.wings} wings")
#
#
# Birds.birds_wings("sparrow")
# Birds.birds_wings("parrot")

class Bank:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance

    def deposit(self,amt):
        self.balance+=amt
        return self.balance

    def withdrawal(self,amt):
        if amt > self.balance:
            print("no sufficient amount")
        else:
            self.balance -=amt
        return self.balance

sreekar = Bank("sreekar",50)
print(sreekar.deposit(1000))
print(sreekar.withdrawal(500))






