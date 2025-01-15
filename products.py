from threading import activeCount


class Product:


    def __init__(self, name, price, quantity):
        """ Initializes a product with a name, price, and quantity.
        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            quantity (int): Quantity of the product.
        """
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
        """ Returns the quantity of the product.
        Returns:
        float: Quantity of the product.
        """
        return float(self.quantity)


    def set_quantity(self, quantity):
        """ Sets the quantity of the product.
        Args:
            quantity (int): New quantity of the product.
        """
        if quantity == 0:
            self.deactivate()


    def is_active(self):
        """ Returns whether the product is active.
        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active


    def activate(self):
        """ Activates the product """
        self.active = True


    def deactivate(self):
        """ Deactivates the product """
        self.active = False


    def show(self):
        """ Returns a string representation of the product.
        Returns:
            str: String representation of the product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """ Buys the product.
        Args:
            quantity (int): Quantity to buy.
        Returns:
            float: Total price of the order.
        """
        if quantity > self.quantity:
            raise ValueError("Not enough quantity.")
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        total_price = float(self.price * quantity)
        return total_price


class NonStockedProduct(Product):


    def __init__(self, name, price):
        """ Initializes a non-stocked product with a name, price, and quantity.
        Args:
            name (str): Name of the product.
            price (float): Price of the product.
        """
        super().__init__(name, price, quantity = 0)
        self.active = True


    def set_quantity(self, quantity):
        """ Sets the quantity of the product. """
        if quantity != 0:
            raise ValueError("Cannot set quantity to non-zero value.")


    def buy(self, quantity):
        """ Buys the product.
        Args:
            quantity (int): Quantity to buy.
        Returns:
            float: Total price of the order.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        total_price = float(self.price * quantity)
        return total_price


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum):
        """ Initializes a limited product with a name, price, and quantity.
        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            quantity (int): Quantity of the product.
            maximum (int): Maximum quantity of the product.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum
        self.active = True


    def set_quantity(self, quantity):
        """ Sets the quantity of the product. """
        self.quantity = quantity


    def buy(self, quantity):
        """ Buys the product.
        Args:
            quantity (int): Quantity to buy.
        Returns:
            float: Total price of the order.
        """
        if quantity > 1:
            raise ValueError("Quantity cannot be higher than 1.")
        total_price = float(self.price * quantity)
        return total_price