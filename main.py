from abc import ABC, abstractmethod


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Person(name={self.name})"


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


class PersonDB(PersonStorage):
    def save(self, person: Person):
        print(f"Save the {person} to the database")


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f"Save the {person} to a JSON file")


class PersonXML(PersonStorage):
    def save(self, person):
        print(f"Save the {person} to a XML file")


if __name__ == "__main__":
    p = Person("John Doe")
    db = PersonXML()
    db.save(p)
