import ccxt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Função para obter dados históricos de candlestick
def get_candlestick_data(symbol, timeframe='5m', limit=1000):
    exchange = ccxt.binance()
    data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    
    # Convertendo para DataFrame do Pandas
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    return df

# Função para processar os dados de candlestick
def process_candlestick_data(df, window_size=10):
    scaler = MinMaxScaler()
    
    # Normalizando os dados de preços (open, high, low, close)
    df[['open', 'high', 'low', 'close']] = scaler.fit_transform(df[['open', 'high', 'low', 'close']])
    
    # Gerando janelas de dados para input na rede neural
    X, y = [], []
    for i in range(window_size, len(df)):
        X.append(df[['open', 'high', 'low', 'close']].iloc[i-window_size:i].values)
        y.append(df['close'].iloc[i])  # Usando o preço de fechamento como alvo
        
    X, y = np.array(X), np.array(y)
    
    return X, y, scaler
