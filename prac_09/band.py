class Band:
    """Band class"""
    def __init__(self, name=""):
        """Initialize a Band with a name and empty musicians collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of each musician playing their first instrument or indicating they need an instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)
