カスタム閾値：0.6 (or 0.5)


最良のハイパーパラメーター: {'bootstrap': True, 'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 200}
カスタム閾値: 0.1
Accuracy: 0.43751603797793176
AUC Score: 0.7146969923499736
Classification Report:
              precision    recall  f1-score   support

           0       0.95      0.22      0.36      5546
           1       0.34      0.97      0.50      2248

    accuracy                           0.44      7794
   macro avg       0.64      0.60      0.43      7794
weighted avg       0.77      0.44      0.40      7794

Confusion Matrix:
[[1225 4321]
 [  63 2185]]
カスタム閾値: 0.2
Accuracy: 0.5579933282011804
AUC Score: 0.7146969923499736
Classification Report:
              precision    recall  f1-score   support

           0       0.86      0.45      0.59      5546
           1       0.38      0.82      0.52      2248

    accuracy                           0.56      7794
   macro avg       0.62      0.64      0.55      7794
weighted avg       0.72      0.56      0.57      7794

Confusion Matrix:
[[2497 3049]
 [ 396 1852]]
カスタム閾値: 0.30000000000000004
Accuracy: 0.6454965357967667
AUC Score: 0.7146969923499736
Classification Report:
              precision    recall  f1-score   support

           0       0.82      0.64      0.72      5546
           1       0.43      0.65      0.51      2248

    accuracy                           0.65      7794
   macro avg       0.62      0.65      0.62      7794
weighted avg       0.71      0.65      0.66      7794

Confusion Matrix:
[[3569 1977]
 [ 786 1462]]
カスタム閾値: 0.4
Accuracy: 0.7082371054657429
AUC Score: 0.7146969923499736
Classification Report:
              precision    recall  f1-score   support

           0       0.79      0.80      0.80      5546
           1       0.49      0.48      0.49      2248

    accuracy                           0.71      7794
   macro avg       0.64      0.64      0.64      7794
weighted avg       0.71      0.71      0.71      7794

Confusion Matrix:
[[4440 1106]
 [1168 1080]]
カスタム閾値: 0.5
Accuracy: 0.7286374133949192
AUC Score: 0.7146969923499736
Classification Report:
              precision    recall  f1-score   support

           0       0.76      0.91      0.83      5546
           1       0.56      0.29      0.38      2248

    accuracy                           0.73      7794
   macro avg       0.66      0.60      0.60      7794
weighted avg       0.70      0.73      0.70      7794

Confusion Matrix:
[[5038  508]
 [1607  641]]
カスタム閾値: 0.6000000000000001
Accuracy: 0.7253015139851168
AUC Score: 0.7146969923499736
Classification Report:
              precision    recall  f1-score   support

           0       0.74      0.96      0.83      5546
           1       0.60      0.15      0.24      2248

    accuracy                           0.73      7794
   macro avg       0.67      0.55      0.53      7794
weighted avg       0.70      0.73      0.66      7794

Confusion Matrix:
[[5320  226]
 [1915  333]]
カスタム閾値: 0.7000000000000001
Accuracy: 0.7187580189889659
AUC Score: 0.7146969923499736
Classification Report:
              precision    recall  f1-score   support

           0       0.72      0.99      0.83      5546
           1       0.67      0.05      0.09      2248

    accuracy                           0.72      7794
   macro avg       0.69      0.52      0.46      7794
weighted avg       0.71      0.72      0.62      7794

Confusion Matrix:
[[5491   55]
 [2137  111]]
カスタム閾値: 0.8
Accuracy: 0.7131126507569926
AUC Score: 0.7146969923499736
Classification Report:
              precision    recall  f1-score   support

           0       0.71      1.00      0.83      5546
           1       0.80      0.01      0.01      2248

    accuracy                           0.71      7794
   macro avg       0.76      0.50      0.42      7794
weighted avg       0.74      0.71      0.60      7794

Confusion Matrix:
[[5542    4]
 [2232   16]]
カスタム閾値: 0.9
Accuracy: 0.7120862201693611
AUC Score: 0.7146969923499736
Classification Report:
              precision    recall  f1-score   support

           0       0.71      1.00      0.83      5546
           1       1.00      0.00      0.00      2248

    accuracy                           0.71      7794
   macro avg       0.86      0.50      0.42      7794
weighted avg       0.80      0.71      0.59      7794

Confusion Matrix:
[[5546    0]
 [2244    4]]
Accuracy: 0.7120862201693611
AUC Score: 0.7146969923499736
Classification Report:
              precision    recall  f1-score   support

           0       0.71      1.00      0.83      5546
           1       1.00      0.00      0.00      2248

    accuracy                           0.71      7794
   macro avg       0.86      0.50      0.42      7794
weighted avg       0.80      0.71      0.59      7794

Confusion Matrix:
[[5546    0]
 [2244    4]]
モデルのトレーニングが完了しました
             特徴量       重要度
2      全国勝率_Zスコア  0.196205
3    全国2連対率_Zスコア  0.148856
7      当地勝率_Zスコア  0.135277
6    当地2連対率_Zスコア  0.121497
8     展示タイム_Zスコア  0.115492
4  モーター2連対率_Zスコア  0.106230
5   ボート2連対率_Zスコア  0.104608
1             体重  0.052047
0             天気  0.019789