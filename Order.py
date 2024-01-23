class Order:
    def __init__ (self, ticker, trader, side, limit, quant, filledQuant, status):
        self.ticker = ticker
        self.trader = trader
        self.side = side
        self.limit = limit
        self.quant = quant
        self.filledQuant = filledQuant
        self.status = status
    
    def update(self, ticker, trader, side, limit, quant, filledQuant, status):
        self.ticker = ticker
        self.trader = trader
        self.side = side
        self.limit = limit
        self.quant = quant
        self.filledQuant = filledQuant
        self.status = status
        
    @property
    def ticker(self):
        return self._ticker
    @ticker.setter
    def ticker(self, value):
        self._ticker = value
        
    @property
    def trader(self):
        return self._trader
    @price.setter
    def trader(self, value):
        self._trader = value
        
    @property
    def side(self):
        return self._side
    @price.setter
    def side(self, value):
        self._side = value
    
    @property
    def limit(self):
        return self._limit
    @price.setter
    def limit(self, value):
        self._limit = value
    
    @property
    def quant(self):
        return self._quant
    @quant.setter
    def quant(self, value):
        self._quant = value
    
    @property
    def filledQuant(self):
        return self._filledQuant
    @filledQuant.setter
    def filledQuant(self, value):
        self._filledQuant = value
        
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value
        
    def printOrder():
        sideString = 'buy' if Order.side == True else "sell"
        underline = '\033[4m'
        end = '\033[0m'
        print(underline + '| ticker | trader  | side | limit  | quantity | filledQty | status |' + end)
        print('| %-6s | %-7s | %-4s | $%-6.2f| %-8d | %-9d | %-6s |\n' % (Order.ticker, Order.trader, sideString, Order.limit, Order.quant, Order.filledQuant, Order.status))
    