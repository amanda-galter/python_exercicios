import json
import urllib.request

#solicitar ao usuário o CEP
cep=input('digite o CEP: ')

#construir um URL para consulta
url=f"https://viacep.com.br/ws/{cep}/json/"

try:
    #fazer a requisição
    response=urllib.request.urlopen(url)

    #Ler o conteudo da resposta
    data = response.read().decode('utf-8')

    #teste...
    print(data)
except Exception as e:
    print(f"erro: {e}")