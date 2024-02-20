import os
from Order import Order
from Ticker import Ticker
from Trade import Trade
from Trader import Trader

def clear():
    os.system('clear')

print("username: ", end="")
trader = Trader(input())
tradeweb = Ticker('TW')

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