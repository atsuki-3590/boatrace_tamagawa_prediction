import pickle
from sklearn.metrics import classification_report
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
sys.path.append(os.path.join(project_root, 'utils'))

from data_loader import load_data


# モデルのロード
with open('models/best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# データのロード
X_test, y_test = load_data('data/processed/modified_data.csv')

# 予測
y_pred = model.predict(X_test)

# 評価
report = classification_report(y_test, y_pred)
print(report)
