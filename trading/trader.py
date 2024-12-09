import ccxt

class Trader:
    def __init__(self, api_key, secret_key):
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret_key,
        })

    def execute_trade(self, symbol, action, amount):
        if action == 'buy':
            self.exchange.create_market_buy_order(symbol, amount)
        elif action == 'sell':
            self.exchange.create_market_sell_order(symbol, amount)
