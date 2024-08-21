from modelos.avaliacao import Avaliacao


class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Ativo".ljust(25)} | {"Avaliação".ljust(25)}')
        for restaurante in cls.restaurantes:
            print(
                f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {str(restaurante.media_avaliacao()).ljust(25)}')

    def ativar(self):
        self._ativo = True

    def avaliar(self, cliente, nota):
        if nota > 5:
            self._avaliacoes.append(Avaliacao(cliente, nota))

    def media_avaliacao(self):
        if not self._avaliacoes:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        return round(soma_notas / len(self._avaliacoes), 1)
