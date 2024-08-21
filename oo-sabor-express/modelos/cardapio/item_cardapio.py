from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco) -> None:
        self._nome = nome
        self._preco = preco
    
    def __str__(self) -> str:
        return f'{self._nome} | {self._preco}'
    
    @abstractmethod
    def aplicar_desconto(self):
        pass