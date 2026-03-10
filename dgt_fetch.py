from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

driver.get("https://info.dgtbusan.com/DGT/esvc/vessel/berthScheduleG")

time.sleep(5)

text = driver.find_element("tag name","body").text
driver.quit()

lines = text.split("\n")

ships = []

for i in range(len(lines)):

    line = lines[i].strip()

    # 선박 코드 패턴
    if re.match(r"[A-Z]{4}\d{3}", line):

        ship = line

        work = ""
        eta = ""
        etd = ""

        for j in range(i+1, min(i+6, len(lines))):

            if "[" in lines[j]:
                work = lines[j]

        if i+4 < len(lines):
            eta = lines[i+3]
            etd = lines[i+4]

        ships.append({
            "ship": ship,
            "work": work,
            "eta": eta,
            "etd": etd
        })

print("=== 발견된 선박 ===")

for s in ships[:10]:
    print(s)

    print("\n=== 선석 작업현황 ===")

berths = ["B1","B2","B3","B4"]

for i,b in enumerate(berths):

    if i < len(ships):

        ship = ships[i]

        name = ship["ship"].split()[0]

        work = ship["work"].replace("[","").replace("]","").split("/")

        discharge = work[0]
        load = work[1]

        print(f"{b} | {name}")
        print(f"   양하 {discharge} / 적하 {load}")

    else:
        print(f"{b} | 대기중")