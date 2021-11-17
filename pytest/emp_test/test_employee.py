"""Test Cases for Employee Object"""

from employee import Employee
import pytest


class TestEmployee:
    @pytest.fixture
    def employee(self):
        return Employee("May", "Agbo", 1999, 2000)

    def test_fullname(self, employee):
        assert employee.fullname == "May Agbo"

    def test_email(self, employee):
        assert employee.create_email() == "may.agbo@emp.com"

    @pytest.mark.parametrize("current_year", [(2021)])
    def test_get_age(self, employee, current_year):
        # current year - year of birth
        assert employee.get_age() == current_year - employee.year_of_birth

    @pytest.mark.messages
    @pytest.mark.parametrize("x, y, total", [(2, 3, 5), (4, 2, 8)])
    def test_sum(self, x, y, total):
        assert x + y == total
