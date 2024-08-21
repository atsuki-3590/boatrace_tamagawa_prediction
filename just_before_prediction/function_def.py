from bs4 import BeautifulSoup 

# raceresult_data
def read_raceresult_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        soup = BeautifulSoup(file_content, 'html.parser')

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
            '1': '北',
            '3': '北東',
            '5': '東',
            '7': '南東',
            '9': '南',
            '11': '南西',
            '13': '西',
            '15': '北西',
            '17': '無風'
         }
        return wind_direction_map.get(wind_number)  # 存在しないkeyの場合はNoneを返す
    wind_direction_elements = soup.find_all("p", class_="weather1_bodyUnitImage")
    # 風向きを取得する処理
    wind_number = None
    for element in wind_direction_elements:
        for class_name in element.get('class', []):  
            match = re.search('is-wind(\d+)', class_name)
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
    
    
    # 結果（一着枠番号）: result
    # 'is-fs14 is-fBold is-boatColor'に続く数字を持つ最初のtd要素を探す
    result_element = soup.find("td", class_=re.compile(r'is-fs14 is-fBold is-boatColor\d+'))
    result_waku = int(result_element.text.strip())
    result = get_frame_by_course(result_waku, file_path)
    
    
  

    return temperature, weather, wind_direction, wind_speed, water_temperature, wave_height, result
