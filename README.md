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

- **initializeTicker**: Initializes a ticker in the ticker map.
- **populateTickerMap**: Populates the ticker map with initial data for each ticker.
- **populateLists**: Populates the buy and sell lists for a given ticker with initial orders.
- **isMatch**: Checks if a buy order matches a sell order.
- **matchBuy**: Matches a buy order with sell orders.
- **matchSell**: Matches a sell order with buy orders.
- **addOrder**: Adds a new order to the ticker map and matches it against existing orders.
- **printOrders**: Prints the buy and sell orders in a formatted table.

## Frontend (UI.py)

The frontend provides a user-friendly GUI for interacting with the order book. It includes:

- A main page with buttons for different stocks and a search bar.
- A ticker page where users can view and place orders for a specific stock.
- A terminal-like widget to display the order book.

### Key Components

- **showClobPage**: Displays the main page with stock buttons and a search bar.
- **showTickerPage**: Displays the ticker page with order entry, search, and terminal-like output.
- **removeAllWidgets**: Removes all child widgets from a given parent widget.
- **display_order_book**: Updates the terminal-like widget to show the current order book for the selected ticker.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter
- YahooQuery

### Installation

1. Clone the repository:
   git clone https://github.com/yourusername/clob-trading-app.git
   cd clob-trading-app

2. Install the required packages:
   pip install yahooquery

### Running the Application

1. Start the application by running the frontend script:
   python UI.py

2. Interact with the application through the GUI.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [YahooQuery](https://github.com/dpguthrie/yahooquery) for fetching stock prices.
- Tkinter for providing the GUI framework.

### Explanation

- **Project Structure**: Describes the overall structure of the project and the purpose of each file.
- **Backend (Driver.py)**: Details the responsibilities of the backend and lists key functions with brief descriptions.
- **Frontend (UI.py)**: Describes the components of the frontend and lists key components with brief descriptions.
- **Getting Started**: Provides instructions on prerequisites, installation, and how to run the application.
- **Example Usage**: Briefly explains how to use the application.
- **License**: Mentions the project license.
- **Acknowledgements**: Credits any third-party tools or libraries used in the project.
