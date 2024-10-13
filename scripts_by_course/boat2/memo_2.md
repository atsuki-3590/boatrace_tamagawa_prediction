# 1号艇の複勝予測に関するドキュメント
test_size=0.2, random_state=42

1号艇データは少し偏りが大きいため、アンダーサンプリングとオーバーサンプリングを試してみた。


## 通常時
### 勝率あり、2連対率なし
Custom_threshold: 0.5
Accuracy: 0.6172495172709719
AUC Score: 0.6501732421989389
Classification Report:
              precision    recall  f1-score   support

           0       0.57      0.46      0.51      2008
           1       0.64      0.73      0.69      2653

    accuracy                           0.62      4661
   macro avg       0.61      0.60      0.60      4661
weighted avg       0.61      0.62      0.61      4661

Custom_threshold: 0.4
Accuracy: 0.6024458270757348
AUC Score: 0.6501732421989389
Classification Report:
              precision    recall  f1-score   support

           0       0.61      0.21      0.31      2008
           1       0.60      0.90      0.72      2653

    accuracy                           0.60      4661
   macro avg       0.61      0.55      0.52      4661
weighted avg       0.61      0.60      0.54      4661


### 勝率あり、2連対率あり
Custom_threshold: 0.4
Accuracy: 0.601931330472103
AUC Score: 0.6463324463135153
Classification Report:
              precision    recall  f1-score   support

           0       0.61      0.20      0.31      2007
           1       0.60      0.90      0.72      2653

    accuracy                           0.60      4660
   macro avg       0.61      0.55      0.51      4660
weighted avg       0.61      0.60      0.54      4660


勝率無し、2連率あり



Zスコア無し、2連対率無し




## オーバーサンプリング
### 勝率あり、2連対率なし
Custom_threshold: 0.4
Accuracy: 0.6063076593005793
AUC Score: 0.6471337604726214
Classification Report:
              precision    recall  f1-score   support

           0       0.58      0.32      0.41      2008
           1       0.62      0.82      0.70      2653

    accuracy                           0.61      4661
   macro avg       0.60      0.57      0.56      4661
weighted avg       0.60      0.61      0.58      4661


### 勝率あり、2連対率あり



## アンダーサンプリング
### 勝率あり、2連対率なし
Custom_threshold: 0.4
Accuracy: 0.6127440463419866
AUC Score: 0.6490576517901255
Classification Report:
              precision    recall  f1-score   support

           0       0.58      0.35      0.44      2008
           1       0.62      0.81      0.71      2653

    accuracy                           0.61      4661
   macro avg       0.60      0.58      0.57      4661
weighted avg       0.61      0.61      0.59      4661



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





