import cart
import products
from cart import get_cart
import os

def checkout(username):
    cart = get_cart(username)
    total = 0
    for item in cart:
       total += item.cost
    return total


def complete_checkout(username):
    cartv = cart.get_cart(username)
    items = cartv
    for item in items:
        assert item.qty >= 1
    for item in items:
        cart.delete_cart(username)
        products.update_qty(item.id, item.qty-1)
        


