class Metaclass(type):
    def __new__(cls, name, bases, attr):
        for key, value in attr.items():
            if isinstance(value, type):
                attr[key] = Metaclass.create_property(key, value)
        return super().__new__(cls, name, bases, attr)

    @staticmethod
    def create_property(name, e_type):
        pr_name = f"_{name}"

        def getter(self):
            return getattr(self, pr_name)

        def setter(self, value):
            if not isinstance(value, e_type):
                raise TypeError(f"Expected {e_type.__name__} for  {name},but given {type(value).__name__}")
            setattr(self, pr_name, value)

        return property(getter, setter)


class MyClass(metaclass=Metaclass):
    name = str
    year = int
    weight = float


obj = MyClass()
obj.name = 2
obj.year = "Bob"
obj.weight = 58.56
