class Veiculo:
    def __init__(self, marca, modelo) -> None:
        self._marca = marca
        self._modelo = modelo
    
    def __str__(self) -> str:
        return f'{self._marca} | {self._modelo}'