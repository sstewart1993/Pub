class Customer:
    def __init__(self, input_name, input_wallet, input_drunkness, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.drunkness = input_drunkness
        self.age = input_age
        
    # def buy_drink(self, price):
    #     self.wallet - self.price 

    # def buy_drink(self, wallet, price):
    #     new_wallet = wallet - price


    def buy_drink(self, wallet, price):
        self.wallet = wallet - price