import Scraper

class Order:
    def __init__(self, ticker: str, trader: str, side: str, limit: float, quant: int, filledQuant: int, status: str) -> None:
        """
        Initialize a new order with given parameters.
        
        :param ticker: The stock ticker symbol
        :param trader: The ID or name of the trader
        :param side: The side of the order ('buy' or 'sell')
        :param limit: The limit price for the order
        :param quant: The quantity of the order
        :param filledQuant: The quantity of the order that has been filled
        :param status: The current status of the order
        """
        self.ticker = ticker
        self.trader = trader
        self.side = side
        self.limit = limit
        self.quant = quant
        self.filledQuant = filledQuant
        self.status = status

    def __str__(self):
        """
        Return a formatted string representation of the order.

        :return: Formatted string of the order
        """
        return '| %-6s | %-7s | %-4s | $%-6.2f | %-8d | %-6d | %-9s |' % (
            self.ticker, self.trader, self.side, self.limit, self.quant, self.filledQuant, self.status
        )

    def update(self, ticker, trader, side, limit, quant, filledQuant, status):
        """
        Update the order with new values.
        
        :param ticker: The stock ticker symbol
        :param trader: The ID or name of the trader
        :param side: The side of the order ('buy' or 'sell')
        :param limit: The limit price for the order
        :param quant: The quantity of the order
        :param filledQuant: The quantity of the order that has been filled
        :param status: The current status of the order
        """
        self.ticker = ticker
        self.trader = trader
        self.side = side
        self.limit = limit
        self.quant = quant
        self.filledQuant = filledQuant
        self.status = status

    @property
    def ticker(self):
        """
        Get the ticker symbol.

        :return: Ticker symbol
        """
        return self._ticker

    @ticker.setter
    def ticker(self, value):
        """
        Set the ticker symbol.

        :param value: New ticker symbol
        """
        self._ticker = value

    @property
    def trader(self):
        """
        Get the trader ID or name.

        :return: Trader ID or name
        """
        return self._trader

    @trader.setter
    def trader(self, value):
        """
        Set the trader ID or name.

        :param value: New trader ID or name
        """
        self._trader = value

    @property
    def side(self):
        """
        Get the side of the order.

        :return: Order side ('buy' or 'sell')
        """
        return self._side

    @side.setter
    def side(self, value):
        """
        Set the side of the order.

        :param value: New order side ('buy' or 'sell')
        """
        self._side = value

    @property
    def limit(self):
        """
        Get the limit price of the order.

        :return: Limit price
        """
        return self._limit

    @limit.setter
    def limit(self, value):
        """
        Set the limit price of the order.

        :param value: New limit price
        """
        self._limit = value

    @property
    def quant(self):
        """
        Get the quantity of the order.

        :return: Order quantity
        """
        return self._quant

    @quant.setter
    def quant(self, value):
        """
        Set the quantity of the order.

        :param value: New order quantity
        """
        self._quant = value

    @property
    def filledQuant(self):
        """
        Get the filled quantity of the order.

        :return: Filled quantity
        """
        return self._filledQuant

    @filledQuant.setter
    def filledQuant(self, value):
        """
        Set the filled quantity of the order.

        :param value: New filled quantity
        """
        self._filledQuant = value

    @property
    def status(self):
        """
        Get the status of the order.

        :return: Order status
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Set the status of the order.

        :param value: New order status
        """
        self._status = value

    def printOrder(self):
        """
        Print the order details in a formatted string with headers.
        """
        self.side = 'buy' if self.side else "sell"
        underline = '\033[4m'
        end = '\033[0m'
        print(underline + '| ticker | trader  | side | limit  | quantity | filledQty | status |' + end)
        print('| %-6s | %-7s | %-4s | $%-6.2f| %-8d | %-6d | %-9s |' % (self.ticker, self.trader, self.side, self.limit, self.quant, self.filledQuant, self.status))

    def printAnotherOrderO(self):  # deprecated
        """
        Print the order details with deprecated method. 
        This method is kept for backward compatibility.
        """
        green = '\u001b[32m'
        red = '\u001b[31m'
        end = '\033[0m'
        print('--------------------------------------------------------------------')
        if self.side == 'buy':
            print('| %-6s | %-7s | %s%-4s%s | $%-6.2f| %-8d | %-6d | %-9s |' % (self.ticker, self.trader, green, self.side, end, self.limit, self.quant, self.filledQuant, self.status))
        else:
            print('| %-6s | %-7s | %s%-4s%s | $%-6.2f| %-8d | %-6d | %-9s |' % (self.ticker, self.trader, red, self.side, end, self.limit, self.quant, self.filledQuant, self.status))

    def printAnotherOrder(self):
        """
        Print the order details with correct data types and color coding for side.
        """
        # Check if limit, quant, and filledQuant are numeric types
        if not isinstance(self.limit, (int, float)) or not isinstance(self.quant, int) or not isinstance(self.filledQuant, int):
            print("Error: Invalid data types in Order attributes.")
            return

        # Format the string with correct data types
        if self.side == 'buy':
            print('| %-6s | %-7s | %s%-4s%s | $%-6.2f| %-8d | %-6d | %-9s |' % (
                self.ticker, self.trader, '\u001b[32m', self.side, '\033[0m', float(self.limit), int(self.quant), int(self.filledQuant), self.status))
        else:
            print('| %-6s | %-7s | %s%-4s%s | $%-6.2f| %-8d | %-6d | %-9s |' % (
                self.ticker, self.trader, '\u001b[31m', self.side, '\033[0m', float(self.limit), int(self.quant), int(self.filledQuant), self.status))
