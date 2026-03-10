import requests
from bs4 import BeautifulSoup

url = "https://info.dgtbusan.com/DGT/esvc/vessel/berthScheduleG"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

ships = soup.find_all("div")

for ship in ships:
    ship_id = ship.get("id")

    if ship_id and ship_id.endswith("_st_time"):
        ship_code = ship_id.replace("_st_time", "")

        hour = ship.get_text().strip()
        time_text = f"{hour}:00"

        print("선박:", ship_code)
        print("시작시간:", time_text)
        print("----------------")