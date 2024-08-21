class Restaurant:
    def __init__(self, name: str, category: str) -> None:
        self._name = name
        self._category = category
        self._active = False
        
    def __str__(self) -> str:
        return f'{self._name} | {self._category}'