from pydantic import BaseModel


class Person(BaseModel):
    """Person model equivalent to the Java Person class."""
    name: str

    def __str__(self) -> str:
        return self.name
