# class A(object):
#     def method(self):
#         print("A method")
#         super().method()
#
# class B(object):
#     def method(self):
#         print("B method")
#         super().method()
#
# class C(object):
#     def method(self):
#         print("C method")
#
# class X(A,B):
#     def method(self):
#         print("X is a child class")
#         super().method()
#
#
# class Y(B,C):
#     def method(self):
#         print("Y is another child class")
#         super().method()
#
# class Z(X,Y,C):
#     def method(self):
#         print("z class")
#         super().method()
#
# test = Z()
# print(test.method())

#
# class Duck:
#     def talk(self):
#         print("quack quack")
#
# class Human:
#     def talk(self):
#         print("Hi! Hello")
#
# class Dog:
#     def bark(self):
#         print("Bow Bow")
#
#
# def call_talk(obj):
#     if hasattr(obj,'talk'):
#         obj.talk()
#     elif hasattr(obj,'bark'):
#         obj.bark()
#
#
# x=Duck()
# call_talk(x)
# x=Dog()
# call_talk(x)

#
# class BookX:
#     def __init__(self,pages):
#
#         self.pages = pages
#
#     def __add__(self, other):
#        return self.pages + other.pages
#
# class BookY:
#     def __init__(self,pages):
#         self.pages = pages
#
# b1 = BookX(100)
# b2 = BookY(150)
# print(b1+b2)
#
#
# class Ramayana:
#     def __init__(self,pages):
#         self.pages = pages
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
# class Mahabharat:
#     def __init__(self,pages):
#         self.pages = pages
#
#
#
# a = Ramayana(100)
# b = Mahabharat(150)
#
# if a>b:
#     print("ramayaba has more pages")
# else:
#     print("Mahabharata has moe pages")

import math
class Square:
    def area(self,x):
        print(f"area of square is {x*x}")

class Circle(Square):
    def area(self,x):
        print(f"area of circle us {math.pi*x*x}")



a = Circle()
a.area(2)
a=Square()
a.area((2))

