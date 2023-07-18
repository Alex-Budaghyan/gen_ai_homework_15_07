class Vehicle:
    def __init__(self, model, year, weight):
        self._model = model
        self._year = year
        self._weight = weight

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def weight(self):
        return self._weight

    def new(self):
        if self._year > 2000:
            print("New Vehicle")
        else:
            print("Old Vehicle")


class Car(Vehicle):
    def __init__(self, model, year, weight, engine_power):
        super.__init__(model, year, weight)
        self._engine_power = engine_power

    @property
    def engine_power(self):
        return self._engine_power

    def new(self):
        if self._year > 2018:
            print("New car")
        else:
            print("Old car")


class Bicycle(Vehicle):
    def __init__(self, model, year, weight, brand):
        super().__init__(model, year, weight, brand)
        self._brand = brand

    @property
    def brand(self):
        return self._brand

    def new(self):
        if self._year > 2020:
            print("New Bicycle")
        else:
            print("Old Bicycle")


class Motorcycles(Bicycle):
    def __init__(self, model, year, weight, brand, max_speed):
        super().__init__(model, year, weight, brand, max_speed)
        self._max_speed = max_speed

    @property
    def max_speed(self):
        return self._max_speed

    def new(self):
        if self._year > 2022:
            print("New Motorcycles")
        else:
            print("Old Motorcycles")