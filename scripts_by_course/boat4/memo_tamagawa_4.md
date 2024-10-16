# 4号艇の複勝予測に関するドキュメント
最良のハイパーパラメーター: {'bootstrap': True, 'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 300}

カスタム閾値: 0.1
Accuracy: 0.45819397993311034
AUC Score: 0.6825093378795152
Classification Report:
              precision    recall  f1-score   support

           0       0.50      0.00      0.00      1134
           1       0.46      1.00      0.63       959

    accuracy                           0.46      2093
   macro avg       0.48      0.50      0.31      2093
weighted avg       0.48      0.46      0.29      2093

Confusion Matrix:
[[   1 1133]
 [   1  958]]
カスタム閾値: 0.2
Accuracy: 0.4968944099378882
AUC Score: 0.6825093378795152
Classification Report:
              precision    recall  f1-score   support

           0       0.80      0.09      0.17      1134
           1       0.48      0.97      0.64       959

    accuracy                           0.50      2093
   macro avg       0.64      0.53      0.40      2093
weighted avg       0.65      0.50      0.38      2093

Confusion Matrix:
[[ 107 1027]
 [  26  933]]
カスタム閾値: 0.30000000000000004
Accuracy: 0.5585284280936454
AUC Score: 0.6825093378795152
Classification Report:
              precision    recall  f1-score   support

           0       0.76      0.27      0.40      1134
           1       0.51      0.90      0.65       959

    accuracy                           0.56      2093
   macro avg       0.63      0.58      0.53      2093
weighted avg       0.64      0.56      0.52      2093

Confusion Matrix:
[[309 825]
 [ 99 860]]
カスタム閾値: 0.4
Accuracy: 0.6115623506927855
AUC Score: 0.6825093378795152
Classification Report:
              precision    recall  f1-score   support

           0       0.69      0.51      0.59      1134
           1       0.56      0.73      0.63       959

    accuracy                           0.61      2093
   macro avg       0.62      0.62      0.61      2093
weighted avg       0.63      0.61      0.61      2093

Confusion Matrix:
[[580 554]
 [259 700]]
カスタム閾値: 0.5
Accuracy: 0.6493072145246058
AUC Score: 0.6825093378795152
Classification Report:
              precision    recall  f1-score   support

           0       0.67      0.71      0.69      1134
           1       0.63      0.58      0.60       959

    accuracy                           0.65      2093
   macro avg       0.65      0.64      0.64      2093
weighted avg       0.65      0.65      0.65      2093

Confusion Matrix:
[[805 329]
 [405 554]]
カスタム閾値: 0.6000000000000001
Accuracy: 0.6220735785953178
AUC Score: 0.6825093378795152
Classification Report:
              precision    recall  f1-score   support

           0       0.61      0.85      0.71      1134
           1       0.67      0.35      0.46       959

    accuracy                           0.62      2093
   macro avg       0.64      0.60      0.58      2093
weighted avg       0.63      0.62      0.59      2093

Confusion Matrix:
[[966 168]
 [623 336]]
カスタム閾値: 0.7000000000000001
Accuracy: 0.57955088389871
AUC Score: 0.6825093378795152
Classification Report:
              precision    recall  f1-score   support

           0       0.57      0.96      0.71      1134
           1       0.72      0.13      0.23       959

    accuracy                           0.58      2093
   macro avg       0.64      0.55      0.47      2093
weighted avg       0.64      0.58      0.49      2093

Confusion Matrix:
[[1085   49]
 [ 831  128]]
カスタム閾値: 0.8
Accuracy: 0.5475394171046345
AUC Score: 0.6825093378795152
Classification Report:
              precision    recall  f1-score   support

           0       0.55      0.99      0.70      1134
           1       0.75      0.02      0.04       959

    accuracy                           0.55      2093
   macro avg       0.65      0.51      0.37      2093
weighted avg       0.64      0.55      0.40      2093

Confusion Matrix:
[[1128    6]
 [ 941   18]]
カスタム閾値: 0.9
C:\Users\atsuk\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\sklearn\metrics\_classification.py:1531: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\atsuk\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\sklearn\metrics\_classification.py:1531: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\atsuk\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\sklearn\metrics\_classification.py:1531: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
Accuracy: 0.5418060200668896
AUC Score: 0.6825093378795152
Classification Report:
              precision    recall  f1-score   support

           0       0.54      1.00      0.70      1134
           1       0.00      0.00      0.00       959

    accuracy                           0.54      2093
   macro avg       0.27      0.50      0.35      2093
weighted avg       0.29      0.54      0.38      2093

Confusion Matrix:
[[1134    0]
 [ 959    0]]
C:\Users\atsuk\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\sklearn\metrics\_classification.py:1531: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\atsuk\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\sklearn\metrics\_classification.py:1531: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\atsuk\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\sklearn\metrics\_classification.py:1531: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
Accuracy: 0.5418060200668896
AUC Score: 0.6825093378795152
Classification Report:
              precision    recall  f1-score   support

           0       0.54      1.00      0.70      1134
           1       0.00      0.00      0.00       959

    accuracy                           0.54      2093
   macro avg       0.27      0.50      0.35      2093
weighted avg       0.29      0.54      0.38      2093

Confusion Matrix:
[[1134    0]
 [ 959    0]]
モデルのトレーニングが完了しました
             特徴量       重要度
2      全国勝率_Zスコア  0.232351
3    全国2連対率_Zスコア  0.177330
7      当地勝率_Zスコア  0.127688
6    当地2連対率_Zスコア  0.113967
8     展示タイム_Zスコア  0.109390
4  モーター2連対率_Zスコア  0.092047
5   ボート2連対率_Zスコア  0.087424
1             体重  0.045368
0             天気  0.014435



# 考察
用語解説
正確性（Accuracy）：モデルが全体的にどれだけ正確に予測できるかを示します。
精度（Precision）：正と予測された中で、実際に正である割合。
再現率（Recall）：実際に正であるデータの中で、正と予測された割合。
F1スコア：精度と再現率の調和平均で、バランスの取れたモデルの性能を示します。

どれが大切か考える。
Recallが高いほど、実際の1の結果を多めに捉える。そう考えると、1のRecallが高く、バランスも良い通常時のモデルがよさそう？
0の精度が低い（0と予想したとき50%しか正解していない）のは少し問題？

2連対率については、あってもなくても結果がそこまで変わらないので、なくてよさそう。

枠ごとの特徴量は偏差値（Zスコア）のほうがいい。

全国勝率も当地勝率もあった方がいい。


勝率と2連率どちらを用いるかは非常に難しい。

1号艇が複勝する場合の予測の正確さを最優先する場合、通常時のモデルが適している。
これは、高いAccuracyと非常に高いクラス1の再現率により、ほとんどの複勝を正確に捉えることができるためである。

クラス0とクラス1の成績のバランスを取ることが重要な場合（つまり、1号艇が複勝しない場合の予測も重要視する場合）、2連率のみのモデルが適している。
このモデルは、両クラスの成績が比較的均等であり、よりバランスの取れた予測を提供する。

多く買ってたくさん的中を目指すか、絞って穴を狙うかに近い。





