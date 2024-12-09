import ccxt

class BinanceConnector:
    def __init__(self, api_key, secret_key):
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret_key,
        })
    
    def get_data(self, symbol, timeframe='5m'):
        data = self.exchange.fetch_ohlcv(symbol, timeframe)
        return data
    
    def buy(self, symbol, amount):
        order = self.exchange.create_market_buy_order(symbol, amount)
        return order
    
    def sell(self, symbol, amount):
        order = self.exchange.create_market_sell_order(symbol, amount)
        return order
    
    def get_balance(self):
        balance = self.exchange.fetch_balance()
        return balance
