from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Animal(ABC):
    name: str
    hobbies: str
    age: int

    @abstractmethod
    def get_info_pet(self):
        pass


@dataclass
class Dog(Animal):
    @property
    def get_info_pet(self):
        return """
        Dog 
        Name: {} - Age: {} - Hobbies: {}
        """.format(
            self.name, self.age, self.hobbies
        )


@dataclass
class Cat(Animal):
    @property
    def get_info_pet(self):
        return """
        Cat
        Name: {} - Age: {} - Hobbies: {}
        """.format(
            self.name, self.age, self.hobbies
        )


dog = Dog(name="Milo", age=19, hobbies="Play with balls")
cat = Cat(name="Louis", age=21, hobbies="Play with sand")
print(getattr(cat, "name"))
print(dog.get_info_pet)
print(cat.get_info_pet)
