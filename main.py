import requests
import time

url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

while True:
    try:
        response = requests.get(url)
        data = response.json()
        if "data" in data and "amount" in data["data"]:
            print("سعر البتكوين الحالي بالدولار:", data["data"]["amount"])
        else:
            print("😢 السعر على الحصول عذرا")
    except Exception as e:
        print("حدث خطأ:", e)

    time.sleep(60)
    
