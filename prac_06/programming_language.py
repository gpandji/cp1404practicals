"""
programming language
Estimate: 30 minutes
Actual:   43 minutes
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed and False otherwise."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing}, {self.reflection}, {self.year}"