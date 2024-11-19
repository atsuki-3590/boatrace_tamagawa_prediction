import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import japanize_matplotlib
import os
import sys

japanize_matplotlib.japanize()

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)

if grandparent_dir not in sys.path:
    sys.path.append(grandparent_dir)

from path_read_def import read_config

# データの読み込み（仮のパス）
data_path = read_config("BOAT1_PROCESSED_DATA_FILE_05")  # 適切なパスに置き換えてください
df = pd.read_csv(data_path)

# 必ず削除する列を指定
columns_to_drop = ['レースコード', 'レース場', 'スタンド距離', '枠', '順位', '結果']

# 指定した列を削除
data_filtered = df.drop(columns=columns_to_drop)

# 欠損値を含む行を削除
data_filtered = data_filtered.dropna()

# データの重複を削除
data_filtered = data_filtered.drop_duplicates()

# カテゴリカルデータの確認とエンコーディング
categorical_columns = data_filtered.select_dtypes(include=['object']).columns
data_filtered = pd.get_dummies(data_filtered, columns=categorical_columns, drop_first=True)

# 特徴量とターゲットに分ける
X = data_filtered.drop(columns=['3連複_結果'])
y = data_filtered['3連複_結果']

# データをシャッフルせずに前半8割を学習データ、後半2割をテストデータに分割
split_index = int(len(X) * 0.8)
X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]

# 各モデルのハイパーパラメータ設定
param_grids = {
    "LogisticRegression": {
        "C": [0.01, 0.1, 1, 10],
        "penalty": ['l2'],
        "solver": ['lbfgs'],
        "max_iter": [100, 200, 500]
    },
    "RandomForest": {
        "n_estimators": [100, 200, 300],
        "max_depth": [None, 10, 20],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
        "bootstrap": [True, False]
    },
    "GradientBoosting": {
        "n_estimators": [100, 200],
        "learning_rate": [0.01, 0.1],
        "max_depth": [3, 5],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2]
    },
    # "SVM": {
    #     "C": [1, 10],
    #     "kernel": ['linear', 'rbf'],
    #     "gamma": ['scale', 0.1, 1]
    # },
    "LightGBM": {
        "num_leaves": [31, 50],
        "learning_rate": [0.01, 0.1],
        "n_estimators": [100, 200],
        "min_child_samples": [20, 50]
    }
}

# モデルリストの定義
models = {
    "LogisticRegression": LogisticRegression(random_state=42),
    "RandomForest": RandomForestClassifier(random_state=42),
    "GradientBoosting": GradientBoostingClassifier(random_state=42),
    "SVM": SVC(probability=True, random_state=42),
    "LightGBM": LGBMClassifier(random_state=42)
}

# 各モデルの評価結果を保存するためのリスト
results = []

# 各モデルのチューニングと評価
for model_name, model in models.items():
    print(f"モデル: {model_name}")
    
    # ハイパーパラメーターチューニング
    grid_search = GridSearchCV(estimator=model,
                               param_grid=param_grids[model_name],
                               scoring='accuracy',
                               cv=3,
                               verbose=2,
                               n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    # 最適なモデルを取得
    best_model = grid_search.best_estimator_
    print(f"{model_name} の最適パラメーター: {grid_search.best_params_}")
    
    # モデルの評価
    y_pred = best_model.predict(X_test)
    y_pred_proba = best_model.predict_proba(X_test)[:, 1]
    
    accuracy = accuracy_score(y_test, y_pred)
    auc_score = roc_auc_score(y_test, y_pred_proba)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # 結果を保存
    results.append({
        "モデル": model_name,
        "Accuracy": accuracy,
        "AUC": auc_score,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })

# 結果をデータフレームに変換
results_df = pd.DataFrame(results)

# 結果を表示
print("モデルの性能比較結果:")
print(results_df)

# 必要に応じてCSVに保存
results_df.to_csv("model_comparison_results.csv", index=False)

# 棒グラフの描画
results_df.set_index("モデル").plot(kind='bar', figsize=(12, 6))
plt.title("モデル性能比較")
plt.ylabel("スコア")
plt.xlabel("モデル")
plt.legend(loc="best")
plt.show()
