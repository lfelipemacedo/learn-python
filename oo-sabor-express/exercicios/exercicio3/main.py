from veiculo import Veiculo
from carro import Carro
from moto import Moto

def main():
    moto = Moto("Royal Enfield", "Cruiser", "Casual")
    carro = Carro("Chevrolet", "Fusca", 2)
    
    print(moto.__str__())
    print(carro.__str__())

if __name__ == '__main__':
    main()