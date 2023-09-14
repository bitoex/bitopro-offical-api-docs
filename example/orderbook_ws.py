# -*- coding: utf-8 -*-
import json
import threading
import time
from loguru import logger
import websocket

class BitoproOrderbookWs():
    def __init__(self, symbols_limit: dict, callback):
        self._connect_endpoint: str = "wss://stream.bitopro.com:443/ws/v1/pub/order-books/"
        for symbol, limit in symbols_limit.items():
            self._connect_endpoint = self._connect_endpoint + f"{str.lower(symbol)}:{limit},"
        self._connect_endpoint = self._connect_endpoint[:-1]  # remove last ','

        self.callback = callback 

        self._ws: websocket.WebSocketApp = None
        self.wst: threading.Thread = None
        
    def init_websocket(self):
        ws_headers = None

        self._ws = websocket.WebSocketApp(
            self._connect_endpoint,
            on_message=lambda ws, msg:self._on_message(ws, msg),
            on_close=lambda ws, status_code, msg: self._on_close(ws, status_code, msg),
            on_error=lambda ws, error:self._on_error(ws, error),
            on_open=lambda ws: self._on_open(ws),
            header=ws_headers
        )
        self.wst = threading.Thread(target=self._ws.run_forever)

    def start(self):
        if self.wst != None:
            self.wst.start()

    def _on_open(self, ws):
        logger.debug(f"{self.__class__.__name__} connected")

    def _on_message(self, ws, message):
        self.callback(message)

    def _on_close(self, ws, close_status_code, msg):
        self.init_websocket()
        log_message = f"{self._connect_endpoint} closed connection, reconnecting...\n"
        logger.info(log_message)
        time.sleep(3)
        self.wst.start()

    def _on_error(self, ws, error):
        logger.error(error)

def websocket_handler(message:str):
    reply = json.loads(message)
    print("ORDER_BOOK: ", reply, end="\n\n")

# run pip install websocket_client before executing script
if __name__ == "__main__":
    symbols_list = {"eth_btc": 5, "BTC_TWD": 1, "ETH_TWD": 20, "BITO_ETH": 1}
    bito_websocket_user_balance = BitoproOrderbookWs(symbols_list, websocket_handler)
    bito_websocket_user_balance.init_websocket()
    bito_websocket_user_balance.start()