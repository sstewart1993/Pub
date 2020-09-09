import unittest
from src.pub import Pub 


class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, "whiskey")

    def test_pub_has_name(self):
        pub_name = self.pub.name 
        self.assertEqual("The Prancing Pony", pub_name)

    def test_pub_till(self):
        pub_till = self.pub.till 
        self.assertEqual(100.00, pub_till)

    def test_pub_drink(self):
        pub_drink = self.pub.drink 
        self.assertEqual("whiskey", pub_drink)