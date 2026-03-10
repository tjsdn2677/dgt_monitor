import requests
import re

def get_ships():

    url = "https://info.dgtbusan.com/DGT/esvc/vessel/berthScheduleG"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=10)

    html = r.text

    ships = re.findall(r'[A-Z]{4}\d{3}', html)

    result = []

    berths = ["B1","B2","B3","B4"]

    for i, b in enumerate(berths):

        if i < len(ships):
            result.append(f"{b} | {ships[i]}")
        else:
            result.append(f"{b} | 대기중")

    return result