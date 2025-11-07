"""
06 – Getters / Setters : Temperature et Position avec validation
"""


class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = 0.0
        self.celsius = celsius  # utilise setter

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, valeur: float) -> None:
        if valeur < -273.15:
            raise ValueError("En dessous du zéro absolu !")
        self._celsius = valeur

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

    def __str__(self) -> str:
        return f"{self._celsius:.2f}°C / {self.fahrenheit:.2f}°F"


class Position:
    def __init__(self, x: int, y: int) -> None:
        self._x = 0
        self._y = 0
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        if value < 0:
            raise ValueError("x négatif")
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        if value < 0:
            raise ValueError("y négatif")
        self._y = value

    def __repr__(self) -> str:
        return f"Position(x={self._x}, y={self._y})"


if __name__ == "__main__":
    t = Temperature(20)
    print(t)
    p = Position(3, 5)
    print(p)
