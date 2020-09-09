import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Beer", 2.50, 3)

    def test_drink_has_name(self):
        drink_name = self.drink.name 
        self.assertEqual("Beer", drink_name)

    def test_drink_price(self):
        drink_price = self.drink.price 
        self.assertEqual(2.50, drink_price)

    def test_alcohol_level(self):
        level = self.drink.alcohol_level
        self.assertEqual(3, level)