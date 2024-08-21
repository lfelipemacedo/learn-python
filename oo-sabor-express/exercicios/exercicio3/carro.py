from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas) -> None:
        super().__init__(marca, modelo)
        self._portas = portas
    
    def __str__(self) -> str:
        return f'{super().__str__()} | {self._portas}'