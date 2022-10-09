from django.test import TestCase

# Create your tests here.

from .models import Thing
from django.core.exceptions import ValidationError
class ThingModelTestCase(TestCase):

    def test_Construction(self):
        self.thing = Thing(
            name = 'Apple',
            description = 'A red apple',
            quantity = 10
            #self.thing.full_clean()
        )


    def _assert_model_is_valid(self):
        try:
            #Checks if user is valid for DB or not.
            self.thing.full_clean()

        except (ValidationError):
            self.fail('Test model should be valid')

            '''checks if user is invalid for DB'''
    def _assert_model_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()
'''
    def test_valid_thing(self):
        self._assert_model_is_valid()'''
