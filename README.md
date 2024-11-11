# Boatrace_prediction

ボートレースにおける枠ごとの結果を予測するプロジェクト

## 目的
3着ごとに入るか入らないか（舟券に絡むか否か）を予想する。


## 検証方法
### 前準備
1. config.iniにファイルパスを設定する（config_sample.iniをコピーし、名前を変更して使用）


### データ準備
1. 出走表データ（info.csv）と結果データ（result.csv）を結合してmerged_data.csvに（scripts\data_marged.py）

2. データ内の予想に必要ないデータ（選手名や登録番号など）を削除し、枠番ごとのデータを作成。特徴量エンジニアリング（勝率などのZスコア変換や風向の変換など）もここで行う（merged_dataからdata_boat1.csvを作成）。（scripts\data_by_course.py）


### モデルの訓練（コースごと）
<!-- 以下は現在コースごとだが、関数化してまとめる予定 -->
3. 予想に必要な特徴量を選定（data_boat1.csvからmodified_data1.csvを作成）。（scripts_by_course\boat1\data_preprocessing.py（scripts\data_preprocessing.pyは全体をまとめて処理したいとき））

4. 訓練モデルをトレーニング（scripts_by_course\boat1\train_model.py）
※ scripts_by_course\boat1\test.pyについては、3~4をまとめている。用いる特徴量やオーバーサンプリングなどのテストを行った。


### 検証
5. データの一部を検証用に用いる、訓練されたモデルを用いて予測データ（data\processed\test_predictions_boat1.csv）を作成（scrpits_verification\verification_preprocessing.py）

6. 予測データ（data\processed\test_predictions_boat1.csv）と結果データ（data\processed\data_boat1.csv）、オッズデータ（data\raw\odds_3f.csv）を結合する（data\processed\test_predict_with_odds.csvを作成）（scrpits_verification\test_data_marged.py）

7. 作成されたデータをもとに、回収率を計算する（scrpits_verification\verification_test2.py）
※ 最低購入オッズを考慮したいときは、scrpits_verification\minimum_purchase_odds.pyを用いる。
 


## 今後の予定
個別のレースで予想をできるようにする（just_before_prediction）。


## 現在
"scripts_by_course\boat1\test_hyperparameter_05.py"でハイパーパラメーターチューニングを実行
"scripts_by_course\boat1\memo_05.md"に記録。