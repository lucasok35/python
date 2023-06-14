import talib
import requests

# Defina sua chave de API do CoinMarketCap aqui
api_key = '0eff6948-6af0-44a4-83e1-8282cc945d06'

# Defina o limite RSI para sobrevenda aqui
rsi_limit = 30

# Defina o período de tempo para buscar (1h neste exemplo)
timeframe = '5m'

# Defina o número de criptomoedas a serem exibidas
limit = 10

# Use a API do CoinMarketCap para obter a lista de criptomoedas
url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY={api_key}&limit={limit}'
response = requests.get(url)
data = response.json()

# Crie uma lista para armazenar as criptomoedas em sobrevenda
oversold_coins = []

# Percorra cada criptomoeda e calcule o RSI
for coin in data['data']:
    symbol = coin['symbol']
    name = coin['name']
    price = coin['quote']['USD']['price']
    volume = coin['quote']['USD']['volume_24h']

    # Use a API do CoinMarketCap para obter o histórico de preços da criptomoeda
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical?CMC_PRO_API_KEY={api_key}&symbol={symbol}&time_start=2022-01-01&time_end=now&interval={timeframe}'
    response = requests.get(url)
    data = response.json()

    print(data,'\n')

    # Extraia os preços de fechamento e calcule o RSI
    closes = [x['quote']['USD']['close'] for x in str(data['data'])]
    rsi = talib.RSI(closes)

    # Verifique se o RSI está abaixo do limite de sobrevenda
    if rsi[-1] < rsi_limit:
        oversold_coins.append((name, symbol, price, volume, rsi[-1]))

# Exiba a lista de criptomoedas em sobrevenda
print(f"Lista de criptomoedas em sobrevenda ({timeframe} período):")
for coin in oversold_coins:
    print(f"{coin[0]} ({coin[1]}) - Preço: ${coin[2]:,.2f}, Volume 24h: ${coin[3]:,.2f}, RSI: {coin[4]:.2f}")
