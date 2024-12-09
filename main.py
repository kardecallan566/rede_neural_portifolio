import numpy as np
import tensorflow as tf
from data.data_loader import get_candlestick_data, process_candlestick_data
from model.rl_model import build_model, train_model, evaluate_model
from portfolio.portfolio_manager import PortfolioManager
from trading.trader import Trader
import config.settings as settings

# Passo 1: Carregar e processar dados
symbol = 'BTC/USDT'
df = get_candlestick_data(symbol)
X, y, scaler = process_candlestick_data(df)

# Passo 2: Criar e treinar o modelo
model = build_model((X.shape[1], X.shape[2]))
train_model(model, X, y, epochs=settings.EPOCHS)

# Passo 3: Gerenciar o portfólio
portfolio = PortfolioManager()

# Passo 4: Executar trades (exemplo)
trader = Trader(settings.API_KEY, settings.API_SECRET)
portfolio.buy(symbol, 5, 100)  # Exemplo de compra
print(f"Saldo após compra: {portfolio.get_balance()}")

# Passo 5: Avaliar o modelo (Exemplo)
X_test, y_test = X[-200:], y[-200:]  # Usar dados de teste
loss = evaluate_model(model, X_test, y_test)
print(f"Loss no conjunto de teste: {loss}")
