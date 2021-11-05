import unittest
import calc


class TestCalc(unittest.TestCase):

    """Test add function"""

    """Test edge cases: to ensure all possible scenarios are covered"""

    def test_add(self):
        self.assertEqual(calc.add(6, 3), 9, msg="Addition failed")
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

        """Test subtract function"""

    def test_subtract(self):
        self.assertEqual(calc.subtract(6, 3), 3)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

        """Test multiply function"""

    def test_multiply(self):
        self.assertEqual(calc.multiply(6, 3), 18)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

        """Test divide function"""

    def test_divide(self):
        self.assertEqual(calc.divide(6, 3), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # test for exception raised, if exception is raised
        # by the function, this test should pass else fail

        # self.assertRaises(ValueError, calc.divide, 10, 2)

        # use context manager instead for exceptions
        with self.assertRaises(ValueError):
            calc.divide(10, 2)


if __name__ == "__main__":
    unittest.main()
