class Car(object):
    def __init__(self, make, model, year, condition, kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
        self.priceL = 6.50

    def gas_cost(self):
        return self.kms * self.priceL

    def change_price_per_liter(self, new_price):
        self.priceL = new_price

    def display(self, show_all=True):
        if show_all:
            print(f"This car is a {self.make} from {self.model}, it is {self.year} and has {self.condition} condition.")
            print(f"Gas cost per liter would come out ${self.gas_cost():.2f}")
        else:
            print("This car is missing data in the database")

# Creating instances of the Car class
whip = Car('Ford', 'Fusion', 2012, "Mint Condition", 12430)  # Adjusted kms for demonstration
whip2 = Car('Ford', 'Fusion', 2012, "Mint Condition", 15000)

# Displaying car information and gas cost
whip.display()

# Changing the price per liter and displaying updated gas cost
whip.change_price_per_liter(7.11)  # Change the price per liter
whip.display()
