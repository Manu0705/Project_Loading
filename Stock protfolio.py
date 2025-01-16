import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  # A dictionary to hold stock symbol and the quantity owned

    def add_stock(self, symbol, quantity):
        """Add stock to portfolio"""
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol} to the portfolio.")

    def remove_stock(self, symbol, quantity):
        """Remove stock from portfolio"""
        if symbol in self.portfolio and self.portfolio[symbol] >= quantity:
            self.portfolio[symbol] -= quantity
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
            print(f"Removed {quantity} shares of {symbol} from the portfolio.")
        else:
            print(f"Error: Not enough shares of {symbol} to remove or stock not found.")

    def get_current_price(self, symbol):
        """Get the current price of the stock"""
        stock = yf.Ticker(symbol)
        stock_info = stock.history(period="1d")
        if not stock_info.empty:
            return stock_info['Close'][0]
        else:
            print(f"Error: Unable to fetch data for {symbol}.")
            return None

    def show_portfolio(self):
        """Show current portfolio and its total value"""
        total_value = 0
        print("\nCurrent Portfolio:")
        if not self.portfolio:
            print("No stocks in portfolio.")
        else:
            for symbol, quantity in self.portfolio.items():
                current_price = self.get_current_price(symbol)
                if current_price is not None:
                    current_value = current_price * quantity
                    total_value += current_value
                    print(f"{symbol}: {quantity} shares, Current Price: ${current_price:.2f}, Total Value: ${current_value:.2f}")
            print(f"\nTotal Portfolio Value: ${total_value:.2f}")


def main():
    portfolio = StockPortfolio()
    
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':  # Add stock
            symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
            quantity = int(input(f"Enter quantity of {symbol}: "))
            portfolio.add_stock(symbol, quantity)
        
        elif choice == '2':  # Remove stock
            symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
            quantity = int(input(f"Enter quantity of {symbol} to remove: "))
            portfolio.remove_stock(symbol, quantity)
        
        elif choice == '3':  # Show portfolio performance
            portfolio.show_portfolio()
        
        elif choice == '4':  # Exit
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
