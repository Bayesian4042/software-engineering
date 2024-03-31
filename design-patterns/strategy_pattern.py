"""
Strategy Pattern is a behavioral design pattern that enables selecting an algorithm at runtime.
The main idea of strategy pattern is to extract related algorithms into separate classes and define a common interface for them.
"""

from abc import ABC, abstractmethod

class TravelStrategy(ABC):
    @abstractmethod
    def calculate_time(self, distance: float) -> float:
        pass

class CarStrategy(TravelStrategy):
    def calculate_time(self, distance: float) -> float:
        # Assuming average speed is 60 km/h
        return distance / 60

class BikeStrategy(TravelStrategy):
    def calculate_time(self, distance: float) -> float:
        # Assuming average speed is 15 km/h
        return distance / 15

class WalkStrategy(TravelStrategy):
    def calculate_time(self, distance: float) -> float:
        # Assuming average speed is 5 km/h
        return distance / 5


class TravelPlanner:
    def __init__(self, strategy: TravelStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: TravelStrategy):
        self._strategy = strategy

    def calculate_travel_time(self, distance: float) -> float:
        return self._strategy.calculate_time(distance)


def main():
    distance = 120  # Distance in kilometers

    planner = TravelPlanner(CarStrategy())
    print(f"Travel time by car: {planner.calculate_travel_time(distance)} hours")

    planner.set_strategy(BikeStrategy())
    print(f"Travel time by bike: {planner.calculate_travel_time(distance)} hours")

    planner.set_strategy(WalkStrategy())
    print(f"Travel time by walking: {planner.calculate_travel_time(distance)} hours")

if __name__ == "__main__":
    main()

