import unittest
import calc


class TestCalc(unittest.TestCase):

    """Test add function"""

    def test_add(self):
        result = calc.add(2, 3)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
