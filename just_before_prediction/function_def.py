from bs4 import BeautifulSoup 
import re


# 出走表データを取得する関数
def read_racelist_data(soup_racelist, soup_beforeinfo):
    # with open(file_path_list, 'r', encoding='utf-8') as file:
    #     file_content = file.read()
    #     soup_racelist = BeautifulSoup(file_content, 'html.parser')
        
    # with open(file_path_beforeinfo, 'r', encoding='utf-8') as file:
    #     file_content = file.read()
    #     soup_beforeinfo = BeautifulSoup(file_content, 'html.parser')

    
    player_rank_list = [] # 級別の追加
    affiliations = [] 
    weights = [] 
    F_number_list = [] 
    L_number_list = [] 
    average_ST_list = []
    national_winning_rate_list = []
    national_2nd_rate_list = [] # 全国2連対率（新たに追加）
    Local_winning_rate_list = []
    Local_2nd_rate_list = [] # 当地2連対率（新たに追加）
    motor_2nd_rate_list = []
    motor_3rd_rate_list = [] 
    boat_2nd_rate_list = [] # ボート2連対率（新たに追加）
    exhibition_time_list = []
    tilt_list = []
    
    # 各枠の情報を取得
    for n in range(6):
        # # 出走表情報
        # frame_result = get_frame_by_course((n+1), soup_raceresult)
        # if frame_result is None:
        #     frame_result = 6  # None の場合には 6 を代入する
        # n_waku = soup_racelist.find_all("tbody", class_="is-fs12")[int(frame_result)-1]
        # playerinfo_elem = n_waku.find_all("div", class_="is-fs11")
        # sibu_elem = playerinfo_elem[1]

        n_waku = soup_racelist.find_all("tbody", class_="is-fs12")[n]
        playerinfo_elem = n_waku.find_all("div", class_="is-fs11")
        number_elem = playerinfo_elem[0]
        sibu_elem = playerinfo_elem[1]
        
        player_race_info_elem = n_waku.find_all("td", class_="is-lineH2", rowspan="4")[0]
        player_info_text = player_race_info_elem.get_text(strip=True)
        
        # # 直前情報（展示タイム、チルト）
        # player_beforeinfo = soup_beforeinfo.find_all("tbody", class_="is-fs12")[int(frame_result)-1]
        player_beforeinfo = soup_beforeinfo.find_all("tbody", class_="is-fs12")[n]

        # 級別の取得
        player_rank_elem = number_elem.find_next("span")
        player_rank = player_rank_elem.text.strip()
        player_rank_list.append(player_rank) 
        
        # 所属情報の取得
        affiliation = sibu_elem.text.split('/')[0].strip()
        affiliations.append(affiliation)
        
        # 体重情報の取得
        weight_base = sibu_elem.text.split('/')[2].strip()
        weight = float(weight_base.replace("kg", ""))
        weights.append(weight)
        
        # F数（フライング数）: F_number取得
        F_number_match = re.search(r'F\d', player_info_text)
        F_number_base = F_number_match.group() if F_number_match else 0.0  # マッチした文字列を取得、なければNone
        F_number = int(F_number_base.replace("F", ""))
        F_number_list.append(F_number)  # F数のリストに追加
        
        # L数（出遅れ数）: L_number取得
        L_number_match = re.search(r'L\d', player_info_text)
        L_number_base = L_number_match.group() if L_number_match else 0.0  # マッチした文字列を取得、なければNone
        L_number = int(L_number_base.replace("L", ""))
        L_number_list.append(L_number)  # L数のリストに追加
        
        # 平均スタートタイミング: average_ST取得
        average_ST_match = re.search(r'\d\.\d+', player_info_text)
        average_ST = average_ST_match.group() if average_ST_match else 0.25  # マッチした文字列を取得、なければNone
        average_ST_list.append(float(average_ST))  # average_STのリストに追加
        
        # 全国勝率: national_winning_rate取得
        national_info = n_waku.find_all("td", class_="is-lineH2", rowspan="4")[1]
        national_lines = national_info.get_text(separator='\n').strip().split('\n')
        national_winning_rate = national_lines[0]
        national_winning_rate_list.append(float(national_winning_rate))

        # 全国2連対率: national_2nd_rate取得
        national_2nd_rate = national_lines[2]
        national_2nd_rate_list.append(float(national_2nd_rate))
        
        # 当地勝率: Local_winning_rate取得
        Local_info = n_waku.find_all("td", class_="is-lineH2", rowspan="4")[2]
        Local_lines = Local_info.get_text(separator='\n').strip().split('\n')
        Local_winning_rate = Local_lines[0]
        Local_winning_rate_list.append(float(Local_winning_rate))

        # 当地2連対率: Local_2nd_rate取得
        Local_2nd_rate = Local_lines[2]
        Local_2nd_rate_list.append(float(Local_2nd_rate))
        
        # モーター2連率: motor_2nd_rate取得
        motor_info = n_waku.find_all("td", class_="is-lineH2", rowspan="4")[3]
        motor_lines = motor_info.get_text(separator='\n').strip().split('\n')
        motor_2nd_rate = motor_lines[2]
        motor_2nd_rate_list.append(float(motor_2nd_rate))
        
        # モーター3連率: motor_3rd_rate取得
        motor_3rd_rate = motor_lines[4]
        motor_3rd_rate_list.append(float(motor_3rd_rate))   

        # ボート2連率: boat_2nd_rate取得
        boat_info = n_waku.find_all("td", class_="is-lineH2", rowspan="4")[4]
        boat_lines = boat_info.get_text(separator='\n').strip().split('\n')
        boat_2nd_rate = boat_lines[2]
        boat_2nd_rate_list.append(float(boat_2nd_rate))
        
        # 展示タイム: exhibition_time取得
        before_info = player_beforeinfo.find_all("td", rowspan="4")
        exhibition_time = before_info[3].text.replace('\xa0', '').strip()
        try:
            exhibition_time_float = float(exhibition_time) if exhibition_time else 0.0
            exhibition_time_list.append(exhibition_time_float)
        except ValueError:
            # exhibition_time が数値に変換できない場合は、例外をキャッチしてデフォルト値を設定します。
            exhibition_time_list.append(0.0)  # または適切な値や None をセットすることができます。

            
        # チルト角度: tilt取得
        before_info = player_beforeinfo.find_all("td", rowspan="4")
        tilt = before_info[4].text.replace('\xa0', '').strip()
        try:
            tilt_float = float(tilt) if tilt else -0.5
            tilt_list.append(tilt_float)
        except ValueError:
            # exhibition_time が数値に変換できない場合は、例外をキャッチしてデフォルト値を設定します。
            tilt_list.append(-0.5)  # または適切な値や None をセットすることができます。

   
    # 各変数をタプルとして結合して返す
    return tuple(player_rank_list + affiliations + weights + F_number_list + L_number_list + average_ST_list + national_winning_rate_list + national_2nd_rate_list + Local_winning_rate_list + Local_2nd_rate_list + motor_2nd_rate_list + motor_3rd_rate_list + boat_2nd_rate_list + exhibition_time_list + tilt_list)



# 水面コンディション取得
def read_course_condition(soup):

    # 気温: temperature取得
    weather1_bodyUnitLabelData = soup.find_all("span", class_="weather1_bodyUnitLabelData")
    temperature_base = weather1_bodyUnitLabelData[0].text.strip()
    temperature = float(temperature_base.replace("℃", ""))

        
    # 天気: weather取得
    weather1_bodyUnitLabelTitle = soup.find_all("span", class_="weather1_bodyUnitLabelTitle")
    weather = weather1_bodyUnitLabelTitle[1].text.strip()

    # 風向: wind_direction取得
    def convert_wind_number_to_direction(wind_number):
        wind_direction_map = {
            '1': '右横風',
            '3': '右追い風',
            '5': '追い風',
            '7': '左追い風',
            '9': '左横風',
            '11': '左向かい風',
            '13': '向かい風',
            '15': '右向かい風',
            '17': '無風'
         }
        return wind_direction_map.get(wind_number)  # 存在しないkeyの場合はNoneを返す
    wind_direction_elements = soup.find_all("p", class_="weather1_bodyUnitImage")
    # 風向きを取得する処理
    wind_number = None
    for element in wind_direction_elements:
        for class_name in element.get('class', []):  
            match = re.search(r'is-wind(\d+)', class_name)
            if match:
                wind_number = match.group(1)
                break
        if wind_number:  # 数字が見つかったらループを抜ける
            break
    # 風向きの数字を方角の文字列に変換
    wind_direction = convert_wind_number_to_direction(str(wind_number))
    
    
    # 風速: wind_speed取得
    weather1_bodyUnitLabelData = soup.find_all("span", class_="weather1_bodyUnitLabelData")
    wind_speed_elem = weather1_bodyUnitLabelData[1] 
    wind_speed_base = wind_speed_elem.text.strip() 
    wind_speed = float(wind_speed_base.replace("m", ""))
    
    
    # 水温: water_temperature取得
    water_temperature_elem = weather1_bodyUnitLabelData[2] 
    water_temperature_base = water_temperature_elem.text.strip() 
    water_temperature = float(water_temperature_base.replace("℃", ""))
    
    
    # 波高: wave_height取得
    wave_height_elem = weather1_bodyUnitLabelData[3] # 要素のテキストから波高を取得
    wave_height_base = wave_height_elem.text.strip() 
    wave_height = float(wave_height_base.replace("cm", ""))
    

    return temperature, weather, wind_direction, wind_speed, water_temperature, wave_height


