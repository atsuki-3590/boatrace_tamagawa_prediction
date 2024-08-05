# 前処理とモデルのトレーニングを合わせてトレーニング
# ファイルの変更は無し


# データ前処理 
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve, auc
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
import pickle
import matplotlib.pyplot as plt
import japanize_matplotlib 

japanize_matplotlib.japanize()

print("データ前処理を開始します")

# ファイルパスを変数に格納
processed_dir = 'data/processed/'


base_file_path = f"{processed_dir}data_boto4.csv"
# modified_file_path = f"{processed_dir}modified_data2.csv"

df = pd.read_csv(base_file_path, low_memory=False)

# 削除する列を指定
columns_to_drop = [
    'レースコード', '枠', '順位', '3連複_結果', '天気', '体重'
    , '全国勝率', '全国2連対率', 'モーター2連対率', 'ボート2連対率', '当地2連対率', '当地勝率', '全国2連対率_Zスコア', '当地2連対率_Zスコア', '展示タイム'
]

columns_to_drop_place = [
    'レースコード', '枠', '順位', '結果', '天気', '体重'
    , '全国勝率', 'モーター2連対率', 'ボート2連対率', '当地勝率', '展示タイム'
    , '全国2連対率', '当地2連対率'
    # , '全国勝率_Zスコア', '全国2連対率_Zスコア', 'モーター2連対率_Zスコア', 'ボート2連対率_Zスコア', '当地2連対率_Zスコア', '当地勝率_Zスコア', '展示タイム_Zスコア'
    # , '全国勝率_Zスコア', '当地勝率_Zスコア'
    ,'全国2連対率_Zスコア', '当地2連対率_Zスコア'
]


# 指定した列を削除
# new_data = df.drop(columns=columns_to_drop)  # 勝率
new_data = df.drop(columns=columns_to_drop_place)  # 3連対率

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



print("モデルのトレーニングを開始します")
# モデルのトレーニング
data = data_filtered

# 特徴量とターゲットに分ける
# X = data.drop(columns=['結果'])
# y = data['結果']
X = data.drop(columns=['3連複_結果'])
y = data['3連複_結果']

# 訓練データとテストデータに分割
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)   # シャッフルなし

# モデルの訓練
model = RandomForestClassifier(random_state=42)


# 通常
model.fit(X_train, y_train)


# # オーバーサンプリング
# # SMOTEのインスタンス化
# sm = SMOTE(random_state=42)
# # 訓練データの再サンプリング
# X_train_res, y_train_res = sm.fit_resample(X_train, y_train)
# # モデルの訓練（再サンプリング後のデータを使用）
# model.fit(X_train_res, y_train_res)


# # アンダーサンプリング
# # アンダーサンプリングのインスタンスを作成
# rus = RandomUnderSampler(random_state=42)
# # 訓練データにアンダーサンプリングを適用
# X_train_res, y_train_res = rus.fit_resample(X_train, y_train)
# # モデルの訓練
# model.fit(X_train_res, y_train_res)


# カスタム閾値の設定
custom_threshold = 0.40  # ここでカスタム閾値を設定します

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
with open('models/boat4_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("モデルが保存されました")

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

# ROC曲線をプロットして最適な閾値を確認（任意）
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)
plt.figure()

plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('偽陽性率')
plt.ylabel('真陽性率')
plt.title('2号艇勝率の特性曲線')
plt.legend(loc="lower right")
plt.show()