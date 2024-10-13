import pandas as pd
from functools import reduce
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

from race_studium_data import race_course_to_course_number

race_stadium = "多摩川"
course_number_str = race_course_to_course_number[race_stadium]
course_number_int = int(course_number_str) 

# processed = "processed"
processed = "processed_new"

# 予測データが含まれる
file_paths = [
    f'data/{processed}/test_{course_number_str}_predictions_boat1.csv',
    f'data/{processed}/test_{course_number_str}_predictions_boat2.csv',
    f'data/{processed}/test_{course_number_str}_predictions_boat3.csv',
    f'data/{processed}/test_{course_number_str}_predictions_boat4.csv',
    f'data/{processed}/test_{course_number_str}_predictions_boat5.csv',
    f'data/{processed}/test_{course_number_str}_predictions_boat6.csv'
]

# 3連複結果の取得に必要
result_file_paths = [
    'data/processed/data_boat1.csv',
    'data/processed/data_boat2.csv',
    'data/processed/data_boat3.csv',
    'data/processed/data_boat4.csv',
    'data/processed/data_boat5.csv',
    'data/processed/data_boat6.csv'
]

# Predictions データの結合
data_frames = []
for idx, file_path in enumerate(file_paths, start=1):
    df = pd.read_csv(file_path)
    df = df[['レースコード', 'predict_result']].rename(columns={'predict_result': f'predict_result_{idx}'})
    data_frames.append(df)

predictions_df = reduce(lambda left, right: pd.merge(left, right, on='レースコード', how='outer'), data_frames)

# Results データの結合
result_data_frames = []
for idx, file_path in enumerate(result_file_paths, start=1):
    df = pd.read_csv(file_path)
    df = df[['レースコード', '3連複_結果']].rename(columns={'3連複_結果': f'result_{idx}'})
    result_data_frames.append(df)

results_df = reduce(lambda left, right: pd.merge(left, right, on='レースコード', how='outer'), result_data_frames)

# Predictions と Results の結合
predictions_df = pd.merge(predictions_df, results_df, on='レースコード', how='inner')

# オッズデータの追加
odds_data = pd.read_csv('data/raw/odds_3f.csv')
final_df = pd.merge(predictions_df, odds_data, on='レースコード', how='inner')

result_columns = [f'result_{i}' for i in range(1, 7)]
final_df['result'] = final_df[result_columns].apply(lambda row: '='.join([str(i+1) for i, val in enumerate(row) if val == 1]), axis=1)

final_df.drop(columns=result_columns, inplace=True)

output_path = f"test_{course_number_str}_predict_with_odds.csv"
final_df.to_csv(f"data/{processed}/{output_path}", index=False)

# 結果を確認
print(final_df.head())