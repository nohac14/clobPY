import tkinter as tk
from tkinter import *
from Driver import *

root = tk.Tk()

clobPage = Frame(root)
tickerPage = Frame(root)

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
    tickerPage.pack()  # Fill and expand the tickerPage frame
    root.title(ticker)
    
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        
    font_size = 15
        
    titleFrame = Frame(tickerPage)
    titleFrame.pack(side=TOP, fill=X)  # Pack titleFrame to the top with horizontal fill
    
    titles = ['    ticker', '        trader', '       side', '          limit', '      quantity', '       filled', '      status']
    for title in titles:
        title_label = Label(titleFrame, text=title, font=('Arial', font_size), pady=5)
        title_label.pack(side=LEFT)

    canvas = Canvas(tickerPage, highlightthickness=0)  # Set highlightthickness to 0 to remove border
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    scrollbar = Scrollbar(tickerPage, command=canvas.yview)  # Place scrollbar in tickerPage
    scrollbar.pack(side=LEFT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")
    
    columns = []
    for i in range(7):
        column = Frame(frame, bd=1, relief=SOLID)
        column.grid(row=0, column=i, sticky="nsew")
        columns.append(column)

        # Fill each column with some text
        text = "\n".join([f"Item {j+1}" for j in range(20)])  # 20 example items
        content_label = Label(column, text=text, padx=10, pady=10)
        content_label.pack(side=LEFT)  # Pack content_label inside the column

    # Configure the grid to expand with the window
    for i in range(7):
        frame.grid_columnconfigure(i, weight=1)

    # Bind the canvas to the scrollbar and configure scrolling
    canvas.bind("<Configure>", on_configure)
    
    def on_radio_button_change():
        selected_option.set(selected_radio.get())  # Update the selected_option variable

    # Create a variable to track the selected option
    selected_option = StringVar()

    # Create a frame for the radio buttons
    radio_frame = Frame(root)
    radio_frame.pack(pady=20)

    # Define the options for the radio buttons
    options = ['Buy', 'Sell']

    # Create radio buttons for each option
    selected_radio = StringVar()
    selected_radio.set(options[0])  # Set the default selected radio button

    for option in options:
        radio_button = Radiobutton(radio_frame, text=option, variable=selected_radio, value=option, command=on_radio_button_change)
        radio_button.pack(anchor=W)  # Align radio buttons to the left (west)

    
    
showClobPage()

root.mainloop()
