# Importing required library for visualization
import matplotlib.pyplot as plt

# Step 1: Store Stock Prices in a List (Array in Python)
# Example: Store daily closing prices for a stock (in dollars)
stock_prices = [150.25, 153.30, 157.00, 159.50, 155.00, 160.10, 158.25, 162.40, 163.50, 164.75, 167.00, 169.50]

# Step 2: Analyze Stock Trends
# Check if the stock price is increasing or decreasing
def analyze_trends(prices):
    trends = []
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            trends.append('Increase')
        elif prices[i] < prices[i-1]:
            trends.append('Decrease')
        else:
            trends.append('No Change')
    return trends

trends = analyze_trends(stock_prices)

# Step 3: Calculate Moving Averages (Simple Moving Average - SMA)
def calculate_sma(prices, window=3):
    sma_values = []
    for i in range(len(prices) - window + 1):
        sma = sum(prices[i:i+window]) / window
        sma_values.append(sma)
    return sma_values

sma = calculate_sma(stock_prices, window=3)  # Using a 3-day SMA

# Step 4: Identify Highest and Lowest Stock Prices
highest_price = max(stock_prices)
lowest_price = min(stock_prices)

# Step 5: Compute Daily Price Changes
def compute_daily_changes(prices):
    daily_changes = []
    for i in range(1, len(prices)):
        change = prices[i] - prices[i-1]
        daily_changes.append(change)
    return daily_changes

daily_changes = compute_daily_changes(stock_prices)

# Step 6: Calculate Stock Volatility (Standard Deviation of Price Changes)
def calculate_volatility(changes):
    mean_change = sum(changes) / len(changes)
    variance = sum((x - mean_change) ** 2 for x in changes) / len(changes)
    volatility = variance ** 0.5  # Standard deviation
    return volatility

volatility = calculate_volatility(daily_changes)

# Step 7: Visualize Stock Trends and Data
plt.figure(figsize=(10, 6))
plt.plot(stock_prices, label='Stock Prices', color='blue', marker='o')
plt.plot(range(2, len(stock_prices)-1), sma, label='3-Day SMA', color='red')
plt.title('Stock Prices and 3-Day Simple Moving Average')
plt.xlabel('Days')
plt.ylabel('Price ($)')
plt.legend(loc='best')
plt.grid(True)
plt.show()

# Step 8: Displaying Results
print(f"Highest Stock Price: {highest_price}")
print(f"Lowest Stock Price: {lowest_price}")
print(f"Stock Volatility (Standard Deviation): {volatility}")
print(f"First 5 Daily Price Changes: {daily_changes[:5]}")

 Display Trend Information
print("\nStock Price Trends:")
for i in range(1, len(stock_prices)):
    print(f"Day {i}: {trends[i-1]}")


OUTPUT:
Highest Stock Price: 169.5
Lowest Stock Price: 150.25
Stock Volatility (Standard Deviation): 2.637922736479664
First 5 Daily Price Changes: [3.0500000000000114, 3.6999999999999886, 2.5, -4.5, 5.099999999999994]

Stock Price Trends:
Day 1: Increase
Day 2: Increase
Day 3: Increase
Day 4: Decrease
Day 5: Increase
Day 6: Decrease
Day 7: Increase
Day 8: Increase
Day 9: Increase
Day 10: Increase
Day 11: Increase


