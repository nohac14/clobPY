import os
from random import seed, randint
import random
from Order import Order
from Ticker import Ticker
from Trade import Trade
from Trader import Trader
import Scraper

def clear():
    os.system('clear')

def isMatch(orderB, orderS):
    if orderB.trader != orderS.trader and orderB.side != orderS.side:  
        if orderB.side == 'buy' and orderS.side == 'sell':  
            if priceMatch(orderS, orderB): 
                return True  
    return False  

def priceMatch(orderS, orderB):
    if (orderS.limit == orderB.limit) or (orderS.limit <= orderB.limit):
        return True
    else:
        return False

def populateTickerMap(tickers, tickerMap):
    for ticker in tickers:
        tickerMap[ticker] = {'buy': [], 'sell': [], 'trades': []}
        populateLists(ticker, tickerMap)

def populateLists(ticker, tickerMap):
    numOrders = 10
    company = Ticker(ticker)
    marketPrice = Scraper.get_stock_price(ticker)

    i = 0
    while i < numOrders:
        if i < numOrders // 2:
            newOrder = Order(
                company.identifier, 
                randint(100, 1000) + i, 
                'buy', 
                random.uniform(marketPrice - (marketPrice * 0.1), marketPrice + (marketPrice * 0.1)), 
                randint(1, 100), 
                0, 
                'OPEN'
            )
            tickerMap[ticker]['buy'].append(newOrder)
            matchBuy(newOrder, ticker)
            sortOrders(ticker, 'buy')
        else:
            newOrder = Order(
                company.identifier, 
                randint(100, 1000) + i, 
                'sell', 
                random.uniform(marketPrice - (marketPrice * 0.1), marketPrice + (marketPrice * 0.1)), 
                randint(1, 100), 
                0, 
                'OPEN'
            )
            tickerMap[ticker]['sell'].append(newOrder)
            matchSell(newOrder, ticker)
            sortOrders(ticker, 'sell')
        i += 1

    newOrder = Order(
        company.identifier,
        randint(100, 1000) + 1,
        'buy',
        marketPrice, 
        50,
        0,
        'OPEN'
    )
    tickerMap[ticker]['buy'].append(newOrder)
    matchBuy(newOrder, ticker)
    sortOrders(ticker, 'buy')

    newOrder = Order(
        company.identifier,
        randint(100, 1000) + 1,
        'sell',
        marketPrice, 
        100,
        0,
        'OPEN'
    )
    tickerMap[ticker]['sell'].append(newOrder)
    matchSell(newOrder, ticker)
    sortOrders(ticker, 'sell')

def printOrders(bOrders, sOrders):
    print('\n| ticker | trader  | side | limit  | quantity | filled | status    |')
    for order in bOrders:
        order.printAnotherOrder()
    for order in sOrders:
        order.printAnotherOrder()

def printTickOrders(ticker):
    printOrders(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])

def addTicker():
    ticker = 'BGC'
    tickerMap[ticker] = {'buy': [], 'sell': [], 'trades': []}
    populateLists(ticker, tickerMap)
    printTickOrders(ticker)

def matchBuy(orderB, ticker):
    for orderS in tickerMap[ticker]['sell']:
        if isMatch(orderB, orderS):
            tradeQuant = min(orderB.quant - orderB.filledQuant, orderS.quant - orderS.filledQuant)
            trade = Trade(orderB.ticker, orderB.limit, tradeQuant, orderB, orderS, 'PENDING')
            tickerMap[ticker]['trades'].append(trade)

            orderB.filledQuant += tradeQuant
            orderS.filledQuant += tradeQuant

            if orderB.filledQuant == orderB.quant:
                orderB.status = 'COMPLETED'
            if orderS.filledQuant == orderS.quant:
                orderS.status = 'COMPLETED'

            trade.printTrade()

    removeCompleted(tickerMap, ticker)

def matchSell(orderS, ticker):
    for orderB in tickerMap[ticker]['buy']:
        if isMatch(orderB, orderS):
            tradeQuant = min(orderB.quant - orderB.filledQuant, orderS.quant - orderS.filledQuant)
            trade = Trade(orderB.ticker, orderB.limit, tradeQuant, orderB, orderS, 'PENDING')
            tickerMap[ticker]['trades'].append(trade)

            orderB.filledQuant += tradeQuant
            orderS.filledQuant += tradeQuant

            if orderB.filledQuant == orderB.quant:
                orderB.status = 'COMPLETED'
            if orderS.filledQuant == orderS.quant:
                orderS.status = 'COMPLETED'

            trade.printTrade()

    removeCompleted(tickerMap, ticker)

def removeCompleted(tickerMap, ticker):
    tickerMap[ticker]['buy'] = [order for order in tickerMap[ticker]['buy'] if order.status != 'COMPLETED']
    tickerMap[ticker]['sell'] = [order for order in tickerMap[ticker]['sell'] if order.status != 'COMPLETED']

def addOrder(ticker, trader, side, limit, quant):
    company = Ticker(ticker)
    newOrder = Order(
        company.identifier,
        trader,
        side,
        limit, 
        quant,
        0,
        'OPEN'
    )
    if side == 'buy':
        tickerMap[ticker][side].append(newOrder)
        matchBuy(newOrder, ticker)
        sortOrders(ticker, side)
    else:
        tickerMap[ticker][side].append(newOrder)
        matchSell(newOrder, ticker)
        sortOrders(ticker, side)

def sortOrders(ticker, side):
    if side == 'sell':
        tickerMap[ticker][side].sort(key=lambda order: order.limit)
    else:
        tickerMap[ticker][side].sort(key=lambda order: order.limit, reverse=True)

def userOrder(tickerMap):
    user='y'
    
    print('user: ', end='')
    trader = input()

    while user=='y':
        print('ticker: ', end='')
        ticker = input()
        clear()

        if ticker not in tickerMap:
            print(f"Ticker '{ticker}' not found or no orders available. Adding ticker to the order book...")
            tickerMap[ticker] = {'buy': [], 'sell': [], 'trades': []}
            populateLists(ticker, tickerMap)
            clear()

        print('\nORDER BOOK:')
        sortOrders(ticker, 'buy')
        sortOrders(ticker, 'sell')
        printOrders(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])
    
        print('Place Order (y/n)? ', end='')
        user = input()

        if user == 'n':
            return

        print('buy OR sell: ', end='')
        uSide = input()

        print('limit: $', end='')
        limit = float(input())

        print('quantity: ', end='')
        quant = int(input())

        addOrder(ticker, trader, uSide, limit, quant)

        print('\nORDER BOOK:')
        printOrders(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])

tickerMap = {}
userOrder(tickerMap)
