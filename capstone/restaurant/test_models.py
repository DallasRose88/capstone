from django.test import TestCase 
from .models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title = "Pizza", Price= 10, Inventory=100)
        self.assertEqual(str(item), "Menu: Pizza : 10")