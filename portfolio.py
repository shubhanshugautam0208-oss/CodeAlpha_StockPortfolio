# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")
print("")

print("Available stock are:")
print("1:AAPL") 
print("2:TSLA") 
print("3:GOOGL") 
print("3:MSFT") 
print("4:AMZN") 

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from:")
        print(", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Stock price:", stock_prices[stock])
        print("Investment value:", investment)

    except ValueError:
        print("Please enter a valid number.")

print("\n================================")
print("Total Investment:", total_investment)
print("================================")

# Save portfolio result to a text file
with open("portfolio_report.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n")
    file.write(f"Total Investment: {total_investment}\n")

print("\nPortfolio report saved as portfolio_report.txt")