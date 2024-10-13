from function_def import read_raceresult_data
import datetime as dt
import os


# 開始日と終了日を指定(YYYY-MM-DD)
START_DATE = "2022-11-01"
END_DATE = "2023-10-31"

start_date = dt.strptime(START_DATE, '%Y-%m-%d')
end_date = dt.strptime(END_DATE, '%Y-%m-%d')

date_dif = (end_date - start_date).days + 1



# 出走表データを取得
for i in range(date_dif):
    current_date = start_date + td(days=i)
    for j in range(12):
        if not os.path.exists(f"data_crawling/racelist/{current_date.strftime('%Y%m%d')}_{(j + 1):02d}R"):
        # 日付とレース番号を含めたURLを構築
            url = f"https://www.boatrace.jp/owpc/pc/race/racelist?rno={j + 1}&jcd=05&hd={current_date.strftime('%Y%m%d')}"
        
        # URLからデータを取得
            response = requests.get(url)
            time.sleep(1)
            response.encoding = response.apparent_encoding
            bs = BeautifulSoup(response.text, 'html.parser')
        # データの保存
            with open(f"data_crawling/racelist/{current_date.strftime('%Y%m%d')}_{(j + 1):02d}R", 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"{current_date.strftime('%Y-%m-%d')}_{(j + 1):02d}Rの出走表データを保存しました")
    


    
# 直前情報データを取得
for i in range(date_dif):
    current_date = start_date + td(days=i)
    for j in range(12):
        if not os.path.exists(f"data_crawling/beforeinfo/{current_date.strftime('%Y%m%d')}_{(j + 1):02d}R"):
        # 日付とレース番号を含めたURLを構築
            url = f"https://www.boatrace.jp/owpc/pc/race/beforeinfo?rno={j + 1}&jcd=05&hd={current_date.strftime('%Y%m%d')}"
        
        # URLからデータを取得
            response = requests.get(url)
            time.sleep(1)
            response.encoding = response.apparent_encoding
            bs = BeautifulSoup(response.text, 'html.parser')
        # データの保存
            with open(f"data_crawling/beforeinfo/{current_date.strftime('%Y%m%d')}_{(j + 1):02d}R", 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"{current_date.strftime('%Y-%m-%d')}_{(j + 1):02d}Rの直前情報データを保存しました")




# 結果データを取得
for i in range(date_dif):
    current_date = start_date + td(days=i)
    for j in range(12):
        if not os.path.exists(f"data_crawling/raceresult/{current_date.strftime('%Y%m%d')}_{(j + 1):02d}R"):
        # 日付とレース番号を含めたURLを構築
            url = f"https://www.boatrace.jp/owpc/pc/race/raceresult?rno={j + 1}&jcd=05&hd={current_date.strftime('%Y%m%d')}"
        
        # URLからデータを取得
            response = requests.get(url)
            time.sleep(1)
            response.encoding = response.apparent_encoding
            bs = BeautifulSoup(response.text, 'html.parser')
        # データの保存
            with open(f"data_crawling/raceresult/{current_date.strftime('%Y%m%d')}_{(j + 1):02d}R", 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"{current_date.strftime('%Y-%m-%d')}_{(j + 1):02d}Rの結果データを保存しました")
    
    
print("クローニングを完了しました")