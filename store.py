import products

class Store:


    def __init__(self, products_list):
        """ Initializes a store with a list of products.
        Args:
            products_list (list): List of products.
        """
        self.products = products_list


    def add_product(self, product):
        """ Adds a product to the store.
        Args:
            product (Product): Product to add.
        """
        self.products.append(product)


    def remove_product(self, product):
        """ Removes a product from the store.
        Args:
            product (Product): Product to remove.
        """
        self.products.remove(product)


    def get_total_quantity(self):
        """ Returns the total quantity of products in the store.
        Returns:
            int: Total quantity of products in the store.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        """ Returns a list of all products in the store.
        Returns:
            list: List of all products in the store.
        """
        return self.products


    def order(self, shopping_list):
        """ Orders the products in the shopping list.
        Args:
            shopping_list (list): List of products to order.
        Returns:
            str: String representation of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except ValueError as e:
                print(e)
        return f"Order cost: {total_price} dollars."
