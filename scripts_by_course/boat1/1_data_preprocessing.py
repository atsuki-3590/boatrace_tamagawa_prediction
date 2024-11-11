# データ前処理
import os
import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)

if grandparent_dir not in sys.path:
    sys.path.append(grandparent_dir)

from path_read_def import read_config

print("データ前処理を開始します")


base_file_path = read_config("BOAT1_MODIFIED_DATA_FILE_05")

# modified_file_path = f"{processed_dir}modified_data1.csv"

df = pd.read_csv(base_file_path, low_memory=False)
print(df.head())

# # 削除する列を指定
# columns_to_drop = [
#     'レースコード', '枠', '順位', '3連複_結果', '天気', '体重'
#     , '全国勝率', '全国2連対率', 'モーター2連対率', 'ボート2連対率', '当地2連対率', '当地勝率', '全国2連対率_Zスコア', '当地2連対率_Zスコア', '展示タイム'
# ]

# columns_to_drop_place = [
#     # 'レースコード', 
#     '枠', '順位', '結果', '天気', '体重'
#     , '全国勝率', '全国2連対率', 'モーター2連対率', 'ボート2連対率', '当地2連対率', '当地勝率', '全国2連対率_Zスコア', '当地2連対率_Zスコア', '展示タイム'
# ]

# # 指定した列を削除
# # new_data = df.drop(columns=columns_to_drop)
# new_data = df.drop(columns=columns_to_drop_place)  # 3連対率



# # 欠損値の確認
# missing_values = new_data.isnull().sum()
# # カテゴリカルデータの確認
# categorical_columns = new_data.select_dtypes(include=['object']).columns
# categorical_columns = categorical_columns.drop('レースコード')

# # 欠損値を含む行を削除
# data_filtered = new_data.dropna()

# label_encoders = {}
# # カテゴリカルデータのラベルエンコーディング
# for column in categorical_columns:
#     if column in data_filtered.columns:
#         le = LabelEncoder()
#         data_filtered[column] = le.fit_transform(data_filtered[column].astype(str))
#         label_encoders[column] = le


# os.makedirs(processed_dir, exist_ok=True)
# data_filtered.to_csv(modified_file_path, index=False)

# print("1号艇のデータ前処理が完了しました")



