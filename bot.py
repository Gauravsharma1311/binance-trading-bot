from binance.client import Client
from binance.enums import ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT, SIDE_BUY, SIDE_SELL, TIME_IN_FORCE_GTC
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, base_url):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = base_url
        logging.info("Bot initialized with testnet")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market order: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit order: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing limit order: {e}")
            return None
