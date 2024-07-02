# CLOB Trading Application

This project is a Client Limit Order Book (CLOB) trading application. The application allows users to view and place buy and sell orders for various stocks. The project is divided into a backend (Driver.py) and a frontend (UI.py).

## Project Structure

- **Driver.py**: This is the backend of the application. It contains the logic for managing orders, matching buy and sell orders, and maintaining the order book.
- **UI.py**: This is the frontend of the application. It provides a graphical user interface (GUI) for users to interact with the order book, place orders, and view stock information.

## Backend (Driver.py)

The backend is responsible for:

- Initializing tickers and populating them with initial orders.
- Matching buy and sell orders.
- Managing the order book and removing completed orders.
- Printing the order book in a formatted manner.

### Key Functions

- **populateTickerMap**: Populates the ticker dictionary with initial data for each ticker.
- **populateLists**: Populates the buy and sell lists for a given ticker with initial orders.
- **matchBuy**: Matches a buy order with sell orders.
- **matchSell**: Matches a sell order with buy orders.
- **addOrder**: Adds a new order to the ticker map and matches it against existing orders.

## Frontend (UI.py)

The frontend provides a user-friendly GUI for interacting with the order book. It includes:

- A main page with buttons for different stocks and a search bar.
- A ticker page where users can view and place orders for a specific stock.
- A terminal-like widget to display the order book.

### Key Components

- **showClobPage**: Displays the main page with stock buttons and a search bar.
- **showTickerPage**: Displays the ticker page with order entry, search, and terminal-like output.

## Getting Started

### Prerequisites

- Python 3.x (any minor version within the 3 series is acceptable)
- Tkinter
- YahooQuery

### Installation

1. Clone the repository:
   ``` bash
   git clone https://github.com/nohac14/clobPY.git
   ```
   ``` bash
   cd clobPY
   ```
3. Install the required packages:
   ``` bash
   pip install yahooquery
   ```
### Running the Application

1. Start the application by running the frontend script:
   ``` bash
   python UI.py
   ```
3. Interact with the application through the GUI.

## Acknowledgements

- [YahooQuery](https://github.com/dpguthrie/yahooquery) for fetching stock prices.
- Tkinter for providing the GUI framework.
