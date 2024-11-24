import requests

import requests

API_URL = "https://api.bullmarket.com"  # Replace with actual endpoint
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(f"{API_URL}/account", headers=headers)
if response.status_code == 200:
    print("Account Info:", response.json())
else:
    print("Error:", response.status_code, response.text)




API_KEY = 'your_api_key_here'
BASE_URL = 'https://api.bullmarket.com/'  # Replace with actual endpoint

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

response = requests.get(BASE_URL + 'account', headers=headers)
if response.status_code == 200:
    print("Account Info:", response.json())
else:
    print("Error:", response.status_code, response.text)


order_data = {
    "symbol": "GGAL",  # Example: Stock ticker
    "quantity": 10,
    "price": 500.0,
    "side": "buy"  # 'buy' or 'sell'
}
response = requests.post(BASE_URL + 'orders', json=order_data, headers=headers)
print(response.json())


# Step 5: Backtesting

#     Use historical data to validate your strategy.
#     Example libraries:
#         Python: Backtrader, Zipline.

