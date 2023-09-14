# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import threading
import time
from loguru import logger
import websocket

def get_current_timestamp() -> int:
        return int(time.time() * 1000)


def build_payload(params={}) -> bytes:
    return base64.urlsafe_b64encode(json.dumps(params).encode("utf-8")).decode("utf-8")


def build_headers(api_key:str, api_secret:str, params={}) -> dict:
    signature = hmac.new(bytes(api_secret, "utf-8"), bytes(build_payload(params), "utf-8"), hashlib.sha384,).hexdigest()
    return {
        "X-BITOPRO-APIKEY": api_key,
        "X-BITOPRO-PAYLOAD": build_payload(params),
        "X-BITOPRO-SIGNATURE": signature,
    }

class BitoproUserBlanceWs():
    def __init__(self, account:str, api_key:str, api_secret:str, callback):
        self._connect_endpoint: str = "wss://stream.bitopro.com:443/ws/v1/pub/auth/account-balance"
        self.send_opening_message:str = ""
        self._account:str = account
        self._api_key:str = api_key
        self._api_secret:str = api_secret

        self.callback = callback 

        self._ws: websocket.WebSocketApp = None
        self.wst: threading.Thread = None
        
    def init_websocket(self):
        if self._account and self._api_key and self._api_secret:
            params = {"identity": self._account, "nonce": get_current_timestamp()}
            ws_headers = build_headers(self._api_key, self._api_secret, params=params)
        else:
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
    print("ACCOUNT_BALANCE: ", reply, end="\n\n")

# run pip install websocket_client before executing script
if __name__ == "__main__":
    account = ""
    apiKey = ""
    apiSecret = ""
    bito_websocket_user_balance = BitoproUserBlanceWs(account, apiKey, apiSecret, websocket_handler)
    bito_websocket_user_balance.init_websocket()
    bito_websocket_user_balance.start()