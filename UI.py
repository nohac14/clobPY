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
    appleBtn = Button(btnFrame, text=appleBtntext, bd = 10,  command=lambda: showTickerPage('AAPL')) 
    appleBtn.pack(in_=btnFrame, side=LEFT)


    googleBtntext = 'GOOG\nAlphabet Inc. C\n$%.2f' % (Scraper.get_stock_price('GOOG'))
    googleBtn = Button(btnFrame, text = googleBtntext, bd = 10, command=lambda: showTickerPage('GOOG')) 
    googleBtn.pack(in_=btnFrame, side=LEFT)

    nvidiaBtntext = 'NVDA\nNVIDIA Corp.\n$%.2f' % (Scraper.get_stock_price('NVDA'))
    nvidiaBtn = Button(btnFrame, text = nvidiaBtntext, bd = 10, command=lambda: showTickerPage('NVDA')) 
    nvidiaBtn.pack(in_=btnFrame, side=LEFT)

    teslaBtntext = 'TSLA\nTesla Inc.\n$%.2f' % (Scraper.get_stock_price('TSLA'))
    teslaBtn = Button(btnFrame, text = teslaBtntext, bd = 10, command=lambda: showTickerPage('TSLA')) 
    teslaBtn.pack(in_=btnFrame, side=LEFT)

    clobPage.grid_columnconfigure(0, weight=1)  # Make the buttons fill available space
    

    searchFrame = Frame(clobPage)
    searchFrame.pack(side=TOP, padx=10, pady=10)  # Pack with padding

    searchLabel = Label(searchFrame, text='Search', fg='#87CEEB')
    searchLabel.pack(side=LEFT)  # Pack label inside the frame

    searchEntry = Entry(searchFrame)
    searchEntry.insert(0, 'ex. BGC')

    def onEntryKey(event):
        if searchEntry.get() == 'ex. BGC':
            searchEntry.delete(0, END)  # Clear placeholder text when user starts typing

    def onEntryLeave(event):
        if not searchEntry.get():
            searchEntry.insert(0, 'ex. BGC')  # Restore placeholder text if Entry widget is left empty

    def onReturn(event):
        showTickerPage(searchEntry.get())  # Pass the text from the Entry widget to showTickerPage

    searchEntry.bind("<Key>", onEntryKey)
    searchEntry.bind("<FocusOut>", onEntryLeave)
    searchEntry.bind('<Return>', onReturn)

    searchEntry.pack(side=LEFT, fill=X, padx=5)

def removeAllWidgets(parent_widget):
    for widget in parent_widget.winfo_children():
        widget.destroy()
    
def showTickerPage(ticker):
    removeAllWidgets(clobPage)
    tickerPage.pack()
    root.title(ticker)
    
def showBuyPage(ticker):
    buyPage.pack()
    root.title("Buy ")
    
def showSellPage(ticker):
    sellPage.pack()
    root.title("Sell")
    
    
showClobPage()

root.mainloop()
