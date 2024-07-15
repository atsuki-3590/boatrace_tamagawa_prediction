# モデルのトレーニング

# サンプル
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import yaml

# 設定ファイルの読み込み
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# データの読み込み
df = pd.read_csv(config['data']['processed_data_path'])

# 特徴量とターゲットの分割
X = df.drop(columns=['target'])
y = df['target']

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=config['model']['random_state'])

# モデルの定義とトレーニング
model = RandomForestClassifier(
    n_estimators=config['model']['n_estimators'],
    max_depth=config['model']['max_depth'],
    random_state=config['model']['random_state']
)
model.fit(X_train, y_train)

# 予測と評価
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy}')

# モデルの保存
joblib.dump(model, 'models/best_model.pkl')
print('Model saved to models/best_model.pkl')
