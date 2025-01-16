

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
        self.promotion = None
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
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
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
        promotion_name = self.promotion.name if self.promotion else "None"
        return f"- {self.name}, Price: {self.price}, Quantity: {self.quantity}\nPromotion: {promotion_name}\n"


    def buy(self, quantity):
        """ Buys the product.
        Args:
            quantity (int): Quantity to buy.
        Returns:
            float: Total price of the order.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity.")

        if self.promotion:
            total_price = self.promotion.apply_discount(self, quantity)
        else:
            total_price = float(self.price * quantity)

        self.quantity -= quantity
        if self.quantity <= 0:
            self.deactivate()
        return total_price


    def set_promotion(self, promotion):
        """Assigns a promotion to the product.
        Args:
            promotion (Promotion): A Promotion object to apply to the product.
        """
        self.promotion = promotion


    def get_price_with_promotion(self, quantity):
        """Returns the price of the product.
        Args:
            quantity (int): Quantity of the product.
        Returns:
            float: Total price of the order.
        """
        if self.promotion:
            return self.promotion.apply_discount(self, quantity)
        else:
            return self.price * quantity


class NonStockedProduct(Product):


    def __init__(self, name, price):
        """ Initializes a non-stocked product with a name, price, and quantity.
        Args:
            name (str): Name of the product.
            price (float): Price of the product.
        """
        super().__init__(name, price, quantity = 0)


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

        if self.promotion:
            total_price = self.promotion.apply_discount(self, quantity)
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
        if maximum < 0:
            raise ValueError("Maximum quantity cannot be negative.")
        self.maximum = maximum


    def get_maximum(self):
        """ Returns the maximum quantity of the product.
        Returns:
            int: Maximum quantity of the product.
        """
        return self.maximum


    def set_quantity(self, quantity):
        """ Sets the quantity of the product. """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        super().set_quantity(quantity)


    def buy(self, quantity):
        """ Buys the product.
        Args:
            quantity (int): Quantity to buy.
        Returns:
            float: Total price of the order.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.get_maximum():
            raise ValueError("Quantity cannot be higher than 1.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity.")
        if self.promotion:
            total_price = self.promotion.apply_discount(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price