from models import Person


class PersonDatabase:
    """
    In-memory database for Person objects.
    Equivalent to the Java PersonDatabase singleton class.
    """

    def __init__(self):
        self.persons: list[Person] = []
        self._init_data()

    def _init_data(self):
        """Initialize the database with sample data (Big Bang Theory characters)."""
        self.persons = [
            Person(name="Penny"),
            Person(name="Leonard"),
            Person(name="Sheldon"),
            Person(name="Amy"),
            Person(name="Howard"),
            Person(name="Bernadette"),
            Person(name="Raj"),
            Person(name="Priya"),
        ]

    def current_list(self) -> list[Person]:
        """Return all persons in the database."""
        return self.persons

    def get_person(self, person_id: int) -> Person | None:
        """
        Get a person by their ID (index).
        Returns None if the ID is out of range.
        """
        if 0 <= person_id < len(self.persons):
            return self.persons[person_id]
        return None


# Singleton instance
person_database = PersonDatabase()
