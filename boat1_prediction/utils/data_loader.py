# データの前処理に関する共通ファイル

# サンプル
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)