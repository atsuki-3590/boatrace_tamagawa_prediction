# モデルのトレーニング
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle


modified_file_path = "data\processed\modified_data.csv"
data = pd.read_csv(modified_file_path, low_memory=False)

# 特徴量とターゲットに分ける
X = data.drop(columns=['1号艇勝敗'])
y = data['1号艇勝敗']

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデルの訓練
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# モデルの予測
y_pred = model.predict(X_test)

# モデルの評価
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

accuracy, report

print(f"accuracy:{accuracy}, report{report}")
print("モデルのトレーニングが完了しました")

# モデルの保存
with open('models/best_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("モデルが保存されました")