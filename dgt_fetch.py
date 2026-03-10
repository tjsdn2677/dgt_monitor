import requests
import re

url = "https://info.dgtbusan.com/DGT/esvc/vessel/berthScheduleG"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:

    r = requests.get(url, headers=headers, timeout=10)

    html = r.text

    ships = re.findall(r'[A-Z]{3,5}[0-9]{3}', html)

    berths = ["B1", "B2", "B3", "B4"]

    for i, b in enumerate(berths):

        if i < len(ships):

            print(f"{b} | {ships[i]}")

        else:

            print(f"{b} | 대기중")

except Exception as e:

    print("ERROR:", e)