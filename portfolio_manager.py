class PortfolioManager:
    def __init__(self, initial_value=15, stop_loss_threshold=0.05):
        self.initial_value = initial_value
        self.current_value = initial_value
        self.stop_loss_threshold = stop_loss_threshold
        self.holdings = {}
    
    def add_position(self, symbol, amount, buy_price):
        self.holdings[symbol] = {'amount': amount, 'buy_price': buy_price}
    
    def update_portfolio_value(self, symbol, current_price):
        if symbol in self.holdings:
            position = self.holdings[symbol]
            value = position['amount'] * current_price
            self.current_value += value - (position['amount'] * position['buy_price'])
    
    def calculate_profit(self):
        return self.current_value - self.initial_value
    
    def check_stop_loss(self):
        if self.calculate_profit() < -self.stop_loss_threshold * self.initial_value:
            return True
        return False
    
    def reset_portfolio(self):
        self.holdings = {}
        self.current_value = self.initial_value
