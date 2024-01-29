class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):  # проверяем что значение является строкой
            self._name = value
        else:
            raise ValueError("name should be a string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self._author = value
        else:
            raise ValueError("author should be a string")



    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages




    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int):
            self._pages = value

        else:

            raise ValueError("pages должен быть целым числом")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"
class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, float):
            self._duration = value

        else:

           raise ValueError("duration должен быть числом")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

print(AudioBook("Капитанская дочка", "Пушкин", 54.6 ))
print(PaperBook("Капитанская дочка", "Пушкин", 100))
print(Book("Капитанская дочка", "Пушкин"))