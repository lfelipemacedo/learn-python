from typing import Union
import requests
from fastapi import FastAPI
from fastapi.params import Query

app = FastAPI()


@app.get('/api/restaurantes')
def get_cardapio(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardapios de um restaurante
    :param restaurante: str
    :return: Uma lista de cardapios
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}
