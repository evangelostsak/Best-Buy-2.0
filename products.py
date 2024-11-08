class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product should not be empty")
        if price < 0:
            raise ValueError("Price should not be negative")
        if quantity < 0:
            raise ValueError("Quantity should not be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Added new promotion attribute

    def get_quantity(self) -> int:
        """Returns quantity of the product"""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Sets quantity of product
            deactivates product if negative
        """
        if quantity < 0:
            raise ValueError("Quantity should not be negative")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()  # only if out of stock

    def is_active(self) -> bool:
        """Returns state of product
            True for active, false otherwise"""
        return self.active

    def activate(self):
        """Activates the product"""
        self.active = True

    def deactivate(self):
        """Deactivates the product"""
        self.active = False

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self) -> str:
        """Shows a string for the product
        Promo added if True"""
        if self.promotion:
            promo_text = f"Promotion: {self.promotion.name}"
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity} {promo_text}"

        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """User can buy the product"""
        if quantity <= 0:
            raise ValueError("Negative quantity is unacceptable.")
        if not self.active:
            raise ValueError(f"{self.name} is not available at the moment")
        if quantity > self.quantity:
            raise ValueError(f"Stock is not enough, there are only {self.quantity} available")

        # Update the products quantity
        self.set_quantity(self.quantity - quantity)

        # Calculates price
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        total_price = self.price * quantity

        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        """ init super from parent class,
        setting quantity to 0 """
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """ Override to prevent any changes to quantity"""
        pass

    def buy(self, quantity):
        """ Non-stocked product, quantity does not affect purchase"""
        return self.price * quantity

    def show(self):
        """ Overriding the show method
        Added Promo text if True"""
        if self.promotion:
            promo_text = f"Promotion: {self.promotion.name}"
            return f"{self.name}, Price: {self.price} {promo_text}"
        return f"{self.name}, Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        """getting basic init from parent, adding maximum attribute
        in order to limit the purchases after"""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """basic buy from parent + limiting purchase capacity """
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} in a single order.")
        return super().buy(quantity)

    def show(self):
        """Overriding show method
        promo text added if True"""
        if self.promotion:
            promo_text = f"Promotion: {self.promotion.name}"
            return (f"{self.name}, Price: {self.price}, Max per order: {self.maximum}, "
                    f"Quantity: {self.quantity} "
                    f"{promo_text}")

        return f"{self.name}, Price: {self.price}, Max per order: {self.maximum}, Quantity: {self.quantity}"
