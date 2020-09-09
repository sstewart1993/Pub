class Pub:

    def __init__(self, input_name, input_till, input_drink):
        self.name = input_name
        self.till = input_till
        self.drink = input_drink

    def increase_till(self, till, price):
        self.till = till + price