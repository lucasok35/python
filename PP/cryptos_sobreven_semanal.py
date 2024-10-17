import os
import requests

# Defina o caminho do arquivo de texto
caminho_arquivo = 'C:\\Users\\lucas\\Desktop\\resultado.txt'

# Defina a URL da API CoinGecko para obter os dados das criptomoedas
api_url = "https://api.coingecko.com/api/v3/coins/markets"

# Parâmetros da solicitação
params = {
    "vs_currency": "usd",  # Moeda de comparação (USD no exemplo)
    "order": "volume_desc",  # Ordenar por volume decrescente
    "per_page": 100,  # Número de criptomoedas retornadas por página
    "page": 1  # Número da página (1 no exemplo)
}

# Faça uma solicitação GET para a API CoinGecko e obtenha os dados das criptomoedas
response = requests.get(api_url, params=params)
data = response.json()

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Acesse os dados necessários, como a lista de criptomoedas e seus valores
    cryptos = data
    
    # Filtra as criptomoedas com base no intervalo de tempo desejado (semanal)
    cryptos_weekly = [crypto for crypto in cryptos if "price_change_percentage_7d" in crypto]
    
    # Filtra as criptomoedas com base no RSI (por exemplo, com RSI menor que 30 considerado sobrevendido)
    oversold_cryptos = [crypto for crypto in cryptos_weekly if crypto["rsi"] < 30]
    
    # Ordene as criptomoedas com base no volume
    sorted_cryptos = sorted(oversold_cryptos, key=lambda x: x["total_volume"], reverse=True)
    
    # Obtenha as dez principais criptomoedas com maior volume e RSI sobrevendido
    top_10_cryptos = sorted_cryptos[:10]
    
    # Salve o resultado em um arquivo de texto
    with open(caminho_arquivo, 'w') as arquivo:
        for crypto in top_10_cryptos:
            linha = f"Nome da criptomoeda: {crypto['name']}\n"
            linha += f"Volume de negociação: {crypto['total_volume']}\n"
            linha += f"RSI: {crypto['rsi']}\n"
            linha += "---\n"
            arquivo.write(linha)
    
    print(f"O resultado foi salvo em: {caminho_arquivo}")
else:
    print("Falha na solicitação da API CoinGecko")
