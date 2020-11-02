import json
import os

import requests

#Documentação:
#   Base: https://console.hgbrasil.com/documentation/finance
#   Lista de Símbolos: https://console.hgbrasil.com/documentation/finance/symbols

url = "https://api.hgbrasil.com/finance/stock_price"
valid_key = "" #Acesse o site do HG Brasil para obter sua chave

for item in open("HGFinance-Lista.txt"):
    ticker = item.replace('\n', '')
    parametros = {"key":valid_key,"symbol":ticker}
    response = requests.get(url, params=parametros)
    content = json.loads(response.content)
    results = content['results'][ticker]
    atualizacao = results["updated_at"][0:10]

    print(f"A cotação atual de {results['symbol']} é {results['price']}, a variação em relação ao dia anterior é {results['change_percent']}")
    
    with open(os.path.join('json', f'{ticker}.json'), 'w') as file:
        json.dump(results, file)
