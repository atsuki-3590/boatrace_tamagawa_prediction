# 1号艇の複勝予測に関するドキュメント
test_size=0.2, random_state=42

1号艇データは少し偏りが大きいため、アンダーサンプリングとオーバーサンプリングを試してみた。


## 通常時
Custom_threshold: 0.8
Accuracy: 0.6369877708646213
AUC Score: 0.6678638730321885
Classification Report:
              precision    recall  f1-score   support

           0       0.28      0.60      0.38       860
           1       0.88      0.65      0.74      3801

    accuracy                           0.64      4661
   macro avg       0.58      0.62      0.56      4661
weighted avg       0.77      0.64      0.68      4661

Custom_threshold: 0.7
Accuracy: 0.742544518343703
AUC Score: 0.6678638730321885
Classification Report:
              precision    recall  f1-score   support

           0       0.32      0.35      0.34       860
           1       0.85      0.83      0.84      3801

    accuracy                           0.74      4661
   macro avg       0.59      0.59      0.59      4661
weighted avg       0.75      0.74      0.75      4661

Custom_threshold: 0.65
Accuracy: 0.777944647071444
AUC Score: 0.6678638730321885
Classification Report:
              precision    recall  f1-score   support

           0       0.35      0.24      0.29       860
           1       0.84      0.90      0.87      3801

    accuracy                           0.78      4661
   macro avg       0.60      0.57      0.58      4661
weighted avg       0.75      0.78      0.76      4661

Custom_threshold: 0.6
Accuracy: 0.794250160909676
AUC Score: 0.6678638730321885
Classification Report:
              precision    recall  f1-score   support

           0       0.37      0.16      0.22       860
           1       0.83      0.94      0.88      3801

    accuracy                           0.79      4661
   macro avg       0.60      0.55      0.55      4661
weighted avg       0.75      0.79      0.76      4661

Custom_threshold: 0.5
Accuracy: 0.8088393048701995
AUC Score: 0.6678638730321885
Classification Report:
              precision    recall  f1-score   support

           0       0.37      0.05      0.09       860
           1       0.82      0.98      0.89      3801

    accuracy                           0.81      4661
   macro avg       0.60      0.52      0.49      4661
weighted avg       0.74      0.81      0.74      4661

Custom_threshold: 0.4
Accuracy: 0.8148465994421797
AUC Score: 0.6678638730321885
Classification Report:
              precision    recall  f1-score   support

           0       0.44      0.01      0.02       860
           1       0.82      1.00      0.90      3801

    accuracy                           0.81      4661
   macro avg       0.63      0.50      0.46      4661
weighted avg       0.75      0.81      0.74      4661



2連対率あり
accuracy:0.8098712446351931, 
report              precision    recall  f1-score   support

           0       0.50      0.07      0.13       887
           1       0.82      0.98      0.89      3773

    accuracy                           0.81      4660
   macro avg       0.66      0.53      0.51      4660
weighted avg       0.76      0.81      0.75      4660


勝率無し、2連率あり
accuracy:0.7407725321888412, 
report              precision    recall  f1-score   support

           0       0.32      0.34      0.33       887
           1       0.84      0.84      0.84      3773

    accuracy                           0.74      4660
   macro avg       0.58      0.59      0.58      4660
weighted avg       0.74      0.74      0.74      4660


Zスコア無し、2連対率無し
accuracy:0.7752321981424148, 
report              precision    recall  f1-score   support

           0       0.32      0.19      0.24       901
           1       0.83      0.91      0.87      3944

    accuracy                           0.78      4845
   macro avg       0.58      0.55      0.56      4845
weighted avg       0.74      0.78      0.75      4845



## オーバーサンプリング
accuracy:0.7275262819137525, 
report              precision    recall  f1-score   support

           0       0.30      0.32      0.31       896
           1       0.84      0.82      0.83      3765

    accuracy                           0.73      4661
   macro avg       0.57      0.57      0.57      4661
weighted avg       0.73      0.73      0.73      4661


2連対率
accuracy:0.7369098712446351, 
report              precision    recall  f1-score   support

           0       0.32      0.35      0.34       887
           1       0.84      0.83      0.84      3773

    accuracy                           0.74      4660
   macro avg       0.58      0.59      0.59      4660
weighted avg       0.74      0.74      0.74      4660



## アンダーサンプリング
accuracy:0.6311950225273546, 
report              precision    recall  f1-score   support

           0       0.29      0.62      0.39       896
           1       0.88      0.63      0.74      3765

    accuracy                           0.63      4661
   macro avg       0.58      0.63      0.56      4661
weighted avg       0.76      0.63      0.67      4661


2連対率あり
accuracy:0.6454935622317597, 
report              precision    recall  f1-score   support

           0       0.29      0.61      0.40       887
           1       0.88      0.65      0.75      3773

    accuracy                           0.65      4660
   macro avg       0.58      0.63      0.57      4660
weighted avg       0.77      0.65      0.68      4660



## LightGBM ハイパーパラメーターチューニング
Best parameters found: {'boosting_type': 'gbdt', 'learning_rate': 0.1, 'n_estimators': 500, 'num_leaves': 70}

accuracy: 0.7554172924265179
report:               precision    recall  f1-score   support

           0       0.32      0.25      0.28       896
           1       0.83      0.88      0.85      3765

    accuracy                           0.76      4661
   macro avg       0.58      0.56      0.57      4661
weighted avg       0.73      0.76      0.74      4661


# 考察
用語解説
正確性（Accuracy）：モデルが全体的にどれだけ正確に予測できるかを示します。
精度（Precision）：正と予測された中で、実際に正である割合。
再現率（Recall）：実際に正であるデータの中で、正と予測された割合。
F1スコア：精度と再現率の調和平均で、バランスの取れたモデルの性能を示します。

どれが大切か考える。
Recallが高いほど、実際の1の結果を多めに捉える。そう考えると、Recallが高く、バランスも良い通常時のモデルがよさそう？
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





