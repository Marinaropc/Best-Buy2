import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]



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

    shopping_list = []
    counter = 0
    for product in best_buy.get_all_products():
        if product.is_active():
            counter += 1
            print(f"{counter}. {product.show()}")
    print("-----")
    print ("When you want to finish order, enter an empty text.")

    while True:
        print("Which product # do you want?")
        product_number = input()
        if not product_number.strip():
            break
        try:
            integer_product = int(product_number)
            product_index = integer_product - 1
            product = best_buy.get_all_products()[product_index]
        except (ValueError, IndexError):
            print("Please enter a number between 1 and 3.")
            continue

        print("How many do you want?")
        while True:
            try:
                quantity = int(input())
                if quantity <= 0:
                    print("Please enter a number higher than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a number higher than 0.")
        if quantity > product.get_quantity():
            print("Please enter a number lower than the quantity available.")
            continue
        else:
            shopping_list.append((product, quantity))
            print(f"Added {quantity} of {product.name} to your shopping list.")
    try:
        print(f"The total cost is {product.buy(quantity)} dollars.")
    except UnboundLocalError:
        pass


def quit_program():
    """ Quits the program."""
    print("Thank you for shopping with us!")


def main():
    """ Main function that displays and handles user interface"""
    best_buy = store.Store(product_list)
    dispatch = {
        "1": start,
        "2": show_total_quantity,
        "3": make_order,
        "4": quit_program
    }
    while True:
        user_choice = user_input()
        if user_choice == "1":
            start(best_buy)
        elif user_choice == "2":
            show_total_quantity(best_buy)
        elif user_choice == "3":
            make_order(best_buy)
        elif user_choice == "4":
            dispatch[user_choice]()
            break
        else:
            print("Invalid input. Please try again.")



if __name__ == '__main__':
    main()