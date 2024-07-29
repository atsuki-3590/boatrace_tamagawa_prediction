# データの前処理に関する共通ファイル
import pandas as pd


def load_data(file_path):
    data = pd.read_csv(file_path)
    X = data.drop('結果', axis=1)
    y = data['結果']
    return X, y