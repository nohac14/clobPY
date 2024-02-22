from yahooquery import Ticker
import os

def clear():
    os.system('clear')

def get_stock_price(stock_symbol):
    ticker = Ticker(stock_symbol)
    try:
        stock_price = ticker.quotes[stock_symbol]['regularMarketPrice']
        return stock_price
    except KeyError:
        return 'Stock price not found'

# Example usage
stock_symbol = 'AAPL'
print('Loading...')
stock_price = get_stock_price(stock_symbol)
clear()
print(f'The stock price of {stock_symbol} is: {stock_price}')