import os
from Order import Order
from Ticker import Ticker
from Trade import Trade
from Trader import Trader

def clear():
    os.system('clear')
    
def printTest():
    print("username: ", end="")
    trader = Trader(input())

    tradeweb = Ticker('TW')
    apple = Ticker('AAPL')
    bgcGroup = Ticker('BGC')
    amd = Ticker('AMD')

    clear()
    order = Order(
        tradeweb.identifier,
        trader.username,
        'buy',
        100,
        0,
        'OPEN'
    )
    order.printOrder()

    order1 = Order(
        apple.identifier,
        trader.username,
        'buy',
        50,
        0,
        'OPEN'
    )
    order1.printAnotherOrder()

    order2 = Order(
        bgcGroup.identifier,
        trader.username,
        'buy',
        30,
        0,
        'OPEN'
    )
    order2.printAnotherOrder()

    order3 = Order(
        amd.identifier,
        trader.username,
        'buy',
        20,
        0,
        'OPEN'
    )
    order3.printAnotherOrder()
    
def scenario1():
    print("username: ", end="")
    trader = Trader(input())
    
    clear()
    order = Order(
        Ticker('TW'),
        trader.username,
        'buy',
        100,
        0,
        'OPEN'
    )
    order.printOrder()
    
def scenario2():
    print('balls')
    
def isMatch(order1, order2):
    if ((order1.trader == order2.trader) or (order1.side == order2.side)):
        return False
    else:
        if(order1.side == 'sell'):
            if ((order1.quant - order1.filledQuant) >= (order2.quant - order2.filledQuant)):
                return priceMatch(order1, order2)
            else:
                return False
        else:
            if ((order2.quant - order2.filledQuant) >= (order1.quant - order1.filledQuant)):
                return priceMatch(order2, order1)
            else:
                return False
            
def priceMatch(orderS, orderB):
    if (((orderS.limit + 1) >= orderB.limit) or ((orderB.limit + 1) >= orderS.limit) or (orderS.limit == orderB.limit)):
        orderS.status = 'COMPLETED'
        orderB.status = 'COMPLETED'
        return True
    else:
        return False
    
scenario1()