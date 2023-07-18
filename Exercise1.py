from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save(self, name, data):
        raise NotImplementedError("The method has not been implemented.")

    @abstractmethod
    def load(self, name):
        raise NotImplementedError("The method has not been implemented.")

    @abstractmethod
    def delete(self, name):
        raise NotImplementedError("The method has not been implemented.")


class FileStorage(Storage):
    def __init__(self):
        pass

    def save(self, name, data):
        with open(name, 'w') as file:
            file.write(data)

    def load(self, name):
        with open(name, 'r') as file:
            return file.read()

    def delete(self, name):
        import os
        os.remove(name)


class DataStorage(Storage):
    def __init__(self):
        pass

    def save(self, name, data):
        print(f"{data} has been saved in {name}.")

    def load(self, name):
        print(f"Loading data  from {name}.")

    def delete(self, name):
        print(f"The {name} has been deleted")


try:
    txt = FileStorage()
    txt.save("python.txt", "Hello Pyhton")
    print(txt.load("python.txt"))
    txt.delete('python.txt')
except NotImplementedError as nie:
    print(str(nie))
except FileNotFoundError as fnf:
    print(str(fnf))
except TypeError as te:
    print(str(te))
