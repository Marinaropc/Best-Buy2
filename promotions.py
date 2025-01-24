

class Promotion:


    def __init__(self, name):
        """ Initializes a promotion with a name.
        Args:
            name (str): Name of the promotion.
        """
        self.name = name
        self.active = True


    def is_active(self):
        """ Returns whether the promotion is active.
        Returns:
            bool: True if the promotion is active, False otherwise.
        """
        return self.active


    def activate(self):
        """ Activates the promotion """
        self.active = True


    def deactivate(self):
        """ Deactivates the promotion """
        self.active = False


class SecondHalfPrice(Promotion):

    def __init__(self, name):
        """ Initializes a second half price promotion with a name.
        Args:
            name (str): Name of the promotion.
        """
        super().__init__(name)

    def apply_discount(self, product, quantity):
        """ Applies the promotion to a product.
        Args:
            product (Product): Product to apply the promotion to.
            quantity (int): Quantity of the product.
        Returns:
            float: total_price
        """
        if quantity < 2:
            return product.price * quantity
        full_price_item = quantity // 2
        discount_item = quantity - full_price_item
        total_price = (full_price_item * product.price) + (discount_item * product.price * 0.5)
        return total_price


class ThirdOneFree(Promotion):

    def __init__(self, name):
        """ Initializes a third one free promotion with a name.
        Args:
            name (str): Name of the promotion.
        """
        super().__init__(name)

    def apply_discount(self, product, quantity):
        """ Applies the promotion to a product.
        Args:
            product (Product): Product to apply the promotion to.
            quantity (int): Quantity of the product.
        Returns:
            float: total_price
        """
        full_price = product.price * quantity
        if quantity < 2:
            return full_price

        if quantity >= 3:
            how_many_free = quantity // 3
            total_price = full_price - product.price * how_many_free
            return total_price


class PercentDiscount(Promotion):


    def __init__(self, name, percent):
        """ Initializes a percent discount promotion with a name and a percent.
        Args:
            name (str): Name of the promotion.
            percent (int): Percent of the discount.
        """
        super().__init__(name)
        if not (0 <= percent <= 100):
            raise ValueError("percentage must be between 0 and 100")
        self.percent = percent

    def apply_discount(self, product, quantity):
        """ Applies the promotion to a product.
        Args:
            product (Product): Product to apply the promotion to.
            quantity (int): Quantity of the product.
        Returns:
            float: total_price
        """
        full_price = product.price * quantity
        discount = (full_price * self.percent) / 100
        total_price = full_price - discount
        return total_price
