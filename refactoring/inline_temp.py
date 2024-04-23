# Problem
# You have a temp variable that assigned the result of simple expression

def has_discount(order):
    base_price = order.base_price()
    return base_price > 1000

# Solution
# Replace the reference to the variable with expression itself

def has_discount(order):
    return order.base_price() > 1000
