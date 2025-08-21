stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 145,
    "AMZN": 130
}

portfolio = {}

print("Enter your stock holdings (type 'done' to finish):")
while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not in our price list. Try again.")
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = qty
    except ValueError:
        print("Invalid quantity. Enter a number.")

total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} x ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

save = input("Save portfolio to file? (yes/no): ").lower()
if save == "yes":
    filetype = input("Enter filename type (.txt or .csv): ").lower()
    filename = f"portfolio{filetype}"
    with open(filename, "w") as f:
        if filetype == ".txt":
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} x ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
        elif filetype == ".csv":
            f.write("Stock,Quantity,Price,Investment\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock]*qty}\n")
            f.write(f"Total,,,{total_investment}\n")
    print(f"Portfolio saved to {filename}")
else:
    print("Portfolio not saved.")