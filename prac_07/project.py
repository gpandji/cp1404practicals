from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a string representation of the project."""
        return (
            f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f},"
            f" completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less than, used for sorting projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is complete."""
        return self.completion_percentage == 100

    def update_priority(self, new_priority):
        """Update the project priority."""
        self.priority = new_priority

    def update_completion_percentage(self, new_completion_percentage):
        """Update the project completion percentage."""
        self.completion_percentage = new_completion_percentage