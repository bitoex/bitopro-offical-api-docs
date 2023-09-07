import requests
import json
import hmac
import hashlib
import base64
import time


apiKey = '[Your API key here]'
apiSecret = '[Your API secret here]'
baseUrl = 'https://api.bitopro.com/v3'
email = '[Your account email here]'


def send_request(method, url, headers=None, data=None, timeout=None):
    try:
        session = requests.Session()
        response = None
        if method == "GET":
            response = session.get(url, headers=headers, params=data, timeout=timeout)
        if method == "POST":
            response = session.post(url, headers=headers, json=data, timeout=timeout)
        if method == "DELETE":
            response = session.delete(url, headers=headers, timeout=timeout)

        if response is not None and response.status_code == requests.codes.ok:
            return response.json()
        else:
            return None
    except Exception as ex:
        print(ex)

# execute pip install requests first
def main():
    # generate payload
    # create order request body
    params = {
        "action": "BUY",
        "amount": str(0.0001),
        "price": str(750000),
        "timestamp": int(time.time() * 1000),
        "type": "LIMIT",
        "timeInForce": "POST_ONLY"
    }
    # base64 encode to get payload
    payload = base64.urlsafe_b64encode(json.dumps(params).encode("utf-8")).decode("utf-8")

    # use api secret to get signature
    signature = hmac.new(
        bytes(apiSecret, "utf-8"),
        bytes(payload, "utf-8"),
        hashlib.sha384,
    ).hexdigest()

    # combine these data into an HTTP request header
    headers = {
        "X-BITOPRO-APIKEY": apiKey,
        "X-BITOPRO-PAYLOAD": payload,
        "X-BITOPRO-SIGNATURE": signature,
    }

    pair = "btc_twd"
    # combine endpoint with baseUrl
    endpoint = f"/orders/{pair}"
    complete_url = baseUrl + endpoint

    # send http request to server
    response = send_request(method="POST", url=complete_url, headers=headers, data=params)
    if response is not None:
        print("Order created:", json.dumps(response, indent=2))
    else:
        print("Failed to create order.")


if __name__ == "__main__":
    main()
