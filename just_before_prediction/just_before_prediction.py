from datetime import datetime as dt
import requests
from bs4 import BeautifulSoup 
from function_def import read_raceresult_data, read_racelist_data
import pandas as pd

"""
Index(['レースコード', 'レース場', 'レース回', '天気', '風向', '風速', '波の高さ', '1枠_体重', '1枠_級別',
       '1枠_全国勝率', '1枠_全国2連対率', '1枠_当地勝率', '1枠_当地2連対率', '1枠_モーター2連対率',
       '1枠_ボート2連対率', '2枠_体重', '2枠_級別', '2枠_全国勝率', '2枠_全国2連対率', '2枠_当地勝率',
       '2枠_当地2連対率', '2枠_モーター2連対率', '2枠_ボート2連対率', '3枠_体重', '3枠_級別', '3枠_全国勝率',
       '3枠_全国2連対率', '3枠_当地勝率', '3枠_当地2連対率', '3枠_モーター2連対率', '3枠_ボート2連対率',
       '4枠_体重', '4枠_級別', '4枠_全国勝率', '4枠_全国2連対率', '4枠_当地勝率', '4枠_当地2連対率',
       '4枠_モーター2連対率', '4枠_ボート2連対率', '5枠_体重', '5枠_級別', '5枠_全国勝率', '5枠_全国2連対率',
       '5枠_当地勝率', '5枠_当地2連対率', '5枠_モーター2連対率', '5枠_ボート2連対率', '6枠_体重', '6枠_級別',
       '6枠_全国勝率', '6枠_全国2連対率', '6枠_当地勝率', '6枠_当地2連対率', '6枠_モーター2連対率',
       '6枠_ボート2連対率', '1着_艇番', '1着_展示タイム', '2着_艇番', '2着_展示タイム', '3着_艇番',
       '3着_展示タイム', '4着_艇番', '4着_展示タイム', '5着_艇番', '5着_展示タイム', '6着_艇番',
       '6着_展示タイム'],
      dtype='object')
"""



START_DATE = "2024-08-26"

date = dt.strptime(START_DATE, '%Y-%m-%d')

Racenumber = "5"
Coursenumber = "05"


def fetch_boatrace_data(page_type):
    START_DATE = "2024-08-26"
    date = dt.strptime(START_DATE, '%Y-%m-%d')
    Racenumber = "5"
    Coursenumber = "05"

    url = f"https://www.boatrace.jp/owpc/pc/race/{page_type}?rno={Racenumber}&jcd={Coursenumber}&hd={date.strftime('%Y%m%d')}"
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    bs = BeautifulSoup(response.text, 'html.parser')

    return bs

raceresult = fetch_boatrace_data("raceresult")
racelist = fetch_boatrace_data("racelist")
beforeinfo = fetch_boatrace_data("beforeinfo")


# 結果データを取得
tuple_raceresult = read_raceresult_data(raceresult)
df_raceresult = pd.DataFrame([tuple_raceresult], columns=['温度', '天気', '風向き', '風速', '波の高さ', 'その他の情報'])

print("df_raceresult:", df_raceresult.columns)
print(df_raceresult.head())



# 出走表データを取得
tuple_racelist = read_racelist_data(racelist, raceresult, beforeinfo)
df_racelist = pd.DataFrame([tuple_racelist], columns = [
    '1枠_支部', '2枠_支部', '3枠_支部', '4枠_支部', '5枠_支部', '6枠_支部',
    '1枠_体重', '2枠_体重', '3枠_体重', '4枠_体重', '5枠_体重', '6枠_体重',
    '1枠_F数', '2枠_F数', '3枠_F数', '4枠_F数', '5枠_F数', '6枠_F数',
    '1枠_L数', '2枠_L数', '3枠_L数', '4枠_L数', '5枠_L数', '6枠_L数',
    '1枠_平均ST', '2枠_平均ST', '3枠_平均ST', '4枠_平均ST', '5枠_平均ST', '6枠_平均ST',
    '1枠_全国勝率', '2枠_全国勝率', '3枠_全国勝率', '4枠_全国勝率', '5枠_全国勝率', '6枠_全国勝率',
    '1枠_当地勝率', '2枠_当地勝率', '3枠_当地勝率', '4枠_当地勝率', '5枠_当地勝率', '6枠_当地勝率',
    '1枠_モーター2連対率', '2枠_モーター2連対率', '3枠_モーター2連対率', '4枠_モーター2連対率', '5枠_モーター2連対率', '6枠_モーター2連対率',
    '1枠_モーター3連率', '2枠_モーター3連率', '3枠_モーター3連率', '4枠_モーター3連率', '5枠_モーター3連率', '6枠_モーター3連率',
    '1枠_展示タイム', '2枠_展示タイム', '3枠_展示タイム', '4枠_展示タイム', '5枠_展示タイム', '6枠_展示タイム',
    '1枠_チルト', '2枠_チルト', '3枠_チルト', '4枠_チルト', '5枠_チルト', '6枠_チルト'
])

print("df_racelist:", df_racelist.columns)
print(df_racelist.head())


"""
これから追加

レースコード
レース場
レース回
1枠_級別
1枠_全国2連対率
1枠_当地2連対率
1枠_ボート2連対率
"""