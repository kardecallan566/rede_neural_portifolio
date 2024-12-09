from binance_connector import BinanceConnector
from portfolio_manager import PortfolioManager
from reinforcement_learning import ReinforcementLearningModel
import time

# Inicialização
api_key = 'your_api_key'
secret_key = 'your_secret_key'
connector = BinanceConnector(api_key, secret_key)
portfolio = PortfolioManager()
rl_model = ReinforcementLearningModel(state_size=10, action_size=5)

def run_bot():
    # Primeira rodada: Seleção de pares
    pairs = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT']
    selected_pair = rl_model.predict(pairs)  # Pode ser uma seleção baseada na rede neural
    
    # Compra inicial
    buy_price = connector.get_data(selected_pair)[-1][4]  # Fechamento mais recente
    amount_to_buy = 5  # Comprar 5 unidades do par selecionado
    connector.buy(selected_pair, amount_to_buy)
    portfolio.add_position(selected_pair, amount_to_buy, buy_price)

    # Monitoramento do portfólio a cada 5 minutos
    for _ in range(48):  # 4 horas
        time.sleep(300)  # Aguardar 5 minutos
        current_price = connector.get_data(selected_pair)[-1][4]
        portfolio.update_portfolio_value(selected_pair, current_price)
        
        if portfolio.calculate_profit() > 0:  # Se o lucro for positivo
            connector.sell(selected_pair, amount_to_buy)
            portfolio.reset_portfolio()
            break
        
        if portfolio.check_stop_loss():  # Se atingir o stop loss
            connector.sell(selected_pair, amount_to_buy)
            portfolio.reset_portfolio()
            break

if __name__ == '__main__':
    run_bot()
