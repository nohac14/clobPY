class Trade:    
    def __init__ (self, ticker, price, quant, buyOrder, sellOrder):
        self.ticker = ticker
        self.price = price
        self.quant = quant
        self.buyOrder = buyOrder
        self.sellOrder = sellOrder

    def update (self, ticker, price, quant, buyOrder, sellOrder):
        self.ticker = ticker
        self.price = price
        self.quant = quant
        self.buyOrder = buyOrder
        self.sellOrder = sellOrder
        
    @property
    def ticker(self):
        return self._ticker
    @ticker.setter
    def ticker(self, value):
        self._ticker = value
        
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value
        
    @property
    def quant(self):
        return self._quant
    @quant.setter
    def quant(self, value):
        self._quant = value
    
    @property
    def buyOrder(self):
        return self._buyOrder
    @buyOrder.setter
    def buyOrder(self, value):
        self._buyOrder = value
        
    @property
    def sellOrder(self):
        return self._sellOrder
    @sellOrder.setter
    def sellOrder(self, value):
        self._sellOrder = value