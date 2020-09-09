class Pub:

    def __init__(self, input_name, input_till, input_drink):
        self.name = input_name
        self.till = input_till
        self.drink = {}

    def increase_till(self, till, price):
        self.till = till + price

    def age_check(self, customer):
        if customer.age < 18:
            print("service refused")
        else:
            print("Here you go")

    def refusal(self, drunk):
        if drunk >= 10:
            print("Go home!")
            return False

    def stock(self):
        return self.drink
        