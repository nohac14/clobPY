import requests
import yahooquery as yq

def get_stock_price(stock_symbol):
    """
    Fetch the current stock price for the given stock symbol.

    :param stock_symbol: The ticker symbol of the stock (e.g., 'AAPL' for Apple Inc.)
    :return: The current market price of the stock, or None if an error occurs
    """
    try:
        ticker = yq.Ticker(stock_symbol)
        return ticker.price[stock_symbol]['regularMarketPrice']
    except (yq.utils.utils.TickerNotFoundError, requests.exceptions.ContentDecodingError, requests.exceptions.RequestException) as e:
        print(f"Error fetching stock price for {stock_symbol}: {e}")
        return None

# Example usage
# stock_symbol = 'AAPL'
# print('Loading...')
# stock_price = get_stock_price(stock_symbol)
# print(f'The stock price of {stock_symbol} is: {stock_price}')
