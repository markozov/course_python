from abc import ABC, abstractmethod


class AbstractPhysicalObject(ABC):

    def __init__(self, material: str, weight: float) -> None:
        '''
        Инициализация экземпляра класса.
        :param material: материал физического объетка
        :param weight: вес объекта

        Example
        >>> window = AbstractPhysicalObject("Стекло", 35.0)
        '''
        self.material = material
        if weight < 0:
            raise ValueError("Вес не может быть отрицательным числом")
        self.weight = weight
    @abstractmethod
    def move(self, new_location: str) -> None:
        '''
        Присвоение физическому объекту места расположения.
        :param new_location: место или локация в которой находится физический объект

        Example:
        >>> window = AbstractPhysicalObject("Стекло", 35.0)
        >>> window.move("Оконная рама")
        '''
        ...

    @abstractmethod
    def weight_change(self, added_weight: float, deleted_weight: float) -> None:
        '''
        Добавление либо убавление веса объекта.
        :param added_weight: число на которое мы изменяем вес объекта
        :raise ValueError: если вес который мы убавляем больше, чем исходный вес объекта, то возвращается ошибка.
         Если вес который мы прибавляем отрицательный, то возвращается ошибка.

         :return: Действительный вес объекта.

         Example:
         >>> pipe = AbstractPhysicalObject("Сталь", 100.0)
         >>> pipe.weight_change(0.0, 50.0)
        '''
        ...

class AbstractLivingBeing(ABC):

    def __init__(self, species: str, habitat: str) -> None:
        '''
        Инициализация экземпляра класса.
        :param species: вид живого существа
        :param habitat: среда обитания

        Example
        >>> gorilla = AbstractLivingBeing("Горилла", "Горная местность")
        '''
        self.species = species
        self.habitat = habitat

    @abstractmethod
    def eat(self, food: str) -> None:
        '''
        Добавление еды, входящей в рацион живого существа.
        :param food: наименование продукта питания

        Example:
        >>> gorilla = AbstractLivingBeing("Горилла", "Горная местность")
        >>> gorilla.eat("Побеги бамбука")
        '''
        ...

    @abstractmethod
    def number_of_individuals(self, number: float) -> None:
        '''
        Добавление числа особей.
        :param number: число особей
        :raise ValueError: Если число особей является отрицательным числом, то возвращается ошибка.

        Example:
        >>> gorilla = AbstractLivingBeing("Горилла", "Горная местность")
        >>> gorilla.number_of_individuals(500.0)
        '''
        ...



class AbstractConcept(ABC):

    def __init__(self, name: str, category: str) -> None:
        '''
        Инициализация экземпляра класса.
        :param name: наименование понятия
        :param category: к какой категории относится понятие

        Example:
        >>> solfeggio = AbstractConcept("Сольфеджио", "Учебная дисциплина")
        '''
        self.name = name
        self.category = category

    @abstractmethod
    def hours_per_week(self, hours: float) -> None:
        '''
        Количество часов в неделю, уделяемое дисциплине.
        :param hours: количество часов
        :raise ValueError: если количество часов отрицательное число, то возвращается ошибка.

        Example:
        >>> solfeggio = AbstractConcept("Сольфеджио", "Учебная дисциплина")
        >>> solfeggio.hours_per_week(3.0)
        '''
        ...

    @abstractmethod
    def certification(self, estimation: str) -> str:
        '''
        Оценка итоговой аттестации по дисциплине.
        :param estimation: Полученная оценка.

        Example:
        >>> solfeggio = AbstractConcept("Сольфеджио", "Учебная дисциплина")
        >>> solfeggio.certification("Отлично")
        '''
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
