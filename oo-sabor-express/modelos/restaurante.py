class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
restaurante_praca = Restaurante("Gula Lele", "Lanchonete")

print(vars(restaurante_praca))