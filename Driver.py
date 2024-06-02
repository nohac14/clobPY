import os
from random import seed, randint
import random
from Order import Order
from Ticker import Ticker
from Trade import Trade
from Trader import Trader
import Scraper

def clear():
    """
    Clear the console output.
    """
    os.system('clear')

def isMatch(orderB, orderS):
    """
    Check if a buy order matches a sell order.

    :param orderB: The buy order
    :param orderS: The sell order
    :return: True if the orders match, False otherwise
    """
    if orderB.trader != orderS.trader and orderB.side != orderS.side:  
        if orderB.side == 'buy' and orderS.side == 'sell':  
            if priceMatch(orderS, orderB): 
                return True  
    return False  

def priceMatch(orderS, orderB):
    """
    Check if the price of a sell order matches the price of a buy order.

    :param orderS: The sell order
    :param orderB: The buy order
    :return: True if the prices match, False otherwise
    """
    if (orderS.limit == orderB.limit) or (orderS.limit <= orderB.limit):
        return True
    else:
        return False

def initializeTicker(ticker, tickerMap):
    """
    Initialize a ticker in the ticker map.

    :param ticker: The ticker symbol
    :param tickerMap: The dictionary to store tickers and their orders
    """
    if ticker not in tickerMap:
        tickerMap[ticker] = {'buy': [], 'sell': [], 'trades': []}

def populateTickerMap(tickers, tickerMap):
    """
    Populate the ticker map with initial data for each ticker.

    :param tickers: A list of ticker symbols
    :param tickerMap: The dictionary to store tickers and their orders
    """
    for ticker in tickers:
        initializeTicker(ticker, tickerMap)
        populateLists(ticker, tickerMap)

def populateLists(ticker, tickerMap):
    """
    Populate the buy and sell lists for a given ticker with initial orders.

    :param ticker: The ticker symbol
    :param tickerMap: The dictionary to store tickers and their orders
    """
    numOrders = 10
    company = Ticker(ticker)
    marketPrice = Scraper.get_stock_price(ticker)

    for i in range(numOrders):
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
    """
    Print the buy and sell orders in a formatted table.

    :param bOrders: List of buy orders
    :param sOrders: List of sell orders
    """
    print('\n| ticker | trader  | side | limit  | quantity | filled | status    |')
    for order in bOrders:
        order.printAnotherOrder()
    for order in sOrders:
        order.printAnotherOrder()

def printTickOrders(ticker):
    """
    Print the orders for a specific ticker.

    :param ticker: The ticker symbol
    """
    printOrders(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])

def addTicker():
    """
    Add a new ticker to the ticker map and populate it with initial orders.
    """
    ticker = 'BGC'
    initializeTicker(ticker, tickerMap)
    populateLists(ticker, tickerMap)
    printTickOrders(ticker)

def matchBuy(orderB, ticker):
    """
    Match a buy order with sell orders.

    :param orderB: The buy order
    :param ticker: The ticker symbol
    """
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
    """
    Match a sell order with buy orders.

    :param orderS: The sell order
    :param ticker: The ticker symbol
    """
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
    """
    Remove completed orders from the ticker map.

    :param tickerMap: The dictionary storing tickers and their orders
    :param ticker: The ticker symbol
    """
    tickerMap[ticker]['buy'] = [order for order in tickerMap[ticker]['buy'] if order.status != 'COMPLETED']
    tickerMap[ticker]['sell'] = [order for order in tickerMap[ticker]['sell'] if order.status != 'COMPLETED']

def addOrder(ticker, trader, side, limit, quant):
    """
    Add a new order to the ticker map and match it against existing orders.

    :param ticker: The ticker symbol
    :param trader: The trader ID
    :param side: The side of the order ('buy' or 'sell')
    :param limit: The limit price of the order
    :param quant: The quantity of the order
    """
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
    """
    Sort orders by their limit price.

    :param ticker: The ticker symbol
    :param side: The side of the order ('buy' or 'sell')
    """
    # if side == 'sell':
    #     tickerMap[ticker][side].sort(key=lambda order: order.limit)
    # else:
    #     tickerMap[ticker][side].sort(key=lambda order: order.limit, reverse=True)
    tickerMap[ticker][side].sort(key=lambda order: order.limit)
        
def uInputOrder(tickerMap, ticker, trader):
    """
    Take user input for a new order and add it to the ticker map.

    :param tickerMap: The dictionary storing tickers and their orders
    :param ticker: The ticker symbol
    :param trader: The trader ID
    """
    print('Enter order in the format {side} {quantity} @ {limit}: ', end='')
    order_input = input().strip()

    try:
        side, rest = order_input.split(' ', 1)
        quant_str, limit_str = rest.split(' @ ')
        quant = int(quant_str)
        limit = float(limit_str)
    except ValueError:
        print("Invalid input format. Please enter the order in the format {side} {quantity} @ {limit}.")
        return

    addOrder(ticker, trader, side, limit, quant)

    print('\nORDER BOOK:')
    printOrders(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])

def userOrder(tickerMap, trader):
    """
    Prompt the user to place orders and update the order book accordingly.

    :param tickerMap: The dictionary storing tickers and their orders
    :param trader: The trader ID
    """
    user = 'y'

    while user == 'y':
        print('ticker: ', end='')
        ticker = input()
        clear()

        if ticker not in tickerMap:
            print(f"Ticker '{ticker}' not found or no orders available. Adding ticker to the order book...")
            initializeTicker(ticker, tickerMap)
            populateLists(ticker, tickerMap)
            clear()

        print('\nORDER BOOK:')
        sortOrders(ticker, 'buy')
        sortOrders(ticker, 'sell')
        printOrders(tickerMap[ticker]['buy'], tickerMap[ticker]['sell'])
    
        print('Place Order (y/n)? ', end='')
        user = input()

        if user == 'y':
            uInputOrder(tickerMap, ticker, trader)
        else:
            print('Quit (y/n)?: ', end='')
            isQuit = input()
            if isQuit == 'n':
                userOrder(tickerMap, trader)

def runInTerminal(tickerMap):
    """
    Run the trading application in the terminal.

    :param tickerMap: The dictionary storing tickers and their orders
    """
    print('user: ', end='')
    trader = input()
    userOrder(tickerMap, trader)
        
tickerMap = {}
