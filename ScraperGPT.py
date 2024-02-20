from yahooquery import Ticker
from tqdm import tqdm
import time

def get_stock_price(stock_symbol):
    with tqdm(desc="Fetching stock data", unit="request", dynamic_ncols=True) as pbar:
        # Simulate loading delay for demonstration
        for _ in range(5):
            time.sleep(1)
            pbar.update(1)

        ticker = Ticker(stock_symbol)
        try:
            stock_price = ticker.quotes[stock_symbol]['regularMarketPrice']
            return stock_price
        except KeyError:
            return 'Stock price not found'

# Example usage
stock_symbol = 'AAPL'
stock_price = get_stock_price(stock_symbol)
print(f'\nThe stock price of {stock_symbol} is: {stock_price}')