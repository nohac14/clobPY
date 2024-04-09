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
    
def printTest(): # sort of deprecated
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
    
def isMatchOld(order1, order2): # sort of deprecated
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
            
def isMatch(orderB, orderS):
    if orderB.trader != orderS.trader and orderB.side != orderS.side:  # Different trader and opposite sides
        if orderB.side == 'buy' and orderS.side == 'sell':  # Ensure correct buy/sell relationship
            if orderS.limit <= orderB.limit:  # Check if seller's limit is acceptable to the buyer
                return True  # Potential match
    return False  # No match
            
def priceMatch(orderS, orderB):
    if (orderS.limit == orderB.limit):
        return True
    else:
        return False
      
def populateLists(ticker, tickerMap): # randomly populates the order lists
    numOrders = 10
    
    company = Ticker(ticker)
    marketPrice = Scraper.get_stock_price(ticker)
        
    # i = 0
    # while(i < 10):
    #     if (i < 5):
    #         tickerMap[ticker]['buy'].append(Order(
    #             company.identifier, 
    #             randint(100, 1000)+i, 
    #             'buy', 
    #             random.uniform(marketPrice - (marketPrice * 0.1), marketPrice + (marketPrice * 0.1)), # random limit between 10% below and above current stock price
    #             randint(1,100), 
    #             0, 
    #             'OPEN'
    #             ))
    #     else:
    #         tickerMap[ticker]['sell'].append(Order(
    #             company.identifier, 
    #             randint(100, 1000)+i, 
    #             'sell', 
    #             random.uniform(marketPrice - (marketPrice * 0.1), marketPrice + (marketPrice * 0.1)), 
    #             randint(1,100), 
    #             0, 
    #             'OPEN'
    #             ))
    #     i+=1
        
    tickerMap[ticker]['buy'].append(Order(
        company.identifier,
        randint(100,1000)+1,
        'buy',
        marketPrice, 
        50,
        0,
        'OPEN'
    ))
    tickerMap[ticker]['sell'].append(Order(
        company.identifier,
        randint(100,1000)+1,
        'sell',
        marketPrice, 
        100,
        0,
        'OPEN'
    ))
    # tickerMap[ticker] = {'buy' : bOrders, 'sell' : sOrders}

def printOrders(bOrders, sOrders):
    print('\n| ticker | trader  | side | limit  | quantity | filledQty | status |')
    for order in bOrders:
        order.printAnotherOrder()
    for order in sOrders:
        order.printAnotherOrder()

def printTickOrders(ticker):
    printOrders(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])

def addTicker():
    # print('insert ticker: ', end='')
    # ticker = input()

    ticker = 'BGC'
    tickerMap[ticker] = {'buy': [], 'sell': []}
    populateLists(ticker, tickerMap)
    printTickOrders(ticker)

def match(bOrders, sOrders):
    matches = []
    for orderB in bOrders:
        for orderS in sOrders:
            if (isMatch(orderB, orderS)):
                matches.append((orderB, orderS))
    
    for orderB, orderS in matches:
        print("Potential Match:", orderB, orderS)
        tradeQuant = min(orderB.quant - orderB.filledQuant, orderS.quant - orderS.filledQuant)
        
        tradePrice = orderB.limit
        trade = Trade(orderB.ticker, orderB.limit, tradeQuant, orderB, orderS, 'EXECUTED')
        
        orderB.filledQuant += tradeQuant
        orderS.filledQuant += tradeQuant
        
        print("Trade:", trade)
        
        if orderB.filledQuant == orderB.quant:
            orderB.status = 'COMPLETED'
        if orderS.filledQuant == orderS.quant:
            orderS.status = 'COMPLETED'
            
def removeCompleted(tickerMap, ticker):
    tickerMap[ticker]['buy'] = [order for order in tickerMap[ticker]['buy'] if order.status != 'COMPLETED']
    tickerMap[ticker]['sell'] = [order for order in tickerMap[ticker]['sell'] if order.status != 'COMPLETED']

# main

tickerMap = {}
user = 'y'

# while (user == 'y'):
#     addTicker(tickerMap)
#     print('\nAdd another ticker? ', end='')
#     user = input()


# print('ticker orders to be matched: ', end='')
# ticker = input()

addTicker()

ticker = 'BGC'

# bOrders = tickerMap[ticker]['buy']
# sOrders = tickerMap[ticker]['sell']

print('\nBEFORE:')
printOrders(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])

match(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])

print('\nAFTER:')
printOrders(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])

print('\nREMOVE COMPLETED:')
removeCompleted(tickerMap, ticker)
printOrders(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])
