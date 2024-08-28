from datetime import datetime as dt
import requests
from bs4 import BeautifulSoup 
from function_def import read_raceresult_data



START_DATE = "2024-08-26"

date = dt.strptime(START_DATE, '%Y-%m-%d')

Racenumber = "5"
Coursenumber = "05"


# 結果データを取得
url = f"https://www.boatrace.jp/owpc/pc/race/raceresult?rno={Racenumber}&jcd={Coursenumber}&hd={date.strftime('%Y%m%d')}"
response = requests.get(url)
response.encoding = response.apparent_encoding
bs = BeautifulSoup(response.text, 'html.parser')

df = read_raceresult_data(bs)

print(df)