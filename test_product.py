import pytest  # pytest library import
from products import Product  # Importing the Product class


def test_create_normal_product():
    """Test that creating a normal product works."""

    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True


def test_create_product_with_invalid_details():
    """Test that creating a product with invalid details
    (empty name, negative price) raises an Exception."""

    with pytest.raises(ValueError):  # Empty name
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError):  # Negative price
        Product("MacBook Air M2", price=-10, quantity=100)

    with pytest.raises(ValueError):  # Negative quantity
        Product("MacBook Air M2", price=1450, quantity=-5)


def test_product_becomes_inactive_when_quantity_zero():
    """Test that when a product reaches 0 quantity, it becomes inactive."""

    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.is_active() is False


def test_product_purchase_updates_quantity():
    """Test that product purchase modifies the quantity and returns the right output."""

    product = Product("MacBook Air M2", price=1450, quantity=10)
    total_price = product.buy(2)
    assert total_price == 1450 * 2
    assert product.quantity == 8


def test_buying_more_than_available_quantity_raises_exception():
    """Test that buying a larger quantity than exists raises an Exception."""

    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(ValueError):
        product.buy(6)
