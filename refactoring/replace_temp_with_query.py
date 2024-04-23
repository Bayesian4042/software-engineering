# Problem
# You place the result of an expression in a local variable for later use in your code.

def calculate_total():
    base_price = quantity * item_price
    if base_price > 1000:
        return base_price * 0.95
    else:
        return base_price

# Solution
# Move the entire expression to a separate method and return the result from it. Query the method instead of using a variable. Incorporate the new method in other methods, if necessary.

def calculate_total():
    if base_price() > 1000:
        return base_price() * 0.95
    else:
        return base_price()

def base_price():
    return quantity * item_price

# the resulting code may be burdened by querying a new method. But with today’s fast CPUs and excellent compilers, the burden will almost always be minimal. By contrast, readable code and the ability to reuse this method in other places in program code—thanks to this refactoring approach—are very noticeable benefits.
# Nonetheless, if your temp variable is used to cache the result of a truly time-consuming expression, you may want to stop this refactoring after extracting the expression to a new method.