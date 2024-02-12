if __name__ == "__main__":
    class Car:
        def __init__(self, brand: str, model: str, year: int):
            """Инициализируем класс автомобиля с маркой, моделью и годом выпуска."""
            self.brand = brand
            self.model = model
            self.year = year

        def __str__(self) -> str:
            """Возвращает строковое представление автомобиля."""
            return f"{self.brand} {self.model} ({self.year})"

        def __repr__(self) -> str:
            """Возвращает подробное строковое представление автомобиля."""
            return f"Car(brand={self.brand}, model={self.model}, year={self.year})"


    class PassengerCar(Car):
        def __init__(self, brand: str, model: str, year: int, passengers: int):
            """
            Инициализируем класс легкового автомобиля с указанием марки, модели, года выпуска и количества пассажиров.


                :param brand: марка автомобиля.
                :param model: модель автомобиля.
                :param year: год выпуска автомобиля.
                :param passengers: количество возможных пассажиров.
            """
            super().__init__(brand, model, year)
            self.passengers = passengers

        def __str__(self) -> str:
            """Возвращает строковое представление легкового автомобиля."""
            return f"{super().__str__()} - {self.passengers} passengers"

        def __repr__(self) -> str:
            """Возвращает подробное строковое представление автомобиля."""
            return f"PassengerCar(brand={self.brand}, model={self.model}, year={self.year}, passengers={self.passengers})"

        def load_passengers(self, num_passengers: int) -> None:
            """
            Загружаем в автомобиль указанное количество пассажиров.


               :param num_passengers: число загружаемых пассажиров.
            """
            ...

        def _unload_passengers(self, num_passengers: int) -> None:
            """
           Выгружаем указанное количество пассажиров из автомобиля.


                :param num_passengers: число выгружаемых из автомобиля пассажиров.
            """

            ...
    pass
