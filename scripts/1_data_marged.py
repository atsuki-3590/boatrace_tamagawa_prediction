# データ結合
import pandas as pd
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)

if grandparent_dir not in sys.path:
    sys.path.append(parent_dir)

from path_read_def import read_config

# ファイルのパス
info_path = read_config("DATA_INFO_05")
result_path = read_config("DATA_RESULT_05")

# CSVファイルの読み込み
info_df = pd.read_csv(info_path)
result_df = pd.read_csv(result_path, low_memory=False)

columns_to_drop = ["レース場", "距離", "レース回"]
result_df1 = result_df.drop(columns=columns_to_drop)

# データフレームの結合
merged_df = pd.merge(info_df, result_df1, on='レースコード', how='left')

# 重複カラムで、info側の不要な列を削除（result側のカラムを優先する）
columns_to_drop = [col for col in merged_df.columns if col.endswith('_info')]
merged_df = merged_df.drop(columns=columns_to_drop)

# カラムの順番を指定
columns_order = ['レースコード', 'レース場', 'レース回', '天気', '風向', '風速', '波の高さ', '距離', '決まり手'] + [col for col in merged_df.columns if col not in ['レースコード', '天気', '風向', '風速', '波の高さ', '決まり手']]
# columns_order = ['レースコード', 'レース場', 'レース回', '天気', '風向', '風速', '波の高さ', '距離', '決まり手'] + [col for col in merged_df.columns if col not in ['レースコード', 'レース場', 'レース回', '天気', '風向', '風速', '波の高さ', '距離', '決まり手']]

merged_df = merged_df[columns_order]

# print(merged_df.head())

output_path = read_config("DATA_MEARGED_05")

os.makedirs(os.path.dirname(output_path), exist_ok=True)
merged_df.to_csv(output_path, index=False)

print("データの結合が完了しました。")

