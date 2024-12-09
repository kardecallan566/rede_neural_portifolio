class PortfolioManager:
    def __init__(self, initial_balance=15):
        self.balance = initial_balance
        self.assets = {}  # Pares de criptomoedas e quantidades compradas

    def buy(self, symbol, amount, price):
        """Comprar uma criptomoeda"""
        if symbol not in self.assets:
            self.assets[symbol] = 0
        self.assets[symbol] += amount
        self.balance -= amount * price
    
    def sell(self, symbol, amount, price):
        """Vender uma criptomoeda"""
        if symbol in self.assets and self.assets[symbol] >= amount:
            self.assets[symbol] -= amount
            self.balance += amount * price

    def get_balance(self):
        """Retornar o saldo total em dólares"""
        total_value = self.balance
        for symbol, amount in self.assets.items():
            # Aqui você usaria o preço atual do mercado para calcular o valor
            total_value += amount * self.get_current_price(symbol)
        return total_value

    def get_current_price(self, symbol):
        """Retornar o preço atual de uma criptomoeda"""
        # Aqui você poderia usar o ccxt para pegar o preço atual
        return 100  # Exemplo: preço fictício, substituir com a chamada à API
