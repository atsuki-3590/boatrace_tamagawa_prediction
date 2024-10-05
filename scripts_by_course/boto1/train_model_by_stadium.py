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

# レース場とコース番号のマッピング
race_course_to_course_number = {
    "桐生": "01",
    "戸田": "02",
    "江戸川": "03",
    "平和島": "04",
    "多摩川": "05",
    "浜名湖": "06",
    "蒲郡": "07",
    "常滑": "08",
    "津": "09",
    "三国": "10",
    "びわこ": "11",
    "住之江": "12",
    "尼崎": "13",
    "鳴門": "14",
    "丸亀": "15",
    "児島": "16",
    "宮島": "17",
    "徳山": "18",
    "下関": "19",
    "若松": "20",
    "芦屋": "21",
    "福岡": "22",
    "唐津": "23",
    "大村": "24"
}

# 使用するレース場を指定
race_stadium = "多摩川"
course_number = race_course_to_course_number[race_stadium]


modified_file_path = f"data/processed/modified_data1.csv"
data = pd.read_csv(modified_file_path, low_memory=False)

# 指定したレース場のデータのみを選択
data = data[data['レース場'] == race_stadium]

# 特徴量とターゲットに分ける
X = data.drop(columns=['レースコード', 'レース場', '風向', '3連複_結果'])
y = data['3連複_結果']

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)   # シャッフルなし

# モデルの訓練
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# カスタム閾値の設定
custom_threshold = 0.60

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
model_filename = f'models/boat1_{course_number}_model.pkl'
with open(model_filename, 'wb') as model_file:
    pickle.dump(model, model_file)

print(f"モデルが保存されました: {model_filename}")

# 訓練時の特徴量リストを保存
trained_features = X.columns.tolist()
features_filename = f'models/trained_features_boat1_{course_number}.pkl'
with open(features_filename, 'wb') as f:
    pickle.dump(trained_features, f)

print(f"訓練時の特徴量リストが保存されました: {features_filename}")

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
