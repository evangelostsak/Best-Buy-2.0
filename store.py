from products import Product
from typing import List

#test
class Store:
    def __init__(self, products):
        """initializing the store with products list"""
        self.products = products

    def add_product(self, product):
        """Adds a new product to the store"""
        self.products.append(product)

    def remove_product(self, product):
        """Removes product from the store"""
        if product in self.products:
            self.products.remove(product)  # Only if exists

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products available"""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """Gets a list of active products in store"""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """Gets order, returns total price"""
        total_price = 0.0

        for item in shopping_list:
            product, quantity = item
            if product in self.products:
                # Trying to buy the given quantity
                total_price += product.buy(quantity)

        return total_price
