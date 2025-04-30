from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if not self.name:
            raise ValueError("Name cannot be empty")
    
p1 = Person(name="Alice", age=30)
p2 = Person(name="Bob", age=25)
print(p1)
print(p2)