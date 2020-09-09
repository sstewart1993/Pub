
import unittest
from src.food import Food
class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food = Food("Pizza", 3.50, 3)

    def test_food_has_name(self):
        food_name = self.food.name 
        self.assertEqual("Pizza", food_name)

    def test_food_price(self):
        food_price = self.food.price 
        self.assertEqual(3.50, food_price)

    def test_rej_level(self):
        level = self.food.rej_level
        self.assertEqual(3, level)