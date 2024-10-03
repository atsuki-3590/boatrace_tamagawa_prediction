from datetime import datetime as dt
import requests
from bs4 import BeautifulSoup 
from function_def import read_racelist_data, read_course_condition
import pandas as pd
import joblib 
import os 
import pickle

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

目標の形
レース場,レース回,風向,風速,波の高さ,スタンド距離,
級別,3連複_結果,全国勝率,当地勝率,モーター2連対率,ボート2連対率,展示タイム
"""

# 参考: https://www.boatrace.jp/owpc/pc/race/racelist?rno=12&jcd=05&hd=20240905


race_course_to_course_number = {
    "桐生": "01",
    "戸田": "02",
    "江戸川": "03",
    "平和島": "04",
    "多摩川": "05",
    "浜名湖": "06",
    "蒲郡": "07",
    "常滑": "08",
    "津": "09",
    "三国": "10",
    "びわこ": "11",
    "住之江": "12",
    "尼崎": "13",
    "鳴門": "14",
    "丸亀": "15",
    "児島": "16",
    "宮島": "17",
    "徳山": "18",
    "下関": "19",
    "若松": "20",
    "芦屋": "21",
    "福岡": "22",
    "唐津": "23",
    "大村": "24"
}

# 風向のマッピング
wind_direction_map = {
    '追い風': 1,
    '左追い風': 2,
    '左横風': 3,
    '左向かい風': 4,
    '向かい風': 5,
    '右向かい風': 6,
    '右横風': 7,
    '右追い風': 8,
    '無風': 9
}

# 級別のマッピング
grade_mapping = {'A1': 1, 'A2': 2, 'B1': 3, 'B2': 4}

# レース場とスタンド距離のマッピング
race_course_to_stand_distance = {
    "桐生": 47,
    "戸田": 37,
    "江戸川": 37.1,
    "平和島": 37,
    "多摩川": 41,
    "浜名湖": 42.7,
    "蒲郡": 41.3,
    "常滑": 40,
    "津": 40,
    "三国": 45,
    "びわこ": 47,
    "住之江": 45,
    "尼崎": 49.1,
    "鳴門": 45,
    "丸亀": 42,
    "児島": 43,
    "宮島": 40,
    "徳山": 45,
    "下関": 43,
    "若松": 41,
    "芦屋": 50,
    "福岡": 50,
    "唐津": 42,
    "大村": 48
}



DATE = "2024-10-01"
Racenumber = "11"
Course = "多摩川"

stand_distance = race_course_to_stand_distance.get(Course)

def fetch_boatrace_data(DATE, Racenumber, Course, page_type):

    date = dt.strptime(DATE, '%Y-%m-%d')
    Coursenumber = race_course_to_course_number.get(Course)

    url = f"https://www.boatrace.jp/owpc/pc/race/{page_type}?rno={Racenumber}&jcd={Coursenumber}&hd={date.strftime('%Y%m%d')}"
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    bs = BeautifulSoup(response.text, 'html.parser')

    return bs


racelist = fetch_boatrace_data(DATE, Racenumber, Course, "racelist")
beforeinfo = fetch_boatrace_data(DATE, Racenumber, Course, "beforeinfo")


# 出走表データを取得
tuple_racelist = read_racelist_data(racelist, beforeinfo)
df_racelist = pd.DataFrame([tuple_racelist], columns = [
    '1枠_級別', '2枠_級別', '3枠_級別', '4枠_級別', '5枠_級別', '6枠_級別', 
    '1枠_支部', '2枠_支部', '3枠_支部', '4枠_支部', '5枠_支部', '6枠_支部',
    '1枠_体重', '2枠_体重', '3枠_体重', '4枠_体重', '5枠_体重', '6枠_体重',
    '1枠_F数', '2枠_F数', '3枠_F数', '4枠_F数', '5枠_F数', '6枠_F数',
    '1枠_L数', '2枠_L数', '3枠_L数', '4枠_L数', '5枠_L数', '6枠_L数',
    '1枠_平均ST', '2枠_平均ST', '3枠_平均ST', '4枠_平均ST', '5枠_平均ST', '6枠_平均ST',
    '1枠_全国勝率', '2枠_全国勝率', '3枠_全国勝率', '4枠_全国勝率', '5枠_全国勝率', '6枠_全国勝率',
    '1枠_全国2連対率', '2枠_全国2連対率', '3枠_全国2連対率', '4枠_全国2連対率', '5枠_全国2連対率', '6枠_全国2連対率', 
    '1枠_当地勝率', '2枠_当地勝率', '3枠_当地勝率', '4枠_当地勝率', '5枠_当地勝率', '6枠_当地勝率',
    '1枠_当地2連対率', '2枠_当地2連対率', '3枠_当地2連対率', '4枠_当地2連対率', '5枠_当地2連対率', '6枠_当地2連対率', 
    '1枠_モーター2連対率', '2枠_モーター2連対率', '3枠_モーター2連対率', '4枠_モーター2連対率', '5枠_モーター2連対率', '6枠_モーター2連対率',
    '1枠_モーター3連対率', '2枠_モーター3連対率', '3枠_モーター3連対率', '4枠_モーター3連対率', '5枠_モーター3連対率', '6枠_モーター3連対率',
    '1枠_ボート2連対率', '2枠_ボート2連対率', '3枠_ボート2連対率', '4枠_ボート2連対率', '5枠_ボート2連対率', '6枠_ボート2連対率',
    '1枠_展示タイム', '2枠_展示タイム', '3枠_展示タイム', '4枠_展示タイム', '5枠_展示タイム', '6枠_展示タイム',
    '1枠_チルト', '2枠_チルト', '3枠_チルト', '4枠_チルト', '5枠_チルト', '6枠_チルト'
])


tuple_course_condition = read_course_condition(beforeinfo)
df_course_condition = pd.DataFrame([tuple_course_condition], columns = [
    '気温', '天気', '風向', '風速', '水温', '波高'
])


# print("df_racelist:", df_racelist.columns)
# print("df_course_condition:", df_course_condition.columns)
# print("1枠_全国2連対率:", df_racelist['1枠_全国2連対率'])
# print("1枠_級別:", df_racelist['1枠_級別'])
# print(df_racelist.head())
# print(df_course_condition.head())


# Zスコアを追加する関数
def add_z_score(df, column):
    mean = df[column].mean()
    std = df[column].std()
    df[f'{column}_Zスコア'] = (df[column] - mean) / std

# レース情報（仮）レース場とレース回は同一と仮定
race_info = {
    'レース場': Course,  
    'レース回': Racenumber,        
    '風向': df_course_condition['風向'][0],
    '風速': df_course_condition['風速'][0],
    '波の高さ': df_course_condition['波高'][0],
    'スタンド距離': stand_distance,  
}

# 各枠のデータを1つずつ整形しリストにまとめる
data_list = []
for i in range(1, 7):
    frame = f'{i}'
    frame_data = {
        '枠': frame,
        'レース場': race_info['レース場'],
        'レース回': race_info['レース回'],
        '風向': race_info['風向'],
        '風速': race_info['風速'],
        '波の高さ': race_info['波の高さ'],
        'スタンド距離': race_info['スタンド距離'],
        '級別': df_racelist[f'{frame}枠_級別'][0],
        '全国勝率': df_racelist[f'{frame}枠_全国勝率'][0],
        '当地勝率': df_racelist[f'{frame}枠_当地勝率'][0],
        'モーター2連対率': df_racelist[f'{frame}枠_モーター2連対率'][0],
        'ボート2連対率': df_racelist[f'{frame}枠_ボート2連対率'][0],
        '展示タイム': df_racelist[f'{frame}枠_展示タイム'][0]
    }
    data_list.append(frame_data)

# データをDataFrameに変換
df_final = pd.DataFrame(data_list)

# Zスコアの計算
columns_to_zscore = ['全国勝率', '当地勝率', 'モーター2連対率', 'ボート2連対率', '展示タイム']
for col in columns_to_zscore:
    add_z_score(df_final, col)

# 必要なカラムを最終的な形にする
df_final = df_final[['枠', 'レース場', 'レース回', '風向', '風速', '波の高さ', 
                     'スタンド距離', '級別', '全国勝率_Zスコア', 
                     '当地勝率_Zスコア', 'モーター2連対率_Zスコア', 
                     'ボート2連対率_Zスコア', '展示タイム_Zスコア']]

# レース場の番号を数値型に変換
race_course_to_course_number_int = {k: int(v) for k, v in race_course_to_course_number.items()}
df_final['レース場'] = df_final['レース場'].map(race_course_to_course_number_int)

# 級別のエンコーディング
df_final['級別'] = df_final['級別'].map(grade_mapping)

# 風向のエンコーディング
df_final['風向'] = df_final['風向'].map(wind_direction_map)

# '枠' カラムを追加（1〜6）
df_final['枠'] = range(1, 7)

# 予測に使用する特徴量を選択
# 訓練時に使用した特徴量は 'trained_features'
# 予測データがそれと一致するように整形

# # 訓練時に使用した特徴量を含めるために、df_finalに存在しないものは追加
# for feature in trained_features:
#     if feature not in df_final.columns:
#         df_final[feature] = 0  # 適切なデフォルト値を設定

# # 訓練時の特徴量順に並べ替える
# features_for_prediction = df_final[trained_features]

# モデルと特徴量リストのロード
model_paths = {
    1: 'models/boat1_model_1.pkl',
    2: 'models/boat2_model_1.pkl',
    3: 'models/boat3_model_1.pkl',
    4: 'models/boat4_model_1.pkl',
    5: 'models/boat5_model_1.pkl',
    6: 'models/boat6_model_1.pkl',
}
trained_feature_paths = {
    1: 'models/trained_features_boat1.pkl',
    2: 'models/trained_features_boat2.pkl',
    3: 'models/trained_features_boat3.pkl',
    4: 'models/trained_features_boat4.pkl',
    5: 'models/trained_features_boat5.pkl',
    6: 'models/trained_features_boat6.pkl',
}

models = {}
trained_features = {}

# モデルと特徴量リストをロード
for boat_num in range(1, 7):
    model_path = model_paths.get(boat_num)
    feature_path = trained_feature_paths.get(boat_num)

    # モデルのロード
    if os.path.exists(model_path):
        models[boat_num] = joblib.load(model_path)
        # print(f"モデル {boat_num} がロードされました: {model_path}")
    else:
        # print(f"モデルが見つかりません: {model_path}")
        models[boat_num] = None

    # 特徴量リストのロード
    if os.path.exists(feature_path):
        with open(feature_path, 'rb') as f:
            trained_features[boat_num] = pickle.load(f)
            # print(f"特徴量リスト {boat_num} がロードされました: {feature_path}")
    else:
        # print(f"特徴量リストが見つかりません: {feature_path}")
        trained_features[boat_num] = []

# ワンホットエンコーディングを適用
df_final = pd.get_dummies(df_final, columns=['レース場', '級別', '風向'], drop_first=False)

predictions = []

# 各ボートごとの予測を実行
for index, row in df_final.iterrows():
    boat_num = row['枠']
    model = models.get(boat_num)
    feature_list = trained_features.get(boat_num)

    if model is not None and feature_list:
        # 訓練時の特徴量リストに従って、必要な特徴量のみを抽出
        features_for_prediction = row.reindex(feature_list).fillna(0)

        # DataFrameに変換して渡す
        features_for_prediction_df = pd.DataFrame([features_for_prediction], columns=feature_list)

        try:
            # 予測を実行
            pred = model.predict(features_for_prediction_df)[0]
            predictions.append(pred)
        except ValueError as e:
            print(f"予測エラー for boat {boat_num} at index {index}: {e}")
            predictions.append(None)
    else:
        print(f"モデルまたは特徴量リストが見つかりません for boat {boat_num}")
        predictions.append(None)

# 予測結果をデータフレームに追加
df_final['予測_3着以内'] = predictions

# 必要なカラムを再度整理
df_final = df_final[['レース回', '風速', '波の高さ', 'スタンド距離',
                     '全国勝率_Zスコア', '当地勝率_Zスコア',
                     'モーター2連対率_Zスコア', 'ボート2連対率_Zスコア',
                     '展示タイム_Zスコア', '予測_3着以内']]

# 結果の表示
print(df_final)