from  CardValidation import *
import unittest

class CardValidationtest(unittest.TestCase):

    def test_validatecard_valid(self):
        results = validatecard(date(2022,2,22))
        self.assertEqual('Valid Card', results)
    def test_validatecard_expired(self):
        results = validatecard(date(2021,2,22))
        self.assertEqual('Invalid Card', results)

