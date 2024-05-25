# IN PROGRESS / EXPERIMENTAL
import tkinter as tk
from tkinter import *
from Driver import Scraper, tickerMap, populateTickerMap, addOrder, printOrders

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting up Initial Things
        self.title("CLOB")
        self.geometry("720x550")
        self.resizable(True, True)
        self.iconphoto(False, tk.PhotoImage(file="iconbook.png"))

        # Creating a container
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize Frames
        self.frames = {}
        self.HomePage = HomePage
        self.Validation = Validation
        self.TickerPage = TickerPage

        # Defining Frames and Packing it
        for F in {HomePage, Validation, TickerPage}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = frame.create_menubar(self)
        self.configure(menu=menubar)
        frame.tkraise()

    def show_ticker_page(self, ticker):
        ticker_page = self.frames[TickerPage]
        ticker_page.update_page(ticker)
        self.show_frame(TickerPage)

    def about(self):
        messagebox.showinfo("About", "This is the CLOB application.")


class HomePage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Home Page", font=('Times', '20'))
        label.pack(pady=10, padx=10)

        self.create_stock_buttons(parent)
        self.create_search_frame(parent)

    def create_stock_buttons(self, parent):
        btnFrame = tk.Frame(self)
        btnFrame.pack()

        appleBtntext = 'AAPL\nApple Inc.\n$%.2f' % (Scraper.get_stock_price('AAPL'))
        appleBtn = tk.Button(btnFrame, text=appleBtntext, bd=10, command=lambda: parent.show_ticker_page('AAPL'))
        appleBtn.pack(side=LEFT, padx=5, pady=5)

        googleBtntext = 'GOOG\nAlphabet Inc. C\n$%.2f' % (Scraper.get_stock_price('GOOG'))
        googleBtn = tk.Button(btnFrame, text=googleBtntext, bd=10, command=lambda: parent.show_ticker_page('GOOG'))
        googleBtn.pack(side=LEFT, padx=5, pady=5)

        nvidiaBtntext = 'NVDA\nNVIDIA Corp.\n$%.2f' % (Scraper.get_stock_price('NVDA'))
        nvidiaBtn = tk.Button(btnFrame, text=nvidiaBtntext, bd=10, command=lambda: parent.show_ticker_page('NVDA'))
        nvidiaBtn.pack(side=LEFT, padx=5, pady=5)

        teslaBtntext = 'TSLA\nTesla Inc.\n$%.2f' % (Scraper.get_stock_price('TSLA'))
        teslaBtn = tk.Button(btnFrame, text=teslaBtntext, bd=10, command=lambda: parent.show_ticker_page('TSLA'))
        teslaBtn.pack(side=LEFT, padx=5, pady=5)

        self.grid_columnconfigure(0, weight=1)  # Make the buttons fill available space

    def create_search_frame(self, parent):
        searchFrame = tk.Frame(self)
        searchFrame.pack(side=TOP, padx=10, pady=10)

        searchLabel = tk.Label(searchFrame, text='Search', fg='#87CEEB')
        searchLabel.pack(side=LEFT)

        searchEntry = tk.Entry(searchFrame)
        searchEntry.insert(0, 'ex. BGC')

        def onEntryKey(event):
            if searchEntry.get() == 'ex. BGC':
                searchEntry.delete(0, END)  # Clear placeholder text when user starts typing

        def onEntryLeave(event):
            if not searchEntry.get():
                searchEntry.insert(0, 'ex. BGC')  # Restore placeholder text if Entry widget is left empty

        def onReturn(event):
            parent.show_ticker_page(searchEntry.get())  # Pass the text from the Entry widget to showTickerPage

        searchEntry.bind("<Key>", onEntryKey)
        searchEntry.bind("<FocusOut>", onEntryLeave)
        searchEntry.bind('<Return>', onReturn)

        searchEntry.pack(side=LEFT, fill=X, padx=5)

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project", command=lambda: parent.show_frame(parent.Validation))
        filemenu.add_command(label="Close", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)

        # Processing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="Validate")
        processing_menu.add_separator()

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=parent.about)
        help_menu.add_separator()

        return menubar


class Validation(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Validation Page", font=('Times', '20'))
        label.pack(pady=0, padx=0)

        # ADD CODE HERE TO DESIGN THIS PAGE

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project", command=lambda: parent.show_frame(parent.Validation))
        filemenu.add_command(label="Close", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)

        # Processing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=parent.about)
        help_menu.add_separator()

        return menubar


class TickerPage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)
        self.terminal = tk.Text(self, wrap='word')
        self.terminal.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(self, command=self.terminal.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.terminal.configure(yscrollcommand=self.scrollbar.set)

    def update_page(self, ticker):
        self.terminal.configure(state='normal')
        self.terminal.delete('1.0', END)
        self.master.title(ticker)  # Use self.master here because self.master is the App instance

        # Populate tickerMap if needed
        if ticker not in tickerMap:
            populateTickerMap([ticker], tickerMap)

        orders = tickerMap[ticker]
        order_text = f"Orders for {ticker}:\n"
        order_text += "\nBuy Orders:\n"
        for order in orders['buy']:
            order_text += f"{order}\n"

        order_text += "\nSell Orders:\n"
        for order in orders['sell']:
            order_text += f"{order}\n"

        self.terminal.insert('1.0', order_text)
        self.terminal.configure(state='disabled')

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project", command=lambda: parent.show_frame(parent.Validation))
        filemenu.add_command(label="Close", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)

        # Processing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=parent.about)
        help_menu.add_separator()

        return menubar


if __name__ == "__main__":
    app = App()
    app.mainloop()
