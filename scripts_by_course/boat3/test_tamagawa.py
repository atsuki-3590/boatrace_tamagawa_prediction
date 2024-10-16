import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, confusion_matrix
import os
import sys
import matplotlib.pyplot as plt
import japanize_matplotlib
import pickle

japanize_matplotlib.japanize()

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)

if grandparent_dir not in sys.path:
    sys.path.append(grandparent_dir)

from path_read_def import read_config

print("データ前処理を開始します")

base_file_path = read_config("BOAT3_PROCESSED_DATA_FILE_05")

# データの読み込み
df = pd.read_csv(base_file_path, low_memory=False)

# 必ず削除する列を指定
columns_to_drop = [
    'レースコード', 'レース場', 'スタンド距離', '枠', '順位', '結果'
]

# 指定した列を削除
new_data = df.drop(columns=columns_to_drop)

# カテゴリカルデータの確認
categorical_columns = new_data.select_dtypes(include=['object']).columns

# 欠損値を含む行を削除
data_filtered = new_data.dropna()

label_encoders = {}
# カテゴリカルデータのラベルエンコーディング
for column in categorical_columns:
    if column in data_filtered.columns:
        le = LabelEncoder()
        data_filtered[column] = le.fit_transform(data_filtered[column].astype(str))
        label_encoders[column] = le

print("再帰的特徴量削減を開始します")

# 特徴量とターゲットに分ける
data = data_filtered
X = data.drop(columns=['3連複_結果'])
y = data['3連複_結果']

# 再帰的特徴量削減を適用する特徴量を指定
columns_for_rfe = [
    '天気', '体重', 
    '全国勝率_Zスコア', '全国2連対率_Zスコア', 'モーター2連対率_Zスコア',
    'ボート2連対率_Zスコア', '当地2連対率_Zスコア', '当地勝率_Zスコア', '展示タイム_Zスコア'
]

# RFEのためのデータセットを作成
X_rfe = X[columns_for_rfe]

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X_rfe, y, test_size=0.2, shuffle=False)

# ランダムフォレストモデルのインスタンス化
model = RandomForestClassifier(random_state=42)

# 再帰的特徴量削減（RFE）
rfe = RFE(estimator=model, n_features_to_select=10)  # 残したい特徴量の数を指定
rfe.fit(X_train, y_train)

# 選ばれた特徴量のサポートとランクを表示
selected_features = X_rfe.columns[rfe.support_]
print(f"選択された特徴量: {selected_features}")

# 選択された特徴量のみを使用してモデルを再訓練
X_train_selected = rfe.transform(X_train)
X_test_selected = rfe.transform(X_test)

# 最良のハイパーパラメーターでモデルを作成
best_params = {'bootstrap': True, 'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 200}
best_model = RandomForestClassifier(**best_params, random_state=42)

# 最良モデルの訓練
best_model.fit(X_train_selected, y_train)

# モデルの予測確率
y_pred_proba = best_model.predict_proba(X_test_selected)[:, 1]

# 指定された閾値を使用して予測
custom_threshold = 0.5
y_pred = (y_pred_proba >= custom_threshold).astype(int)

# モデルの評価
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
auc_score = roc_auc_score(y_test, y_pred_proba)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"AUC Score: {auc_score}")
print(f"Classification Report: \n{report}")
print(f"Confusion Matrix: \n{conf_matrix}")
print("モデルのトレーニングが完了しました")

# モデルの保存
models_path = read_config("BOAT3_TRAIN_DATA_pkl_05")

with open(models_path, 'wb') as model_file:
    pickle.dump(model, model_file)

print("モデルが保存されました")


# 特徴量の重要度を確認
feature_importances = best_model.feature_importances_
features = selected_features

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