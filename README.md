# Boatrace_prediction

ボートレースにおける枠ごとの結果を予測するプロジェクト

## 目的
3着ごとに入るか入らないか（舟券に絡むか否か）を予想する。


## 検証方法



## 実行方法
### データ準備
1. 出走表データと結果データを結合（scripts\data_marged.py）

### モデルの訓練（コースごと）
<!-- 以下は現在コースごとだが、関数化してまとめる予定 -->
2. データ内の各値をZスコアに変換（scripts\data_preprocessing.py）
3. 訓練モデルをトレーニング（scripts_by_course\boto1\train_model.py）

### 検証
4. データの一部を検証用に用いる、訓練されたモデルを用いて予測データを作成（scrpits_verification\verification_preprocessing.py）
5. 予測データと結果データ、オッズデータを結合する（scrpits_verification\test_data_marged.py）
6. 作成されたデータをもとに、回収率を計算する（scrpits_verification\verification_test2.py）
 