カスタム閾値：0.6 (or 0.5)


最良のハイパーパラメーター: {'bootstrap': True, 'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 300}
カスタム閾値: 0.1
Accuracy: 0.4648447523736207
AUC Score: 0.6666087532749196
Classification Report:
              precision    recall  f1-score   support

           0       0.67      0.00      0.00      4176
           1       0.46      1.00      0.63      3618

    accuracy                           0.46      7794
   macro avg       0.57      0.50      0.32      7794
weighted avg       0.57      0.46      0.30      7794

Confusion Matrix:
[[  10 4166]
 [   5 3613]]
カスタム閾値: 0.2
Accuracy: 0.5039774185270721
AUC Score: 0.6666087532749196
Classification Report:
              precision    recall  f1-score   support

           0       0.81      0.10      0.17      4176
           1       0.48      0.97      0.65      3618

    accuracy                           0.50      7794
   macro avg       0.65      0.54      0.41      7794
weighted avg       0.66      0.50      0.39      7794

Confusion Matrix:
[[ 406 3770]
 [  96 3522]]
カスタム閾値: 0.30000000000000004
Accuracy: 0.5617141390813446
AUC Score: 0.6666087532749196
Classification Report:
              precision    recall  f1-score   support

           0       0.74      0.28      0.41      4176
           1       0.52      0.89      0.65      3618

    accuracy                           0.56      7794
   macro avg       0.63      0.58      0.53      7794
weighted avg       0.64      0.56      0.52      7794

Confusion Matrix:
[[1167 3009]
 [ 407 3211]]
カスタム閾値: 0.4
Accuracy: 0.6014883243520657
AUC Score: 0.6666087532749196
Classification Report:
              precision    recall  f1-score   support

           0       0.67      0.51      0.58      4176
           1       0.56      0.71      0.62      3618

    accuracy                           0.60      7794
   macro avg       0.61      0.61      0.60      7794
weighted avg       0.62      0.60      0.60      7794

Confusion Matrix:
[[2120 2056]
 [1050 2568]]
カスタム閾値: 0.5
Accuracy: 0.6320246343341032
AUC Score: 0.6666087532749196
Classification Report:
              precision    recall  f1-score   support

           0       0.64      0.70      0.67      4176
           1       0.62      0.55      0.58      3618

    accuracy                           0.63      7794
   macro avg       0.63      0.63      0.63      7794
weighted avg       0.63      0.63      0.63      7794

Confusion Matrix:
[[2932 1244]
 [1624 1994]]
カスタム閾値: 0.6000000000000001
Accuracy: 0.6145753143443674
AUC Score: 0.6666087532749196
Classification Report:
              precision    recall  f1-score   support

           0       0.60      0.84      0.70      4176
           1       0.66      0.36      0.46      3618

    accuracy                           0.61      7794
   macro avg       0.63      0.60      0.58      7794
weighted avg       0.63      0.61      0.59      7794

Confusion Matrix:
[[3495  681]
 [2323 1295]]
カスタム閾値: 0.7000000000000001
Accuracy: 0.5719784449576597
AUC Score: 0.6666087532749196
Classification Report:
              precision    recall  f1-score   support

           0       0.56      0.94      0.70      4176
           1       0.67      0.15      0.25      3618

    accuracy                           0.57      7794
   macro avg       0.62      0.54      0.47      7794
weighted avg       0.61      0.57      0.49      7794

Confusion Matrix:
[[3905  271]
 [3065  553]]
カスタム閾値: 0.8
Accuracy: 0.5414421349756223
AUC Score: 0.6666087532749196
Classification Report:
              precision    recall  f1-score   support

           0       0.54      0.99      0.70      4176
           1       0.74      0.02      0.04      3618

    accuracy                           0.54      7794
   macro avg       0.64      0.51      0.37      7794
weighted avg       0.63      0.54      0.39      7794

Confusion Matrix:
[[4153   23]
 [3551   67]]
カスタム閾値: 0.9
Accuracy: 0.5364382858609187
AUC Score: 0.6666087532749196
Classification Report:
              precision    recall  f1-score   support

           0       0.54      1.00      0.70      4176
           1       1.00      0.00      0.00      3618

    accuracy                           0.54      7794
   macro avg       0.77      0.50      0.35      7794
weighted avg       0.75      0.54      0.38      7794

Confusion Matrix:
[[4176    0]
 [3613    5]]
Accuracy: 0.5364382858609187
AUC Score: 0.6666087532749196
Classification Report:
              precision    recall  f1-score   support

           0       0.54      1.00      0.70      4176
           1       1.00      0.00      0.00      3618

    accuracy                           0.54      7794
   macro avg       0.77      0.50      0.35      7794
weighted avg       0.75      0.54      0.38      7794

Confusion Matrix:
[[4176    0]
 [3613    5]]
モデルのトレーニングが完了しました
             特徴量       重要度
2      全国勝率_Zスコア  0.253531
3    全国2連対率_Zスコア  0.182173
7      当地勝率_Zスコア  0.128113
6    当地2連対率_Zスコア  0.109681
8     展示タイム_Zスコア  0.102995
4  モーター2連対率_Zスコア  0.089161
5   ボート2連対率_Zスコア  0.077828
1             体重  0.043404
0             天気  0.013113