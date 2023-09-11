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
    params = {"identity": email, "nonce": int(time.time() * 1000)}

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

    # combine endpoint with baseUrl
    endpoint = "/accounts/balance"
    complete_url = baseUrl + endpoint

    # send http request to server
    response = send_request(method="GET", url=complete_url, headers=headers)
    if response is not None:
        print("Account balance:", json.dumps(response, indent=2))
    else:
        print("Request failed.")


if __name__ == "__main__":
    main()
