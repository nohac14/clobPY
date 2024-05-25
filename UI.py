import tkinter as tk
from tkinter import *
from random import randint
from Driver import *

# Initialize the root window
root = tk.Tk()
root.iconphoto(False, tk.PhotoImage(file="iconbook.png"))
clobPage = Frame(root)
tickerPage = Frame(root)

# Generate a unique user ID between 1 and 1000
user_id = randint(1, 1000)

def showClobPage():
    """
    Display the main page with stock buttons and a search bar.
    """
    from Driver import Scraper
    
    # Display the main frame and set the window title
    clobPage.grid(row=0, column=0, sticky='nsew')
    root.title("CLOB")

    # Display the user ID
    user_id_label = Label(clobPage, text=f"User ID: {user_id}", font=('Helvetica', 14))
    user_id_label.grid(row=0, column=0, pady=10, columnspan=2)

    # Create and layout the button frame
    btnFrame = Frame(clobPage)
    btnFrame.grid(row=1, column=0, columnspan=2)

    # Define button texts and commands
    appleBtntext = 'AAPL\nApple Inc.\n$%.2f' % (Scraper.get_stock_price('AAPL'))
    appleBtn = Button(btnFrame, text=appleBtntext, bd=10, command=lambda: showTickerPage('AAPL', user_id))
    appleBtn.grid(row=0, column=0, padx=5)

    googleBtntext = 'GOOG\nAlphabet Inc. C\n$%.2f' % (Scraper.get_stock_price('GOOG'))
    googleBtn = Button(btnFrame, text=googleBtntext, bd=10, command=lambda: showTickerPage('GOOG', user_id))
    googleBtn.grid(row=0, column=1, padx=5)

    nvidiaBtntext = 'NVDA\nNVIDIA Corp.\n$%.2f' % (Scraper.get_stock_price('NVDA'))
    nvidiaBtn = Button(btnFrame, text=nvidiaBtntext, bd=10, command=lambda: showTickerPage('NVDA', user_id))
    nvidiaBtn.grid(row=0, column=2, padx=5)

    teslaBtntext = 'TSLA\nTesla Inc.\n$%.2f' % (Scraper.get_stock_price('TSLA'))
    teslaBtn = Button(btnFrame, text=teslaBtntext, bd=10, command=lambda: showTickerPage('TSLA', user_id))
    teslaBtn.grid(row=0, column=3, padx=5)

    clobPage.grid_columnconfigure(0, weight=1)  # Make the buttons fill available space

    # Create and layout the search frame
    searchFrame = Frame(clobPage)
    searchFrame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Add the search label and entry
    searchLabel = Label(searchFrame, text='Search', fg='#87CEEB')
    searchLabel.grid(row=0, column=0, padx=5)

    searchEntry = Entry(searchFrame)
    searchEntry.insert(0, 'ex. BGC')

    # Event handlers for the search entry
    def onEntryKey(event):
        """
        Clear the placeholder text when the user starts typing.
        """
        if searchEntry.get() == 'ex. BGC':
            searchEntry.delete(0, END)

    def onEntryLeave(event):
        """
        Restore the placeholder text if the entry is empty.
        """
        if not searchEntry.get():
            searchEntry.insert(0, 'ex. BGC')

    def onReturn(event):
        """
        Trigger a search and display the ticker page when the user presses Enter.
        """
        searchTicker = searchEntry.get()
        showTickerPage(searchTicker, user_id)

    searchEntry.bind("<Key>", onEntryKey)
    searchEntry.bind("<FocusOut>", onEntryLeave)
    searchEntry.bind('<Return>', onReturn)

    searchEntry.grid(row=0, column=1, padx=5, sticky='ew')

def removeAllWidgets(parent_widget):
    """
    Remove all child widgets from a given parent widget.

    :param parent_widget: The parent widget
    """
    for widget in parent_widget.winfo_children():
        widget.destroy()

def showTickerPage(ticker, user_id):
    """
    Display the ticker page with order entry, search, and terminal-like output.

    :param ticker: The stock ticker symbol
    :param user_id: The user's unique ID
    """
    removeAllWidgets(clobPage)
    tickerPage.grid(row=0, column=0, sticky='nsew')  # Fill and expand the tickerPage frame
    root.title(ticker)

    # Display the user ID
    user_id_label = Label(tickerPage, text=f"User ID: {user_id}", font=('Helvetica', 14))
    user_id_label.grid(row=0, column=0, pady=5, columnspan=2)

    # Create a loading label
    loading_label = Label(tickerPage, text="Loading...", font=('Helvetica', 14))
    loading_label.grid(row=1, column=0, pady=5, columnspan=2)

    # Update the GUI to show the loading label
    root.update_idletasks()

    # Radio buttons for Buy/Sell
    def on_radio_button_change():
        """
        Update the selected option when a radio button is changed.
        """
        selected_option.set(selected_radio.get())

    selected_option = StringVar()
    radio_frame = Frame(tickerPage)
    radio_frame.grid(row=2, column=0, columnspan=2, pady=5)

    options = ['Buy', 'Sell']
    selected_radio = StringVar()
    selected_radio.set(options[0])

    for i, option in enumerate(options):
        radio_button = Radiobutton(radio_frame, text=option, variable=selected_radio, value=option, command=on_radio_button_change)
        radio_button.grid(row=0, column=i, padx=5)
        
    dollarLabel = Label(radio_frame, text='$')
    dollarLabel.grid(row=0, column=2, padx=5)
    
    limitEntry = Entry(radio_frame, width=5)
    limitEntry.insert(0, 'limit')
    
    # Event handlers for limit entry
    def onEntryKey(event):
        """
        Clear the placeholder text when the user starts typing.
        """
        if limitEntry.get() == 'limit':
            limitEntry.delete(0, END)

    def onEntryLeave(event):
        """
        Restore the placeholder text if the entry is empty.
        """
        if not limitEntry.get():
            limitEntry.insert(0, 'limit')

    def onReturn(event):
        """
        Add the order and update the order book when the user presses Enter.
        """
        limit = float(limitEntry.get())
        quant = int(quantEntry.get())
        side = selected_radio.get().lower()
        addOrder(ticker, user_id, side, limit, quant)
        display_order_book()

    limitEntry.bind("<Key>", onEntryKey)
    limitEntry.bind("<FocusOut>", onEntryLeave)
    limitEntry.bind('<Return>', onReturn)
    limitEntry.grid(row=0, column=3, padx=5, sticky='w')
    
    quantEntry = Entry(radio_frame, width=6)
    quantEntry.insert(0, 'quantity')
    
    # Event handlers for quantity entry
    def onEntryKey(event):
        """
        Clear the placeholder text when the user starts typing.
        """
        if quantEntry.get() == 'quantity':
            quantEntry.delete(0, END)

    def onEntryLeave(event):
        """
        Restore the placeholder text if the entry is empty.
        """
        if not quantEntry.get():
            quantEntry.insert(0, 'quantity')

    def onReturn(event):
        """
        Add the order and update the order book when the user presses Enter.
        """
        limit = float(limitEntry.get())
        quant = int(quantEntry.get())
        side = selected_radio.get().lower()
        addOrder(ticker, user_id, side, limit, quant)
        display_order_book()

    quantEntry.bind("<Key>", onEntryKey)
    quantEntry.bind("<FocusOut>", onEntryLeave)
    quantEntry.bind('<Return>', onReturn)
    quantEntry.grid(row=0, column=4, padx=5, sticky='w')
    
    searchFrame = Frame(radio_frame)
    searchFrame.grid(row=0, column=5, padx=10, pady=5, sticky='w')

    searchLabel = Label(searchFrame, text='Search', fg='#87CEEB')
    searchLabel.grid(row=0, column=0, padx=5)

    searchEntry = Entry(searchFrame, width=10)
    searchEntry.insert(0, 'ex. BGC')

    # Event handlers for search entry
    def onEntryKey(event):
        """
        Clear the placeholder text when the user starts typing.
        """
        if searchEntry.get() == 'ex. BGC':
            searchEntry.delete(0, END)

    def onEntryLeave(event):
        """
        Restore the placeholder text if the entry is empty.
        """
        if not searchEntry.get():
            searchEntry.insert(0, 'ex. BGC')

    def onReturn(event):
        """
        Trigger a search and display the ticker page when the user presses Enter.
        """
        ticker = searchEntry.get()
        removeAllWidgets(tickerPage)
        showTickerPage(ticker, user_id)

    searchEntry.bind("<Key>", onEntryKey)
    searchEntry.bind("<FocusOut>", onEntryLeave)
    searchEntry.bind('<Return>', onReturn)
    searchEntry.grid(row=0, column=1, padx=5, sticky='w')

    # Terminal-like widget
    terminal_frame = Frame(tickerPage)
    terminal_frame.grid(row=3, column=0, columnspan=2, sticky='nsew')
    tickerPage.grid_rowconfigure(3, weight=1)
    tickerPage.grid_columnconfigure(0, weight=1)

    terminal = Text(terminal_frame, wrap='none', state='disabled', bg='black', fg='white', font=('Courier', 12))
    terminal.grid(row=0, column=0, sticky='nsew')
    scrollbar = Scrollbar(terminal_frame, command=terminal.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    terminal.configure(yscrollcommand=scrollbar.set)

    # Configure text tags for coloring
    terminal.tag_config('buy', foreground='green')
    terminal.tag_config('sell', foreground='red')
    terminal.tag_config('header', font=('Courier', 12, 'bold', 'underline'))

    # Display order book in terminal
    def display_order_book():
        """
        Display the order book in the terminal-like widget.
        """
        terminal.configure(state='normal')
        terminal.delete('1.0', END)
        header = '| ticker | trader  | side | limit   | quantity | filled | status    |\n'
        terminal.insert('end', header, 'header')
        if ticker in tickerMap:
            orders = tickerMap[ticker]
            for order in orders['buy']:
                formatted_order = f"| {order.ticker:<6} | {order.trader:<7} | "
                terminal.insert('end', formatted_order)
                terminal.insert('end', 'buy ', 'buy ')
                formatted_order = f" | ${order.limit:<6.2f} | {order.quant:<8} | {order.filledQuant:<6} | {order.status:<9} |\n"
                terminal.insert('end', formatted_order)
            for order in orders['sell']:
                formatted_order = f"| {order.ticker:<6} | {order.trader:<7} | "
                terminal.insert('end', formatted_order)
                terminal.insert('end', 'sell', 'sell')
                formatted_order = f" | ${order.limit:<6.2f} | {order.quant:<8} | {order.filledQuant:<6} | {order.status:<9} |\n"
                terminal.insert('end', formatted_order)
        else:
            terminal.insert('end', "No orders found for this ticker.\n")
        terminal.configure(state='disabled')
        # Hide the loading label once loading is done
        loading_label.grid_forget()
    
    # Populate tickerMap if needed
    if ticker not in tickerMap:
        populateTickerMap([ticker], tickerMap)
    
    display_order_book()

# Display the main CLOB page
showClobPage()

# Run the Tkinter event loop
root.mainloop()
