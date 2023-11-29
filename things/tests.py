"""Unit tests for ThingForm"""
from django.test import TestCase

from things.forms import ThingForm
from things.models import Thing


# Create your tests here.
class ThingFormTestCase(TestCase):
    def setUp(self):
        self.form_input = {
            "name": "Thing1",
            "description": "Hey I'm Thing1",
            "quantity": 20
        }

    # ThingForm must accept valid input
    def test_thing_is_valid(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    # ThingForm must reject with invalid input
    def test_name_is_unique(self):
        thing1 = Thing.objects.create(name="Thing1",
                                      description="Hey I'm Thing1!",
                                      quantity=0)
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_name_is_less_than_or_equal_to_35_characters(self):
        self.form_input["name"] = "T" * 36
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_description_is_less_than_or_equal_to_120_characters(self):
        self.form_input["description"] = "T" * 121
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_quantity_is_more_than_0(self):
        self.form_input["quantity"] = -1
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_quantity_is_less_than_or_equal_to_100(self):
        self.form_input["quantity"] = 101
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
