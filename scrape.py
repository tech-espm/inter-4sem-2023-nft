import requests
from safeData import url, apiKey
import datetime

ranking = 0
data = []
date = datetime.datetime.now().strftime('%Y-%m-%d')


def scrape(continuation = '', index = 0):
    base = url + continuation
    headers = {
        "accept": "*/*",
        "x-api-key": apiKey
    }

    response = requests.get(base, headers=headers).json()

    collections = response['collections']

    for collection in collections:
        #Craindo local na lista e dicionário para popular
        data.append([])
        data[index] = {
            'rank': collection['rank']['1day'],
            'name': collection['name'],
            'image': collection['image'],
            'volume': collection['volume']['1day'],
            'volumeChange': collection['volumeChange']['1day'],
            'tokenCount': collection['tokenCount'],
            'onSaleCount': collection['onSaleCount'],
            'floorSale': collection['floorSale']['1day'],
            'ownerCount': collection['ownerCount'],
            'date': date
        }
        ranking = collection['rank']['1day']
        index += 1

    if response['continuation'] != None and ranking < 100:
        continuation = f'&continuation={response["continuation"]}'
        scrape(continuation, index)

    if len(data) == 0:
        raise ValueError('Não foi possível obter os dados da API')
    return data
