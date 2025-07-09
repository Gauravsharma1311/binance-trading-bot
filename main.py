from config import API_KEY, API_SECRET, BASE_URL
from bot import BasicBot
from utils import setup_logger

setup_logger()

bot = BasicBot(API_KEY, API_SECRET, BASE_URL)

print("== Welcome to Binance Testnet Bot ==")
symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
order_type = input("Market or Limit? ").strip().lower()
side = input("Side (BUY/SELL): ").strip().upper()
quantity = float(input("Quantity: "))

if order_type == "market":
    bot.place_market_order(symbol, side, quantity)
elif order_type == "limit":
    price = input("Limit Price: ")
    bot.place_limit_order(symbol, side, quantity, price)
else:
    print("Invalid order type")
