from products import Product, NonStockedProduct, LimitedProduct
from store import Store
import promotions


def inventory_setup():
    """Initializing new inventory"""

    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    return Store(product_list)


def press_to_continue():
    """Some addition to the program to make it more likable, hope its alright"""

    print()
    input("Press anything to continue...")
    print()


def exit_program():
    """quitting func"""
    print(f"\nThank you for using Best Buy!")
    print("Have a nice day!")


def menu():
    """show menu func"""

    print("\n---Store Menu---\n")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store):
    """Lists all available products to the user"""
    products = store.get_all_products()
    if products:
        for index, product in enumerate(products, start=1):
            print(f"{index}. -- {product.show()}")
    else:
        print("All products are out of stock or unavailable")


def show_total_quantity(store):
    """Showing the total amount to the user"""
    total = store.get_total_quantity()
    print(f"Total amount in store: {total} items")


def make_order(store):
    """Order mechanics func. user gets asked what he wants to buy. he enters a number from the list
    enters quantity and item is stored in the shopping list until user decides to pay by clicking '0'
    """

    products = store.get_all_products()
    if not products:
        print("Out of luck! No products are available at the moment")
        return

    shopping_list = []
    while True:
        list_products(store)
        try:
            # -1 to match pythons indexing. we need to show and accept the items from 1 and not 0
            product_index = int(input("\nEnter the product number you'd like to buy (or 0 to stop): ")) - 1
            if product_index == -1:
                break
            if 0 <= product_index < len(products):
                quantity = int(input(f"Please enter the wished quantity for {products[product_index].name}: "))
                shopping_list.append((products[product_index], quantity))
            else:
                print("Invalid product number.")
        except ValueError:
            print("Please enter a valid number")

    if shopping_list:
        try:
            total_price = store.order(shopping_list)
            print(f"Total order price amount: {total_price} euros.")
        except ValueError as e:
            print(f"Oops! {e}. Please try that again")
    else:
        print("Looks like you changed your mind")


def start(store):
    """actions menu. function pointers for better view.
    program is running until users wants to exit by '4'
    nothing but '1-4' is accepted in order to proceed
    """

    menu_options = {
        1: list_products,
        2: show_total_quantity,
        3: make_order
    }

    while True:
        menu()
        try:
            menu_choice = int(input("\nWhat would you like to do? (1-4): "))

            if menu_choice in menu_options:

                menu_options[menu_choice](store)
                press_to_continue()

            if menu_choice == 4:
                exit_program()
                break

        except ValueError:
            print("Invalid input! Try that again")


def main():
    """Main function. Welcoming the user once and proceeds with the start function"""

    print("\nWelcome to Best Buy!")
    best_buy = inventory_setup()
    start(best_buy)


if __name__ == "__main__":
    main()
