from abc import ABC, abstractmethod
from math import sqrt, sin, pow


class Function(ABC):
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, float):
            raise ValueError('Value is not a number')
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, float):
            raise ValueError('Value is not a number')
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if not isinstance(value, float):
            raise ValueError('Value is not a number')
        self._z = value

    @abstractmethod
    def calculate(self) -> int:
        pass


class FirstFunction(Function):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate(self) -> int:
        return 7 * pow(self.x, 4) + sqrt(3 * self.y * self.x)


class SecondFunction(Function):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def calculate(self) -> int:
        return sin(self.x) + 3 * pow(self.z, self.y) - self.y * self.z


print('Мойсол Андрiй Олексiйович, IП-96, 14 варiант')

while True:
    try:
        t = int(input('Enter an action(0 - exit, 1 - first function, 2 - second function): '))
        if t == 0:
            break
        if t == 1:
            x = float(input('Enter x: '))
            y = float(input('Enter y: '))
            func: Function = FirstFunction(x, y)
            print(f'Result: {func.calculate()}')
        if t == 2:
            x = float(input('Enter x: '))
            y = float(input('Enter y: '))
            z = float(input('Enter z: '))
            func: Function = SecondFunction(x, y, z)
            print(f'Result: {func.calculate()}')
    except ValueError:
        print('Error occurred, try again:')
        continue

