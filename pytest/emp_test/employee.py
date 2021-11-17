""" Employee Class"""


class Employee:
    def __init__(self, firstname, lastname, year_of_birth, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.year_of_birth = year_of_birth
        self.salary = salary

    # get full name
    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    # get email firstname.lastname@emp.com
    def create_email(self):
        return f"{self.firstname}.{self.lastname}@emp.com".lower()

    # get age
    def get_age(self):
        return 2021 - self.year_of_birth

