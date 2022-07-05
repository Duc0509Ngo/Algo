from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    color_hair: str
    age: int


p1 = Person(name='Duc', color_hair='short hair', age=19)

print(p1.name)




   