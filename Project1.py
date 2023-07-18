class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer
        if isinstance(total, int):
            self._total = total
        else:
            raise TypeError("Total must be integer")
        if isinstance(allocated, int):
            self._allocated = allocated
        else:
            raise TypeError("Allocated must be integer")

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"Resource(name = {self._name}, manufacturer = {self._manufacturer}, " \
               f"total={self._total}, allocated={self._allocated})"

    def claim(self, m):
        if isinstance(m, int):
            if self._total - self._allocated >= m:
                self._allocated += m
            else:
                self._allocated = self._total
        else:
            raise TypeError("m must be integer")

    def freeup(self, n):
        if isinstance(n, int):
            if self._allocated >= n:
                self._allocated -= n
            else:
                self._allocated = 0
        else:
            raise TypeError("n must be integer")

    def died(self, n):
        if isinstance(n, int):
            if self._total >= n:
                self._total -= n
                if self._allocated >= n:
                    self._allocated -= n
                else:
                    self._allocated = 0
            else:
                self._total = 0
        else:
            raise TypeError("n must be integer")

    def purchased(self, n):
        if isinstance(n, int):
            self._total += n
        else:
            raise TypeError("n must be integer")

    def category(self):
        return self.__class__.__name__.lower()


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_wats):
        super().__init__(name, manufacturer, total, allocated)
        if isinstance(cores, int):
            self._cores = cores
        else:
            raise TypeError("Cores must be integer")
        self._socket = socket
        if isinstance(power_wats, int):
            self._power_wats = power_wats
        else:
            raise TypeError("Power  wats must be integer")

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_wats(self):
        return self._power_wats

    def __repr__(self):
        return f"{self.__class__.__name__}: {self._name}, {self._manufacturer}, {self._total}," \
               f" {self._allocated}, {self._cores}, {self._socket}, {self._power_wats}"


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name, manufacturer, total, allocated)
        if isinstance(capacity_GB, int):
            self._capacity_GB = capacity_GB
        else:
            raise TypeError("Capacity must be integer")

    @property
    def capacity_GB(self):
        return self._capacity_GB

    def __repr__(self):
        return f"{self.__class__.__name__}: {self._name}, {self._manufacturer}, {self._total}, " \
               f"{self._allocated}, {self._capacity_GB}"


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        if isinstance(size, int):
            self._size = size
        else:
            raise TypeError("Size must be integer")
        if isinstance(rpm, int):
            self._rpm = rpm
        else:
            raise TypeError("Rpm must be integer")

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        return f"{self.__class__.__name__}: {self._name}, {self._manufacturer}, {self._total}," \
               f" {self._allocated}, {self._capacity_GB}, {self._size}, {self._rpm}"


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._interface = interface

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        return f"{self.__class__.__name__}: {self._name}, {self._manufacturer}, {self._total}," \
               f" {self._allocated}, {self._capacity_GB}, {self._interface}"


