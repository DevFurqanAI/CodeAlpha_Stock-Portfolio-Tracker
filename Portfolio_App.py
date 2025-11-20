import csv

class StockMarket:
    """Static stock market with hardcoded prices."""
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2800,
        "AMZN": 3300,
        "MSFT": 300
    }

    @classmethod
    def is_valid_stock(cls, stock_symbol):
        """Check if the stock symbol is valid."""
        return stock_symbol in cls.stock_prices
    
    @classmethod
    def get_stock_price(cls, stock_symbol):
        """Get the price of the stock."""
        return cls.stock_prices.get(stock_symbol, 0)


class Portfolio:
    """Represents a stock portfolio."""
    def __init__(self):
        self.stocks = {}
        
    def add_stock(self, stock_symbol, quantity):
        """Add stocks to the portfolio."""
        self.stocks[stock_symbol] = self.stocks.get(stock_symbol, 0) + quantity
    
    def total_value(self):
        """Calculate the total value of the portfolio."""
        return sum(StockMarket.get_stock_price(s) * q for s, q in self.stocks.items())
    
    def show_summary(self):
        """Display the portfolio summary."""
        print("\n📊 Portfolio Summary:")
        for stock, quantity in self.stocks.items():
            price = StockMarket.get_stock_price(stock)
            print(f"{stock}: {quantity} shares | Price: ${price} | Total: ${price * quantity}")
        print(f"\n💰 Total Investment: ${self.total_value()}\n")
        
    def save_to_txt(self, filename="portfolio.txt"):
        """Save the portfolio summary to a text file."""
        try:
            with open(filename, "w") as file:
                file.write("Portfolio Summary:\n")
                for stock, quantity in self.stocks.items():
                    price = StockMarket.get_stock_price(stock)
                    file.write(f"{stock}: {quantity} shares | Price: ${price} | Total: ${price * quantity}\n")
                file.write(f"\nTotal Investment: ${self.total_value()}\n")
            print(f"💾 Saved to {filename}")
        except Exception as e:
            print(f"⚠ Error saving to TXT: {e}")
            
    def save_to_csv(self, filename="portfolio.csv"):
        """Save the portfolio summary to a CSV file."""
        try:
            with open(filename, "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Stock Symbol", "Quantity", "Price per Share", "Total Value"])
                for stock, quantity in self.stocks.items():
                    writer.writerow([stock, quantity, StockMarket.get_stock_price(stock), StockMarket.get_stock_price(stock) * quantity])
                writer.writerow(["Total Investment", "", "", self.total_value()])
            print(f"💾 Saved to {filename}")
        except Exception as e:
            print(f"⚠ Error saving to CSV: {e}")


class PortfolioApp:
    """Handles user input and application flow."""
    def __init__(self):
        self.portfolio = Portfolio()

    def run(self):
        print("📈 Stock Portfolio Tracker (OOP Version)")
        print("Available stocks:", ", ".join(StockMarket.stock_prices.keys()))
        print("Type 'done' when finished.\n")

        while True:
            stock = input("Enter stock symbol: ").upper().strip()

            if stock == "DONE":
                break

            if not StockMarket.is_valid_stock(stock):
                print("❌ Stock not found! Available options:", ", ".join(StockMarket.stock_prices.keys()), "\n")
                continue

            try:
                quantity = int(input(f"Enter quantity of {stock}: "))
                if quantity <= 0:
                    print("❌ Quantity must be greater than zero.\n")
                    continue
            except ValueError:
                print("❌ Invalid number!\n")
                continue

            self.portfolio.add_stock(stock, quantity)
            investment = StockMarket.get_stock_price(stock) * quantity
            print(f"✅ Added {quantity} shares of {stock} worth ${investment}")
            print(f"📊 Current Portfolio Value: ${self.portfolio.total_value()}\n")

        # Empty portfolio case
        if not self.portfolio.stocks:
            print("\n⚠ No stocks added. Portfolio empty.")
            return

        # Summary
        self.portfolio.show_summary()

        # Save?
        save = input("Save results? (txt/csv/no): ").lower().strip()
        if save == "txt":
            self.portfolio.save_to_txt()
        elif save == "csv":
            self.portfolio.save_to_csv()
        else:
            print("❌ Not saved.")


# Run App
if __name__ == "__main__":
    app = PortfolioApp()
    app.run()
