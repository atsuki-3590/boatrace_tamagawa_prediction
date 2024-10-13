# 1号艇の複勝予測に関するドキュメント
test_size=0.2, random_state=42

1号艇データは少し偏りが大きいため、アンダーサンプリングとオーバーサンプリングを試してみた。


## 通常時
Custom_threshold: 0.5
Accuracy: 0.6168204248015448
AUC Score: 0.6433845082706378
Classification Report:
              precision    recall  f1-score   support

           0       0.60      0.53      0.56      2155
           1       0.63      0.69      0.66      2506

    accuracy                           0.62      4661
   macro avg       0.61      0.61      0.61      4661
weighted avg       0.62      0.62      0.61      4661


Custom_threshold: 0.4
Accuracy: 0.5942930701566187
AUC Score: 0.6433845082706378
Classification Report:
              precision    recall  f1-score   support

           0       0.63      0.30      0.40      2155
           1       0.58      0.85      0.69      2506

    accuracy                           0.59      4661
   macro avg       0.61      0.57      0.55      4661
weighted avg       0.61      0.59      0.56      4661


Custom_threshold: 0.3
Accuracy: 0.5653293284702854
AUC Score: 0.6433845082706378
Classification Report:
              precision    recall  f1-score   support

           0       0.68      0.11      0.19      2155
           1       0.56      0.95      0.70      2506

    accuracy                           0.57      4661
   macro avg       0.62      0.53      0.45      4661
weighted avg       0.61      0.57      0.47      4661


### 勝率あり、2連対率あり
Custom_threshold: 0.5
Accuracy: 0.6171673819742489
AUC Score: 0.6490861432587262
Classification Report:
              precision    recall  f1-score   support

           0       0.60      0.52      0.56      2155
           1       0.63      0.70      0.66      2505

    accuracy                           0.62      4660
   macro avg       0.61      0.61      0.61      4660
weighted avg       0.62      0.62      0.61      4660


Custom_threshold: 0.4
Accuracy: 0.6
AUC Score: 0.6490861432587262
Classification Report:
              precision    recall  f1-score   support

           0       0.64      0.30      0.41      2155
           1       0.59      0.86      0.70      2505

    accuracy                           0.60      4660
   macro avg       0.62      0.58      0.55      4660
weighted avg       0.61      0.60      0.57      4660





勝率無し、2連率あり



Zスコア無し、2連対率無し




## オーバーサンプリング
### 勝率あり、2連対率なし
Custom_threshold: 0.5
Accuracy: 0.609525852821283
AUC Score: 0.6441606501704494
Classification Report:
              precision    recall  f1-score   support

           0       0.58      0.57      0.57      2155
           1       0.63      0.65      0.64      2506

    accuracy                           0.61      4661
   macro avg       0.61      0.61      0.61      4661
weighted avg       0.61      0.61      0.61      4661



### 勝率あり、2連対率あり



## アンダーサンプリング
### 勝率あり、2連対率なし
Custom_threshold: 0.5
Accuracy: 0.6075949367088608
AUC Score: 0.6418100040181985
Classification Report:
              precision    recall  f1-score   support

           0       0.57      0.59      0.58      2155
           1       0.64      0.62      0.63      2506

    accuracy                           0.61      4661
   macro avg       0.61      0.61      0.61      4661
weighted avg       0.61      0.61      0.61      4661



### 勝率あり、2連対率あり



## LightGBM ハイパーパラメーターチューニング
Best parameters found: {'boosting_type': 'gbdt', 'learning_rate': 0.1, 'n_estimators': 500, 'num_leaves': 70}

accuracy:


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





