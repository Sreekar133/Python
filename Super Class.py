# class Father:
#     def __init__(self,property=0):
#         self.property = property
#
#     def details(self):
#         print(f"The property is {self.property}")
#
# class Son(Father):
#     def __init__(self,property1=0,property=0):
#         super().__init__(property)
#         self.property1 = property1
#
#     def details(self):
#         print("The assests of son is" ,self.property+self.property1)
#
# S=Son(2000,8000)
# print(S.details())

class Square:
    def __init__(self,x):
        self.x = x

    def square_area(self):
        return self.x*self.x

class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def rectangle_area(self):
        return self.x*self.y


area = Rectangle(4,5)
print(area.rectangle_area())




