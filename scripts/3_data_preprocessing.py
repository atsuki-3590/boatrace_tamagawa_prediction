import os
import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)

if grandparent_dir not in sys.path:
    sys.path.append(parent_dir)

from path_read_def import read_config
from race_studium_data import race_course_to_course_number

# データ前処理
def preprocess_boat_data(boat_number):
    print(f"データ前処理を開始します ({boat_number}号艇)")

    # ディレクトリの設定
    # processed_dir = 'data/processed/'
    # processed_dir = 'data/processed_new/'
    
    # ファイルパスを生成
    input_file_path = read_config(f"BOAT{i}_PROCESSED_DATA_FILE_05")
    output_file_path = read_config(f"BOAT{i}_MODIFIED_DATA_FILE_05")

    # データの読み込み
    df = pd.read_csv(input_file_path, low_memory=False)

    # 削除する列を指定
    columns_to_drop = [
        '枠', '順位', '結果', '天気', '体重',
        # 'レース場', 
        '全国勝率', '全国2連対率', 'モーター2連対率', 'ボート2連対率', 
        '当地2連対率', '当地勝率', '全国2連対率_Zスコア', '当地2連対率_Zスコア', '展示タイム'
    ]

    # 指定した列を削除
    new_data = df.drop(columns=columns_to_drop)

    # レース場のマッピングを適用し、数値型に変換
    if 'レース場' in new_data.columns:
        new_data['レース場'] = new_data['レース場'].map(race_course_to_course_number).astype(float)


    # 欠損値の確認
    missing_values = new_data.isnull().sum()
    print(f"欠損値の確認:\n{missing_values}")

    # カテゴリカルデータの確認
    categorical_columns = new_data.select_dtypes(include=['object']).columns
    if 'レースコード' in categorical_columns:
        categorical_columns = categorical_columns.drop('レースコード')

    # 欠損値を含む行を削除
    data_filtered = new_data.dropna()

    # カテゴリカルデータのラベルエンコーディング
    for column in categorical_columns:
        if column in data_filtered.columns:
            le = LabelEncoder()
            data_filtered[column] = le.fit_transform(data_filtered[column].astype(str))

    # ディレクトリの作成
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # 処理済みデータをCSVファイルに保存
    data_filtered.to_csv(output_file_path, index=False)

    print(f"{boat_number}号艇のデータ前処理が完了しました")


# すべてのボートのデータを処理する
for i in range(1, 7):
    preprocess_boat_data(i)

print("すべてのボートのデータ前処理が完了しました")



