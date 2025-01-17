import pytest
from products import Product


def test_empty_name():
    with pytest.raises(ValueError, match = "Name cannot be empty."):
        Product("", price=1450, quantity=100)

def test_negative_price():
    with pytest.raises(ValueError, match = "Price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)

def test_product_works():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.active == True
    assert product.get_quantity() == 100
    assert product.is_active() == True
    assert product.show() == "MacBook Air M2, Price: 1450, Quantity: 100"
    assert product.buy(2) == 2900

def test_product_deactivate():
    product = Product("MacBook Air M2", price=1450, quantity=0)
    assert product.deactivate() == None
    assert product.active == False
    assert product.is_active() == False

def test_quantity_after_purchase():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.buy(10) == 14500
    assert product.get_quantity() == 90

def test_large_purchase():
    with pytest.raises(ValueError, match = "Not enough quantity."):
        product = Product("tv", price=1000, quantity=100)
        product.buy(1000)
