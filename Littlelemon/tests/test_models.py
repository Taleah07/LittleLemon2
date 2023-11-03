from django.test import TestCase
from restaurant.models import menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = menu.objects.create(title="chicken", price=10, inventory=3)
        self.assertEqual(item, "chicken : 10")

    def test_get_item(self):
        item = menu.objects.create(title = "soup", price= 12, inventory=5)
        self.assertEqual(item, "soup : 12" )