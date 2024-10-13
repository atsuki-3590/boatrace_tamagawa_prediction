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
base_file_path = f"{processed_dir}data_boat1.csv"
df = pd.read_csv(base_file_path, low_memory=False)

# 削除する列を指定
columns_to_drop_place = [
    'レースコード', '枠', '順位', '結果', '天気', '体重',
    '全国勝率', 'モーター2連対率', 'ボート2連対率', '当地勝率', '展示タイム',
    '全国2連対率', '当地2連対率',
    '全国2連対率_Zスコア', '当地2連対率_Zスコア'
]

# 指定した列を削除
new_data = df.drop(columns=columns_to_drop_place)

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

# 特徴量とターゲットに分ける
X = data_filtered.drop(columns=['3連複_結果'])
y = data_filtered['3連複_結果']

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False) 

print("データ前処理が完了しました")



def train_and_evaluate_model(X_train, y_train, X_test, y_test, sampling_strategy=None, custom_threshold=0.5):
    # モデルのインスタンス化
    model = RandomForestClassifier(random_state=42)
    
    # サンプリングの適用
    if sampling_strategy == 'smote':
        sm = SMOTE(random_state=42)
        X_train, y_train = sm.fit_resample(X_train, y_train)
    elif sampling_strategy == 'undersample':
        rus = RandomUnderSampler(random_state=42)
        X_train, y_train = rus.fit_resample(X_train, y_train)
    
    # モデルの訓練
    model.fit(X_train, y_train)
    
    # 予測と評価
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_pred_proba >= custom_threshold).astype(int)
    
    accuracy = accuracy_score(y_test, y_pred)
    auc_score = roc_auc_score(y_test, y_pred_proba)
    report = classification_report(y_test, y_pred, output_dict=True)
    
    return {
        'model': model,
        'accuracy': accuracy,
        'auc_score': auc_score,
        'report': report,
        'y_pred': y_pred,
        'y_pred_proba': y_pred_proba
    }

# ベースラインモデル
results_baseline = train_and_evaluate_model(X_train, y_train, X_test, y_test, custom_threshold=0.5)
# オーバーサンプリング
results_smote = train_and_evaluate_model(X_train, y_train, X_test, y_test, sampling_strategy='smote', custom_threshold=0.5)
# アンダーサンプリング
results_undersample = train_and_evaluate_model(X_train, y_train, X_test, y_test, sampling_strategy='undersample', custom_threshold=0.5)

# 各モデルの結果を表示
print("Baseline Model")
print(f"Accuracy: {results_baseline['accuracy']}")
print(f"AUC Score: {results_baseline['auc_score']}")
print(f"Classification Report: \n{results_baseline['report']}")

print("\nSMOTE Model")
print(f"Accuracy: {results_smote['accuracy']}")
print(f"AUC Score: {results_smote['auc_score']}")
print(f"Classification Report: \n{results_smote['report']}")

print("\nUndersample Model")
print(f"Accuracy: {results_undersample['accuracy']}")
print(f"AUC Score: {results_undersample['auc_score']}")
print(f"Classification Report: \n{results_undersample['report']}")



# "0"のPrecisionが高いモデルの結果を表示
precision_0_baseline = results_baseline['report']['0']['precision']
precision_0_smote = results_smote['report']['0']['precision']
precision_0_undersample = results_undersample['report']['0']['precision']

best_precision_0_model = max(
    ('Baseline', precision_0_baseline),
    ('SMOTE', precision_0_smote),
    ('Undersample', precision_0_undersample),
    key=lambda x: x[1]
)

print(f"\n'0'のPrecisionが最も高いモデル: {best_precision_0_model[0]} (Precision: {best_precision_0_model[1]})")




def plot_roc_curve(y_test, y_pred_proba, title):
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('偽陽性率')
    plt.ylabel('真陽性率')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.show()

plot_roc_curve(y_test, results_baseline['y_pred_proba'], 'Baseline Model ROC Curve')
plot_roc_curve(y_test, results_smote['y_pred_proba'], 'SMOTE Model ROC Curve')
plot_roc_curve(y_test, results_undersample['y_pred_proba'], 'Undersample Model ROC Curve')
