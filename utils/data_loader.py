# データの前処理に関する共通ファイル
import pandas as pd


def load_data(file_path):
    data = pd.read_csv(file_path)
    X = data.drop('1号艇勝敗', axis=1)
    y = data['1号艇勝敗']
    return X, y