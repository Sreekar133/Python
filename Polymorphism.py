class Teacher:
    def __init__(self,id,name,year,address):
        self.id=id
        self.name = name
        self.year = year
        self.address = address

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_year(self):
        return self.year
    def get_address(self):
        return self.address


class Student(Teacher):
    def get_studentid(self,id):
        self.id=id
        return self.id



