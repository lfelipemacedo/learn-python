class Car:
    def __init__(self, type: str, color: str, year: int) -> None:
        self._type = type
        self._color = color
        self._year = year
    
    def __str__(self) -> str:
        return f'{self._type} | {self._color} | {self._year}'