# problem

class PizzaDelivery:
    def get_rating():
        return 2 if more_than_five_late_deliveries() else 1

    def more_than_five_late_deliveries():
        return number_of_late_deliveries > 5


# solution
class PizzaDelivery:
    def get_rating():
        return 2 if number_of_late_deliveries > 5 else 1