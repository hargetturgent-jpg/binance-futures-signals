import requests

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

response = requests.get(url)
data = response.json()

# بعض الردود من API ترجع قائمة، لذا نتأكد
if isinstance(data, dict) and "price" in data:
    print("سعر البتكوين الحالي بالدولار:", data["price"])
else:
    print("تعذر الحصول على السعر 😢")
  
