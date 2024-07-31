import pickle
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
sys.path.append(os.path.join(project_root, 'utils'))

from data_loader import load_data


# データのロード
X, y = load_data("data/processed/modified_data.csv")

# テストデータの分割
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデルのロード
with open('models/boat1_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# 予測
y_pred = model.predict(X_test)

# 評価
report = classification_report(y_test, y_pred)
print(report)

