import tkinter as tk
from tkinter import *
from Driver import *

root = tk.Tk()

clobPage = Frame(root)
tickerPage = Frame(root)
buyPage = Frame(root)
sellPage = Frame(root)

def showClobPage():
    from Driver import Scraper
    clobPage.pack()
    root.title("CLOB")
    
    btnFrame = Frame(clobPage)
    btnFrame.pack()

    appleBtntext = 'AAPL\nApple Inc.\n$%.2f' % (Scraper.get_stock_price('AAPL'))
    appleBtn = Button(btnFrame, text = appleBtntext, bd = '10') 
    appleBtn.pack(in_=btnFrame, side=LEFT)

    googleBtntext = 'GOOG\nAlphabet Inc. C\n$%.2f' % (Scraper.get_stock_price('GOOG'))
    googleBtn = Button(btnFrame, text = googleBtntext, bd = '10') 
    googleBtn.pack(in_=btnFrame, side=LEFT)

    nvidiaBtntext = 'NVDA\nNVIDIA Corp.\n$%.2f' % (Scraper.get_stock_price('NVDA'))
    nvidiaBtn = Button(btnFrame, text = nvidiaBtntext, bd = '10') 
    nvidiaBtn.pack(in_=btnFrame, side=LEFT)

    teslaBtntext = 'TSLA\nTesla Inc.\n$%.2f' % (Scraper.get_stock_price('TSLA'))
    teslaBtn = Button(btnFrame, text = teslaBtntext, bd = '10') 
    teslaBtn.pack(in_=btnFrame, side=LEFT)

    clobPage.grid_columnconfigure(0, weight=1)  # Make the buttons fill available space
    

    # searchIconFrame = Frame(root, width=5, height=5)
    # searchIconFrame.pack(side=LEFT)
    # searchIcon = PhotoImage(file="search_icon.png")
    # searchLabel = Label(searchIconFrame, image=searchIcon)

    searchFrame = Frame(clobPage)
    searchFrame.pack(side=TOP, padx=10, pady=10)  # Pack with padding

    searchLabel = Label(searchFrame, text='Search')
    searchLabel.pack(side=LEFT)  # Pack label inside the frame

    searchEntry = Entry(searchFrame)
    searchEntry.pack(side=LEFT, fill=X, padx=5)  # Pack entry with fill and padding
    
def showTickerPage():
    tickerPage.pack()
    root.title("")
    
def showBuyPage():
    buyPage.pack()
    root.title("Buy ")
    
def showSellPage():
    sellPage.pack()
    root.title("Sell")
    
    
showClobPage()

root.mainloop()
