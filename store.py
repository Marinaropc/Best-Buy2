import products

class Store:
    def __init__(self, products_list):
        self.products = products_list

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        return self.products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except ValueError as e:
                print(e)
        return f"Order cost: {total_price} dollars."


