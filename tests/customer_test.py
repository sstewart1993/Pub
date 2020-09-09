import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food


class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("John", 24.60, 12, 30)
        self.drink = Drink("Beer", 2.50, 3)
        self.pub = Pub("The Prancing Pony", 100.00, "whiskey")
        self.food = Food("Pizza", 3.50, 3)

    def test_name(self):
        name = self.customer.name
        self.assertEqual("John", name)

    def test_wallet(self):
        wallet = self.customer.wallet
        self.assertEqual(24.60, wallet)

    def test_age(self):
        self.assertEqual(30, self.customer.age)
        
    def test_buy_drink(self):
        wallet = self.customer.wallet
        price = self.drink.price
        till = self.pub.till
        self.customer.buy_drink(wallet, price)
        self.pub.increase_till(till, price)
        self.assertEqual(22.10, self.customer.wallet)
        self.assertEqual(102.50, self.pub.till)

    def test_drunkness(self):
        self.assertEqual(12, self.customer.drunkness)

    def test_buy_drinks(self):
        if self.pub.refusal(self.customer.drunkness):
            self.customer.buy_drinks(self.drink.alcohol_level)
            self.assertEqual(15, self.customer.drunkness)

    def test_buy_food(self):
        self.customer.buy_food(self.food.rej)
        self.assertEqual(9, self.customer.drunkness)


    


    
        


