# データ前処理
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# ファイルパスを変数に格納
raw_file_path = 'data/raw/merged_data.csv'
processed_dir = 'data/processed/'

modified_file_path = f"{processed_dir}modified_data.csv"

df = pd.read_csv(raw_file_path, low_memory=False)

# 削除する列を指定
columns_to_drop = [
    '1枠_艇番', '2枠_艇番', '3枠_艇番', '4枠_艇番', '5枠_艇番', '6枠_艇番',
    '1枠_登録番号', '2枠_登録番号', '3枠_登録番号', '4枠_登録番号', '5枠_登録番号', '6枠_登録番号',
    '1枠_年齢', '2枠_年齢', '3枠_年齢', '4枠_年齢', '5枠_年齢', '6枠_年齢',
    '1枠_モーター番号', '2枠_モーター番号', '3枠_モーター番号', '4枠_モーター番号', '5枠_モーター番号', '6枠_モーター番号',
    '1枠_ボート番号', '2枠_ボート番号', '3枠_ボート番号', '4枠_ボート番号', '5枠_ボート番号', '6枠_ボート番号',
    '1枠_選手名', '2枠_選手名', '3枠_選手名', '4枠_選手名', '5枠_選手名', '6枠_選手名',
    '1枠_支部', '2枠_支部', '3枠_支部', '4枠_支部', '5枠_支部', '6枠_支部',
    '1着_登録番号', '2着_登録番号', '3着_登録番号', '4着_登録番号', '5着_登録番号', '6着_登録番号',
    '1着_着順', '2着_着順', '3着_着順', '4着_着順', '5着_着順', '6着_着順', 
    '1着_選手名', '2着_選手名', '3着_選手名', '4着_選手名', '5着_選手名', '6着_選手名',
    '日次', 'レース日'
]

# 指定した列を削除
new_data = df.drop(columns=columns_to_drop)

# 新しいカラムを追加
new_data['1号艇勝敗'] = new_data['1着_艇番'].apply(lambda x: 1 if x == 1 else 0)



# 欠損値の確認
missing_values = new_data.isnull().sum()
# カテゴリカルデータの確認
categorical_columns = new_data.select_dtypes(include=['object']).columns



# 全体の5%を超える欠損値を持つ列を削除
threshold = 0.05 * len(new_data)
columns_to_keep = missing_values[missing_values <= threshold].index
data_filtered = new_data[columns_to_keep]

# 欠損値を含む行を削除
data_filtered = data_filtered.dropna()

label_encoders = {}
# カテゴリカルデータのラベルエンコーディング
for column in categorical_columns:
    if column in data_filtered.columns:
        le = LabelEncoder()
        data_filtered[column] = le.fit_transform(data_filtered[column].astype(str))
        label_encoders[column] = le


os.makedirs(processed_dir, exist_ok=True)
data_filtered.to_csv(modified_file_path, index=False)

print("データ前処理が完了しました")
