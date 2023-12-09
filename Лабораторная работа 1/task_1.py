from abc import ABC, abstractmethod


class AbstractPhysicalObject(ABC):

    def __init__(self, material: str, weight: float) -> None:
        self.material = material
        self.weight = weight

    def move(self, new_location: str) -> None:
        pass

    def break_into_pieces(self) -> None:
        pass

class AbstractLivingBeing(ABC):

    def __init__(self, species: str, habitat: str) -> None:
        self.species = species
        self.habitat = habitat

    def eat(self, food: str) -> None:
        pass

    def reproduce(self) -> None:
        pass


class AbstractConcept(ABC):

    def __init__(self, name: str, category: str) -> None:
        self.name = name
        self.category = category

    def manipulate(self, action: str) -> None:
        pass

    def analyze(self) -> str:
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()