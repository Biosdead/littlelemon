# tests/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .models import menu
from .serializers import MenuItemSerializer   # ajuste o import se o caminho for outro

class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # cria dados apenas UMA vez para toda a classe de testes
        cls.item1 = menu.objects.create(title="IceCream", price=80, inventory=100)
        cls.item2 = menu.objects.create(title="Burger",   price=50, inventory=50)

    def test_get_all_menu_items(self):
        """
        A rota /menu/ deve devolver todos os itens serializados.
        """
        url = reverse("restaurant/menu")             # depende do seu DefaultRouter
        response = self.client.get(url)

        # ➜ serializa o queryset exatamente como a view faz
        queryset = menu.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)