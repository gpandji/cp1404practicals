"""
Guitar class
Estimated : 30 minutes
Actual : 40 minutes
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        return f"in 2024 the {self.name} is {2024 - self.year}"

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return 2024 - self.year >= 50

    def __lt__(self, other):
        """Less than, used for sorting Guitars by year."""
        return self.year < other.year
