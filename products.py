

class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
            return float(self.quantity)

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("quantity must be greater than 0")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Not enough quantity.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        total_price = float(self.price * quantity)
        return total_price

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

#print(bose.buy(50))
#print(mac.buy(100))
#print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()