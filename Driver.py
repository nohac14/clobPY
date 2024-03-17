import os
from random import seed
import random
from random import randint
from Order import Order
from Ticker import Ticker
from Trade import Trade
from Trader import Trader
import Scraper

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
    if (orderS.limit == orderB.limit):
        orderS.status = 'COMPLETED'
        orderB.status = 'COMPLETED'
        return True
    else:
        return False
    
    
def populateLists(bOrders, sOrders):
    numOrders = 10
    
    bgcGroup = Ticker('BGC')
    marketPrice = Scraper.get_stock_price('BGC')
        
    i = 0
    while(i < 10):
        if (i < 5):
            bOrders.append(Order(
                bgcGroup.identifier, 
                i, 
                'buy', 
                random.uniform(marketPrice - (marketPrice * 0.1), marketPrice + (marketPrice * 0.1)), 
                randint(1,100), 
                0, 
                'OPEN'
                ))
        else:
            sOrders.append(Order(
                bgcGroup.identifier, 
                i, 
                'sell', 
                random.uniform(marketPrice - (marketPrice * 0.1), marketPrice + (marketPrice * 0.1)), 
                randint(1,100), 
                0, 
                'OPEN'
                ))
        i+=1


def printheader():
    print('\n| ticker | trader  | side | limit  | quantity | filledQty | status |')
    

# main

bOrders = []
sOrders = []
populateLists(bOrders, sOrders)

printheader()
for order in bOrders:
    order.printAnotherOrder()
for order in sOrders:
    order.printAnotherOrder()