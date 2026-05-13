import csv
from datetime import datetime

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 140.00,
    "AMZN": 145.00
}

def get_user_portfolio():
    """Get stock names and quantities from user"""
    portfolio = {}
    
    print("\n=== STOCK TRACKER ===")
    print("Available stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price:.2f}")
    
    print("\nEnter stocks (press Enter on empty symbol to finish):")
    
    while True:
        symbol = input("\nStock symbol: ").upper().strip()
        
        if not symbol:
            break
        
        if symbol not in STOCK_PRICES:
            print(f"Invalid symbol. Choose from: {', '.join(STOCK_PRICES.keys())}")
            continue
        
        try:
            quantity = float(input(f"Quantity of {symbol}: "))
            if quantity <= 0:
                print("Quantity must be positive")
                continue
            portfolio[symbol] = quantity
        except ValueError:
            print("Please enter a valid number")
    
    return portfolio

def calculate_total(portfolio):
    """Calculate total investment value"""
    total = 0
    details = []
    
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = quantity * price
        total += value
        details.append({
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'value': value
        })
    
    return total, details

def display_results(total, details):
    """Display investment summary"""
    print("\n" + "="*55)
    print("INVESTMENT SUMMARY")
    print("="*55)
    print(f"{'Symbol':<10} {'Quantity':<12} {'Price':<10} {'Value':<15}")
    print("-"*55)
    
    for item in details:
        print(f"{item['symbol']:<10} {item['quantity']:<12.2f} ${item['price']:<9.2f} ${item['value']:<14.2f}")
    
    print("-"*55)
    print(f"{'TOTAL INVESTMENT':<33} ${total:<14.2f}")
    print("="*55)

def save_to_file(total, details):
    """Save results to CSV or TXT file"""
    choice = input("\nSave results? (csv/txt/no): ").lower().strip()
    
    if choice == 'no':
        print("Results not saved")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if choice == 'csv':
        filename = f"stock_report_{timestamp}.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Symbol', 'Quantity', 'Price', 'Value'])
            for item in details:
                writer.writerow([item['symbol'], item['quantity'], f"${item['price']:.2f}", f"${item['value']:.2f}"])
            writer.writerow([])
            writer.writerow(['TOTAL', '', '', f"${total:.2f}"])
            writer.writerow(['Date', datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        print(f"✅ Saved to {filename}")
    
    elif choice == 'txt':
        filename = f"stock_report_{timestamp}.txt"
        with open(filename, 'w') as f:
            f.write("STOCK INVESTMENT REPORT\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*50 + "\n\n")
            f.write(f"{'Symbol':<10} {'Quantity':<12} {'Price':<10} {'Value':<15}\n")
            f.write("-"*50 + "\n")
            for item in details:
                f.write(f"{item['symbol']:<10} {item['quantity']:<12.2f} ${item['price']:<9.2f} ${item['value']:<14.2f}\n")
            f.write("-"*50 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total:.2f}\n")
        print(f"✅ Saved to {filename}")
    
    else:
        print("Invalid choice. Results not saved")

def main():
    """Main program"""
    portfolio = get_user_portfolio()
    
    if not portfolio:
        print("\nNo stocks entered. Exiting...")
        return
    
    total, details = calculate_total(portfolio)
    display_results(total, details)
    save_to_file(total, details)
    
    print("\nThank you for using Stock Tracker!")

if __name__ == "__main__":
    main()