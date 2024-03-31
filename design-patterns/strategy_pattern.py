"""
Strategy Pattern is a behavioral design pattern that enables selecting an algorithm at runtime.
The main idea of strategy pattern is to extract related algorithms into separate classes and define a common interface for them.

Let's consider of system that calculated shipping cost for orders on e-commerce website.
"""

from abc import ABC, abstractmethod

"""
Example without using Strategy Pattern
Without using the Strategy pattern, you might find yourself writing a monolithic shipping cost calculator, 
stuffed with conditionals (if, else if, else) to handle the myriad of combinations of these factors. 
This approach quickly becomes hard to manage, error-prone, and a nightmare to test and extend. 
For instance, adding a new shipping method would require modifying the existing code, increasing the risk of introducing bugs.
"""

class ShippingCostCalculator:
    def calculate_shipping_cost(self, order, carrier, delivery_speed):
        if carrier == "UPS":
            if delivery_speed == "standard":
                # Complex logic for UPS standard
                return 20
            elif delivery_speed == "express":
                # Complex logic for UPS express
                return 40
        elif carrier == "FedEx":
            # Similar branching for FedEx...
            pass
        # And so on for other carriers and conditions

"""
Above approach has several drawbacks, primarily due to its inflexibility and the high cost of maintenance.
Introducing a new carrier or changing the pricing strategy would require modifying the ShippingCostCalculator class, violating the Open/Closed Principle.
"""

class ShippingStrategy:
    def calculate(self, order) -> float:
        pass

class UPSShippingStrategy(ShippingStrategy):
    def calculate(self, order) -> float:
        # Logic for calculating UPS shipping cost
        return 20  # Simplified for example purposes

class FedExShippingStrategy(ShippingStrategy):
    def calculate(self, order) -> float:
        # Logic for calculating FedEx shipping cost
        return 25  # Simplified for example purposes

class ShippingCost:
    def __init__(self, strategy: ShippingStrategy):
        self._strategy = strategy

    def calculate(self, order) -> float:
        return self._strategy.calculate(order)

def main():
    order = {"weight": 5, "destination": "New York"}

    # Client code can dynamically choose the strategy at runtime
    ups = ShippingCost(UPSShippingStrategy())
    print("UPS Shipping Cost:", ups.calculate(order))

    fedex = ShippingCost(FedExShippingStrategy())
    print("FedEx Shipping Cost:", fedex.calculate(order))
