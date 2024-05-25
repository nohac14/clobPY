class Trade:    
    def __init__(self, ticker, price, quant, buyOrder, sellOrder, status):
        """
        Initialize a new Trade with the given parameters.

        :param ticker: The ticker symbol of the trade
        :param price: The price at which the trade was executed
        :param quant: The quantity of the trade
        :param buyOrder: The buy order associated with the trade
        :param sellOrder: The sell order associated with the trade
        :param status: The status of the trade
        """
        self.ticker = ticker
        self.price = price
        self.quant = quant
        self.buyOrder = buyOrder
        self.sellOrder = sellOrder
        self.status = status

    def update(self, ticker, price, quant, buyOrder, sellOrder, status):
        """
        Update the trade details with new values.

        :param ticker: The new ticker symbol
        :param price: The new price at which the trade was executed
        :param quant: The new quantity of the trade
        :param buyOrder: The new buy order associated with the trade
        :param sellOrder: The new sell order associated with the trade
        :param status: The new status of the trade
        """
        self.ticker = ticker
        self.price = price
        self.quant = quant
        self.buyOrder = buyOrder
        self.sellOrder = sellOrder
        self.status = status
        
    @property
    def ticker(self):
        """
        Get the ticker symbol of the trade.

        :return: The current ticker symbol
        """
        return self._ticker

    @ticker.setter
    def ticker(self, value):
        """
        Set the ticker symbol of the trade.

        :param value: The new ticker symbol
        """
        self._ticker = value
        
    @property
    def price(self):
        """
        Get the price at which the trade was executed.

        :return: The current trade price
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Set the price at which the trade was executed.

        :param value: The new trade price
        """
        self._price = value
        
    @property
    def quant(self):
        """
        Get the quantity of the trade.

        :return: The current trade quantity
        """
        return self._quant

    @quant.setter
    def quant(self, value):
        """
        Set the quantity of the trade.

        :param value: The new trade quantity
        """
        self._quant = value
    
    @property
    def buyOrder(self):
        """
        Get the buy order associated with the trade.

        :return: The buy order
        """
        return self._buyOrder

    @buyOrder.setter
    def buyOrder(self, value):
        """
        Set the buy order associated with the trade.

        :param value: The new buy order
        """
        self._buyOrder = value
        
    @property
    def sellOrder(self):
        """
        Get the sell order associated with the trade.

        :return: The sell order
        """
        return self._sellOrder

    @sellOrder.setter
    def sellOrder(self, value):
        """
        Set the sell order associated with the trade.

        :param value: The new sell order
        """
        self._sellOrder = value

    @property
    def status(self):
        """
        Get the status of the trade.

        :return: The current trade status
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Set the status of the trade.

        :param value: The new trade status
        """
        self._status = value

    def printTrade(self):
        """
        Print the trade details in a formatted string with headers.
        """
        underline = '\033[4m'
        end = '\033[0m'
        print(underline + '| ticker |  price | quantity | buyer | seller | status   |' + end)
        print('| %-6s | $%-5.2f| %-8d | %-5d | %-6d | %-8s |' % (self.ticker, self.price, self.quant, int(self.buyOrder.trader), int(self.sellOrder.trader), self.status))
