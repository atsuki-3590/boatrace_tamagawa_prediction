import pandas as pd
from functools import reduce

file_paths = [
    'data/processed/test_predictions_boat1.csv',
    'data/processed/test_predictions_boat2.csv',
    'data/processed/test_predictions_boat3.csv',
    'data/processed/test_predictions_boat4.csv',
    'data/processed/test_predictions_boat5.csv',
    'data/processed/test_predictions_boat6.csv'
]

result_file_paths = [
    'data/processed/data_boto1.csv',
    'data/processed/data_boto2.csv',
    'data/processed/data_boto3.csv',
    'data/processed/data_boto4.csv',
    'data/processed/data_boto5.csv',
    'data/processed/data_boto6.csv'
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
final_df = pd.merge(predictions_df, results_df, on='レースコード', how='inner')

# オッズデータの追加
odds_data = pd.read_csv('data/raw/odds_3f.csv')
final_df = pd.merge(final_df, odds_data, on='レースコード', how='inner')

output_path = "test_predict_with_odds.csv"
final_df.to_csv(f"data/processed/{output_path}", index=False)

# 結果を確認
print(final_df.head())