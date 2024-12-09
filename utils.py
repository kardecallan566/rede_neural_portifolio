def calculate_profit(portfolio, current_value):
    return (current_value - portfolio.initial_value) / portfolio.initial_value

def format_portfolio(portfolio):
    return {
        "initial_value": portfolio.initial_value,
        "current_value": portfolio.current_value,
        "profit": portfolio.calculate_profit()
    }
