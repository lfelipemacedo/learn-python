from modelos.restaurante import Restaurante

pizza_planet = Restaurante('Pizza Planet', 'Pizzaria')
java_flash = Restaurante('Japa Flash', 'Japonesa')

java_flash.ativar()
java_flash.avaliar('Felipe', 10)
java_flash.avaliar('Amanda', 7)
java_flash.avaliar('Luis', 5)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
