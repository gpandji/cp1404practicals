from car import Car
import random


class UnreliableCar(Car):
    """An unreliable version of a Car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance if it is reliable enough."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
