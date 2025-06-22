from django.test import TestCase
from restaurant.models import menu

class MenuModelTest(TestCase):
    def test_str_representation(self):
        """
        O método __str__ deve retornar 'IceCream : 80.00'
        quando o item tem title='IceCream' e price=80.
        """
        item = menu.objects.create(title="IceCream", price=80, inventory=100)
        expected = "IceCream : 80.00"      # agora bate com o __str__()
        self.assertEqual(str(item), expected)