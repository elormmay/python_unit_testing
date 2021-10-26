import requests


class Employee:
    """A sample employee class"""

    raise_amt = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com".lower()

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # unittest mocking
    # mocking: getting a employee's schedule from a website even of the site is down
    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.last_name}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"


# emp = Employee("May", "Agbo", 100)
# emp.apply_raise()

# print(f"Name: {emp.fullname} \nEmail: {emp.email} \nSalary: {emp.pay}")
