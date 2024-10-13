import pandas as pd
import pickle
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

from race_studium_data import race_course_to_course_number

# processed = "processed"
processed = "processed_new"


def predict_with_model(boat_number):
    # データの読み込み
    data = pd.read_csv(f"data/processed/modified_data{boat_number}.csv")
    
    race_stadium = "多摩川"
    course_number_str = race_course_to_course_number[race_stadium]
    course_number_int = int(course_number_str) 

    data = data[data['レース場'] == course_number_int]
    data['レース日'] = pd.to_datetime(data['レースコード'].str[:8], format='%Y%m%d')
    data = data[data['レース日'] >= pd.Timestamp('2024-06-01')]


    # モデルファイルと特徴量リストのパスを組み立て
    model_path = f'models/{course_number_str}_boat{boat_number}_model.pkl'
    features_path = f'models/{course_number_str}_trained_features_boat{boat_number}.pkl'

    # モデルの読み込み
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    
    # 特徴量リストの読み込み
    with open(features_path, 'rb') as features_file:
        trained_features = pickle.load(features_file)
    
    # 特徴量の準備（訓練時と同じ特徴量を使用）
    X = data[trained_features]

    # 予測の実行
    data['predict_result'] = model.predict(X)

    data = data.drop('レース日', axis=1)

    # 予測結果を含んだデータの保存
    output_path = f"test_{course_number_str}_predictions_boat{boat_number}.csv"
    data.to_csv(f"data/{processed}/{output_path}", index=False)

    print(f"予測が完了し、結果が '{output_path}' に保存されました。")

# 使用例: boat1 のモデルを使って予測
# predict_with_model(1)

for i in range(1, 7):
    predict_with_model(i)




