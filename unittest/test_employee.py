import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    # class functions to run before for any test rans
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    # class function runs after tests ran
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # function runs before any test runs
    def setUp(self):
        print("setUp")
        self.emp = Employee("Cal", "Agbo", 200)

    # function runs after tests ran
    def tearDown(self):
        print("tearDown\n")

    # test email
    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp.email, "cal.agbo@email.com")

        self.emp.first_name = "May"
        self.assertEqual(self.emp.email, "may.agbo@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp.fullname, "Cal Agbo")

        self.emp.first_name = "May"
        self.emp.last_name = "Agbod"
        self.assertEqual(self.emp.fullname, "May Agbod")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp.apply_raise()
        self.assertEqual(self.emp.pay, 210)

    def test_monthly_schedule(self):
        print("test_monthly_schedule")
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp.monthly_schedule("May")
            print("----", schedule)
            mocked_get.assert_called_with("http://company.com/Agbo/May")
            self.assertEqual(schedule, "Success")

            # testing for if return value is false eg. site down or wrong url
            mocked_get.return_value.ok = False

            schedule = self.emp.monthly_schedule("May")
            print("----", schedule)
            mocked_get.assert_called_with("http://company.com/Agbo/May")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()

