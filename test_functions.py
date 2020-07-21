import unittest
from functions import get_part_of_day_from_hour, is_evening

class TestStringMethods(unittest.TestCase):

    def test_morning(self):
        self.assertEqual(get_part_of_day_from_hour(1), 'Morning')

    def test_noon(self):
        self.assertEqual(get_part_of_day_from_hour(12), 'Noon')

    def test_afternoon(self):
        self.assertEqual(get_part_of_day_from_hour(15), 'Afternoon')

    def test_evening(self):
        self.assertEqual(get_part_of_day_from_hour(20), 'Evening')

    def test_night(self):
        self.assertEqual(get_part_of_day_from_hour(22), 'Night')

    def test_is_evening(self):
        self.assertTrue(is_evening(20))
        self.assertFalse(is_evening(2))




if __name__ == '__main__':
    unittest.main()





## first you write a test that fails, then write the code so that it can pass the test
## If you have more code than you write a test for, then you might miss test coverage - the next step might pass the test without you writing a test for that specific piece

## You're defining 'evening' in two different functions, use one function for the other.
## return statement can be its own boolean return function == x (will return true or false)


## AssertionError:
## - Morning (Problem is function shouldn't have morning but it does)
## + Noon (Function should have noon but doesn't)