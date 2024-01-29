# class salary_inc:
#
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#
#     def display(self):
#         print(f"id={self.id}")
#         print(f"name={self.name}")
#         print(f"salary={self.salary}")
# class Myclass:
#     @staticmethod
#     def salary_details(e):
#         e.salary+=1000
#         e.display()
#
# e=salary_inc(1,"sreekar",1000)
# Myclass.salary_details(e)

class Details:
    def __init__(self):
        self.name = "Sreekar"
        self.age = self.dob()

    def display(self):
        print(f"name = {self.name}")
        print(f"dob = {self.age}")

        class dob:
            def __init__(self):
                self.date = 20
                self.month = 8
                self.year = 1997

            def display(self):
                print(f"{self.date}/{self.month}/{self.year}")


p = Details()
p.display()

q=p.age
q.display()