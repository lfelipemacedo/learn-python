from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_pizzaria = Restaurante('Pizza Planet', 'Pizzaria')
suco = Bebida('Suco de Uva', 5.0, 'Grande')
bife_com_batata = Prato('Bife com Batata Frita', 20.0, 'O melhor do Rio!')

suco.aplicar_desconto()
bife_com_batata.aplicar_desconto()

restaurante_pizzaria.adicionar_item_no_cardapio(bife_com_batata)
restaurante_pizzaria.adicionar_item_no_cardapio(suco)

restaurante_pizzaria.exibir_cardapio

print(restaurante_pizzaria)
print(suco)
print(bife_com_batata)