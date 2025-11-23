<p align="center"> <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"> <img src="https://img.shields.io/badge/Category-Finance Tool-orange?style=for-the-badge"> </p>

## Stock Portfolio Tracker
A clean, object-oriented Stock Portfolio Tracker built in Python using class-based design, input validation, and optional file export support.
Perfect for beginners learning OOP or anyone who wants a simple stock investment calculator.

## ✨ Key Features
- 🏷️ Hardcoded stock price dictionary (AAPL, TSLA, GOOGL, etc.)

- ➕ Add multiple stocks with quantities

- 💵 Calculates total investment value in real time
 
- 📊 Displays a complete portfolio summary

- 🧠 Input validation (valid symbols, positive quantities only)

- 💾 Save results to .txt or .csv

- 🧱 Clean Object-Oriented structure:
  - StockMarket class → price lookup

  - Portfolio class → investments & summary

  - PortfolioApp class → application flow


## 📁 Project Files
```bash
Portfolio_App.py   # Main OOP implementation and program entry point
README.md          # Project documentation
```

## 🚀 Getting Started

### 1. Install Python
Ensure Python 3.x is installed.
Check using:

```bash
python --version
```

### 2. Run the Program
```bash
python Portfolio_App.py
```

### 3. Use the Tracker
- Enter valid stock symbols

- Enter quantity

- Type done when finished

- Choose whether to save your results

## 📈 Portfolio Overview
- Each stock has a fixed, hardcoded price

- Total investment = ```price × quantity```

- Multiple stocks can be added

- At completion:

  - 📊 A full summary is displayed

  - 💾 User can save results to TXT or CSV

## 🧱 Code Structure (OOP)
| Class / Method      | Purpose                                     |
| ------------------- | ------------------------------------------- |
| **StockMarket**     | Stores static stock prices and lookup tools |
| `is_valid_stock()`  | Validates stock symbol                      |
| `get_stock_price()` | Returns stock price                         |
| **Portfolio**       | Represents user’s investment portfolio      |
| `add_stock()`       | Adds or updates quantity                    |
| `total_value()`     | Calculates total investment                 |
| `show_summary()`    | Prints full portfolio summary               |
| `save_to_txt()`     | Exports summary to a text file              |
| `save_to_csv()`     | Exports summary to a CSV file               |
| **PortfolioApp**    | Handles user input and app flow             |
| `run()`             | Main execution loop                         |


## 🧾 Example Output (Preview)
```yaml
📈 Stock Portfolio Tracker (OOP Version)
Available stocks: AAPL, TSLA, GOOGL, AMZN, MSFT

Enter stock symbol: AAPL
Enter quantity of AAPL: 5
✅ Added 5 shares of AAPL worth $900
📊 Current Portfolio Value: $900

Enter stock symbol: TSLA
Enter quantity of TSLA: 2
✅ Added 2 shares of TSLA worth $500
📊 Current Portfolio Value: $1400
```

Final Summary Example:
```yaml
📊 Portfolio Summary:
AAPL: 5 shares | Price: $180 | Total: $900
TSLA: 2 shares | Price: $250 | Total: $500

💰 Total Investment: $1400
```

## 🧰 Customization
🔹 Add more stock prices
```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "NVDA": 420,
    "META": 300
}
```
🔹 Change default export filenames
```python
portfolio.save_to_txt("my_portfolio_report.txt")
portfolio.save_to_csv("investment.csv")
```

## 📊 Sample Hardcoded Stock Prices (Default)
```python
{
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300,
    "MSFT": 300
}
```

## 🤝 Contributing
Enhance this project by adding features like:

- Live API stock prices

- Graphical charts

- GUI (Tkinter / PyQt)

- Historical tracking


## 📜 License
This project is free to use, modify, and share.
