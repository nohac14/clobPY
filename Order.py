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
        
    def printOrder():
        sideString = 'buy' if True else "sell"
        underline = '\033[4m'
        end = '\033[0m'
        print(underline + '| ticker | trader  | side | limit  | quantity | filledQty | status |' + end)
        print('| %-6s | %-7s | %-4s | $%-6.2f| %-8d | %-9d | %-6s |\n' % (ticker.getIdentifier(), trader.getUsername(), sideString, limit, quant, filledQuant, status))
    