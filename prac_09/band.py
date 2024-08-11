class Band:
    """Represent a Band, which is a collection of musicians."""

    def __init__(self, name):
        """Initialise a Band instance."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of the Band."""
        return "{} ({})".format(self.name, ", ".join(str(member) for member in self.members))

    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def play(self):
        """Make the band play their instruments."""
        for member in self.members:
            print(member.play())