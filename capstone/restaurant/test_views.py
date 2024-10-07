from django.test import TestCase 
from django.urls import reverse 
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.item = Menu.objects.create(Title="Food", Price= 5, Inventory= 50)
        self.item2 = Menu.objects.create()
        
    def test_getall(self):
        url = reverse('http://127.0.0.1:8000/restaurant/menu/')
        response = self.client.get(url)
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data, expected_data)