# モデルのトレーニング
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import matplotlib.pyplot as plt
import japanize_matplotlib 

japanize_matplotlib.japanize()

modified_file_path = f"data\processed\modified_data1.csv"
data = pd.read_csv(modified_file_path, low_memory=False)

# 特徴量とターゲットに分ける
X = data.drop(columns=['結果'])
y = data['結果']

# X = data.drop(columns=['3連複_結果'])
# y = data['3連複_結果']

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

# # モデルの保存
# with open('models/best_model.pkl', 'wb') as model_file:
#     pickle.dump(model, model_file)

# print("モデルが保存されました")



# 特徴量の重要度を確認
feature_importances = model.feature_importances_
features = X.columns

# データフレームにまとめる
importance_df = pd.DataFrame({'特徴量': features, '重要度': feature_importances})

# 重要度の高い順にソート
importance_df = importance_df.sort_values(by='重要度', ascending=False)

# 特徴量の重要度を表示
print(importance_df)

# 特徴量の重要度をプロット
plt.figure(figsize=(12, 8))
plt.barh(importance_df['特徴量'], importance_df['重要度'])
plt.xlabel('重要度')
plt.ylabel('特徴量')
plt.title('特徴量の重要度')
plt.gca().invert_yaxis()
plt.show()