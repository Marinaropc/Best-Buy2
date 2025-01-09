import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(best_buy):
    """ Main function that displays and handles user interface"""
    print("Store Menu\n -----")
    while True:
        print(f"\n1. List all products in store"
              f"\n2. Show total amount in store"
              f"\n3. Make an order\n4. Quit")
        user_input = input("Please choose a number: ")
        print("-----")
        if user_input == "1":
            print(f"Here is the list of products in the store:\n")
            for product in best_buy.get_all_products():
                print(product.show())
            print("-----")

        elif user_input == "2":
            print(f"Total quantity in store: {best_buy.get_total_quantity()}")
            print("-----")

        elif user_input == "3":
            shopping_list = []
            counter = 0
            for product in best_buy.get_all_products():
                if product.is_active():
                    counter += 1
                    print(f"{counter}. {product.show()}")
            print("-----")
            print ("When you want to finish order, enter empty text.")

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
                            print("Please enter a number between 1 and 3.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a number between 1 and 3.")
                shopping_list.append((product, quantity))
                print(f"Added {quantity} of {product.name} to your shopping list.")
            print(f"The total cost is {product.buy(quantity)} dollars.")
        elif user_input == "4":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid input. Please try again.")

start(best_buy)