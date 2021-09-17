"""
CP1404/CP5632 Practical - Guitar class
"""
CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:
    """Store details of a guitar using the Guitar class."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display the Guitar in a string."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Sort Guitar by year."""
        return self.year < other.year
