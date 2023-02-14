import pandas as pd
import talib

# Carregue seus dados de preço de fechamento em um DataFrame do Pandas
df = pd.read_csv("preco_criptomoedas.csv")

# Calcule o RSI para cada criptomoeda
for symbol in df.columns:
    close = df[symbol]
    rsi = talib.RSI(close, timeperiod=14)
    
    # Verifique se o RSI está acima de 70 ou abaixo de 30
    if (rsi > 70).any():
        print(f"{symbol} está sobrecomprada")
    elif (rsi < 30).any():
        print(f"{symbol} está sobrevendida")
