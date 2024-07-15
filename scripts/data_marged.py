# データ結合
import pandas as pd
import os

# ファイルのパス
info_path = 'data/raw/info.csv'
result_path = 'data/raw/result.csv'

# CSVファイルの読み込み
info_df = pd.read_csv(info_path)
result_df = pd.read_csv(result_path, low_memory=False)

merged_df = pd.merge(info_df, result_df, on='レースコード', how='left')
columns_order = ['レースコード', '天気', '風向', '風速', '波の高さ', '決まり手'] + [col for col in merged_df.columns if col not in ['レースコード', '天気', '風向', '風速', '波の高さ', '決まり手']]
merged_df = merged_df[columns_order]

# print(merged_df.head())

output_path = 'data/raw/merged_data.csv'

os.makedirs(os.path.dirname(output_path), exist_ok=True)
merged_df.to_csv(output_path, index=False)

print("データの結合が完了しました。")

