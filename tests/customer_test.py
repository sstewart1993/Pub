import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub


class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("John", 24.60, 6, 30)
        self.drink = Drink("Beer", 2.50, 3)
        self.pub = Pub("The Prancing Pony", 100.00, "whiskey")

    def test_pub_has_name(self):
        name = self.customer.name
        self.assertEqual("John", name)

    def test_wallet(self):
        wallet = self.customer.wallet
        self.assertEqual(24.60, wallet)

        
    def test_buy_drink(self):
        wallet = self.customer.wallet
        price = self.drink.price
        till = self.pub.till
        self.customer.buy_drink(wallet, price)
        self.pub.increase_till(till, price)
        self.assertEqual(22.10, self.customer.wallet)
        self.assertEqual(102.50, self.pub.till)
        


