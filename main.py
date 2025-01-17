import products
import store
import promotions

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", 30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)
product_list[2].set_promotion(thirty_percent)

# Initialize store
best_buy = store.Store(product_list)

def user_input():
    """ Displays and handles user interface, returns user choice."""
    print("\nStore Menu\n -----")
    print(f"\n1. List all products in store"
          f"\n2. Show total amount in store"
          f"\n3. Make an order\n4. Quit")
    user_choice = input("Please choose a number: ")
    print("-----")
    return user_choice


def start(best_buy):
    """ Displays a list of all products in the store."""
    print(f"Here is the list of products in the store:\n")
    for item in best_buy.get_all_products():
        print(item.show())
    print("-----")


def show_total_quantity(best_buy):
    """ Displays the total quantity of products in the store."""
    print(f"Total quantity in store: {best_buy.get_total_quantity()}")
    print("-----")


def make_order(best_buy):
    """ Displays the buying menu, and handles user input for making an order."""
    active_products = [product for product in
                       best_buy.get_all_products() if product.is_active()]
    shopping_list = []

    for index, product in enumerate(active_products):
        print(f"{index+1}. {product.show()}")

    print("-----")
    print ("When you want to finish order, enter an empty text.")
    print("-----")

    while True:
        print("Which product # do you want?")
        product_number = input()

        if not product_number.strip():
            break

        try:
            product_index = int(product_number) - 1
            if product_index < 0 or product_index >= len(active_products):
                print("Please enter one of the displayed index number.")
                continue

            product = active_products[product_index]
            if isinstance(product, products.LimitedProduct):
                already_ordered = any(p == product for p, _ in shopping_list)
                if already_ordered:
                    print("You can only purchase a LimitedProduct once.")
                    continue
        except (ValueError, IndexError):
            print("Please enter one of the displayed index number.")
            continue

        print("How many do you want?")
        while True:

            string_quantity = input()
            if not string_quantity.strip():
                break

            try:
                quantity = int(string_quantity)

                if quantity <= 0:
                    print("Please enter an integer number higher than 0.")
                    continue

                if (isinstance(product, products.LimitedProduct)
                        and quantity > product.get_maximum()):
                    print("Please enter a number lower "
                          "than the maximum amount per purchase.")
                    continue

                if not isinstance(product, products.NonStockedProduct):
                    available_stock = product.get_quantity()
                    already_ordered = sum(q for p, q in shopping_list if p == product)
                    remaining_stock = available_stock - already_ordered

                    if remaining_stock <= 0:
                        print("Sorry, this product is sold out.")
                        break

                    if quantity > remaining_stock:
                        print("Please enter a number lower than the quantity available.")
                        continue

                    elif quantity > 1000000:
                        print("Please enter a number under the stock available.")
                        continue

                shopping_list.append((product, quantity))
                print(f"Added {quantity} of {product.name} to your shopping list.")
                break

            except ValueError:
                print("Please enter an integer number higher than 0.")

    total_cost = 0
    for item, quantity in shopping_list:
        total_cost += item.buy(quantity)
    print(f"The total cost is {total_cost} dollars.")


def quit_program():
    """ Quits the program."""
    print("Thank you for shopping with us!")


def main():
    """ Main function that displays and handles user interface"""
    best_buy_store = store.Store(product_list)
    dispatch = {
        "1": lambda: start(best_buy_store),
        "2": lambda: show_total_quantity(best_buy_store),
        "3": lambda: make_order(best_buy_store),
        "4": quit_program
    }

    while True:
        user_choice = user_input()
        if user_choice in dispatch:
            dispatch[user_choice]()
            if user_choice == "4":
                break
        else:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    main()