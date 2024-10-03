# モデルのトレーニング
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
import pickle
import matplotlib.pyplot as plt
import japanize_matplotlib 

japanize_matplotlib.japanize()

modified_file_path = f"data/processed/modified_data1.csv"  # パスの区切りを修正
data = pd.read_csv(modified_file_path, low_memory=False)

# 特徴量とターゲットに分ける
X = data.drop(columns=['レースコード', 'レース場', '風向', '3連複_結果'])
y = data['3連複_結果']

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)   # シャッフルなし

# モデルの訓練
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# カスタム閾値の設定
custom_threshold = 0.60  # ここでカスタム閾値を設定します

# モデルの予測
y_pred_proba = model.predict_proba(X_test)[:, 1]
y_pred = (y_pred_proba >= custom_threshold).astype(int)  # カスタム閾値を使用して予測

# モデルの評価
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
auc_score = roc_auc_score(y_test, y_pred_proba)

print(f"Custom_threshold: {custom_threshold}")
print(f"Accuracy: {accuracy}")
print(f"AUC Score: {auc_score}")
print(f"Classification Report: \n{report}")
print("モデルのトレーニングが完了しました")

# モデルの保存
with open('models/boat1_model_1.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("モデルが保存されました")

# 訓練時の特徴量リストを保存
trained_features = X.columns.tolist()

with open('models/trained_features_boat1.pkl', 'wb') as f:
    pickle.dump(trained_features, f)

print("訓練時の特徴量リストが保存されました")

# 特徴量の重要度を確認
feature_importances = model.feature_importances_
features = X.columns

# データフレームにまとめる
importance_df = pd.DataFrame({'特徴量': features, '重要度': feature_importances})

# 重要度の高い順にソート
importance_df = importance_df.sort_values(by='重要度', ascending=False)

# 特徴量の重要度を表示
print(importance_df)

# # 特徴量の重要度をプロット
# plt.figure(figsize=(12, 8))
# plt.barh(importance_df['特徴量'], importance_df['重要度'])
# plt.xlabel('重要度')
# plt.ylabel('特徴量')
# plt.title('特徴量の重要度')
# plt.gca().invert_yaxis()
# plt.show()
