# import pandas as pd
# from functools import reduce
# import sys
# import os

# script_dir = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.dirname(script_dir)
# if project_root not in sys.path:
#     sys.path.append(project_root)

# from path_read_def import read_config
# from race_studium_data import race_course_to_course_number

# race_stadium = "多摩川"
# course_number_str = race_course_to_course_number[race_stadium]
# course_number_int = int(course_number_str) 

# # processed = "processed"
# # processed = "processed_new"

# # 予測データが含まれる
# file_paths = [
#     read_config(f"BOAT1_PREDICTION_DATA_FILE_{course_number_str}"), 
#     read_config(f"BOAT2_PREDICTION_DATA_FILE_{course_number_str}"), 
#     read_config(f"BOAT3_PREDICTION_DATA_FILE_{course_number_str}"), 
#     read_config(f"BOAT4_PREDICTION_DATA_FILE_{course_number_str}"), 
#     read_config(f"BOAT5_PREDICTION_DATA_FILE_{course_number_str}"), 
#     read_config(f"BOAT6_PREDICTION_DATA_FILE_{course_number_str}")
# ]

# # 3連複結果の取得に必要
# result_file_paths = [
#     read_config(f"BOAT1_PROCESSED_DATA_FILE_{course_number_str}"), 
#     read_config(f"BOAT2_PROCESSED_DATA_FILE_{course_number_str}"), 
#     read_config(f"BOAT3_PROCESSED_DATA_FILE_{course_number_str}"), 
#     read_config(f"BOAT4_PROCESSED_DATA_FILE_{course_number_str}"), 
#     read_config(f"BOAT5_PROCESSED_DATA_FILE_{course_number_str}"), 
#     read_config(f"BOAT6_PROCESSED_DATA_FILE_{course_number_str}")
# ]

# # Predictions データの結合
# data_frames = []
# for idx, file_path in enumerate(file_paths, start=1):
#     df = pd.read_csv(file_path)
#     df = df[['レースコード', 'predict_result']].rename(columns={'predict_result': f'predict_result_{idx}'})
#     data_frames.append(df)

# predictions_df = reduce(lambda left, right: pd.merge(left, right, on='レースコード', how='inner'), data_frames)

# # Results データの結合
# result_data_frames = []
# for idx, file_path in enumerate(result_file_paths, start=1):
#     df = pd.read_csv(file_path)
#     df = df[['レースコード', '3連複_結果']].rename(columns={'3連複_結果': f'result_{idx}'})
#     result_data_frames.append(df)

# results_df = reduce(lambda left, right: pd.merge(left, right, on='レースコード', how='inner'), result_data_frames)

# # Predictions と Results の結合
# predictions_df = pd.merge(predictions_df, results_df, on='レースコード', how='inner')

# # オッズデータの追加
# odds_data = read_config("DATA_ODDS_NEW") #2020-2024の多摩川と、2024年前半の全場のオッズ
# final_df = pd.merge(predictions_df, odds_data, on='レースコード', how='inner')

# result_columns = [f'result_{i}' for i in range(1, 7)]
# final_df['result'] = final_df[result_columns].apply(lambda row: '='.join([str(i+1) for i, val in enumerate(row) if val == 1]), axis=1)

# final_df.drop(columns=result_columns, inplace=True)

# output_path = read_config(f"ODDS_MEARGED_FILE_{course_number_str}")
# final_df.to_csv(output_path, index=False)

# # 結果を確認
# print(final_df.head())




import pandas as pd
import sqlite3
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

from path_read_def import read_config
from race_studium_data import race_course_to_course_number

# SQLiteデータベースの準備
db_path = os.path.join(project_root, 'race_data.db')
conn = sqlite3.connect(db_path)

race_stadium = "多摩川"
course_number_str = race_course_to_course_number[race_stadium]
course_number_int = int(course_number_str)

# 予測データが含まれるファイルの読み込みと保存
file_paths = [
    read_config(f"BOAT1_PREDICTION_DATA_FILE_{course_number_str}"),
    read_config(f"BOAT2_PREDICTION_DATA_FILE_{course_number_str}"),
    read_config(f"BOAT3_PREDICTION_DATA_FILE_{course_number_str}"),
    read_config(f"BOAT4_PREDICTION_DATA_FILE_{course_number_str}"),
    read_config(f"BOAT5_PREDICTION_DATA_FILE_{course_number_str}"),
    read_config(f"BOAT6_PREDICTION_DATA_FILE_{course_number_str}")
]

# 各ファイルを読み込んでSQLiteに保存
for idx, file_path in enumerate(file_paths, start=1):
    df = pd.read_csv(file_path)
    df = df[['レースコード', 'predict_result']].rename(columns={'predict_result': f'predict_result_{idx}'})
    table_name = f'predictions_boat_{idx}'
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# 3連複結果の取得に必要なファイルの読み込みと保存
result_file_paths = [
    read_config(f"BOAT1_PROCESSED_DATA_FILE_{course_number_str}"),
    read_config(f"BOAT2_PROCESSED_DATA_FILE_{course_number_str}"),
    read_config(f"BOAT3_PROCESSED_DATA_FILE_{course_number_str}"),
    read_config(f"BOAT4_PROCESSED_DATA_FILE_{course_number_str}"),
    read_config(f"BOAT5_PROCESSED_DATA_FILE_{course_number_str}"),
    read_config(f"BOAT6_PROCESSED_DATA_FILE_{course_number_str}")
]

# 各ファイルを読み込んでSQLiteに保存
for idx, file_path in enumerate(result_file_paths, start=1):
    df = pd.read_csv(file_path)
    df = df[['レースコード', '3連複_結果']].rename(columns={'3連複_結果': f'result_{idx}'})
    table_name = f'results_boat_{idx}'
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# 予測データの結合クエリ
predictions_query = """
    SELECT p1.レースコード,
           p1.predict_result_1,
           p2.predict_result_2,
           p3.predict_result_3,
           p4.predict_result_4,
           p5.predict_result_5,
           p6.predict_result_6
    FROM predictions_boat_1 p1
    INNER JOIN predictions_boat_2 p2 ON p1.レースコード = p2.レースコード
    INNER JOIN predictions_boat_3 p3 ON p1.レースコード = p3.レースコード
    INNER JOIN predictions_boat_4 p4 ON p1.レースコード = p4.レースコード
    INNER JOIN predictions_boat_5 p5 ON p1.レースコード = p5.レースコード
    INNER JOIN predictions_boat_6 p6 ON p1.レースコード = p6.レースコード
"""

# 結果データの結合クエリ
results_query = """
    SELECT r1.レースコード,
           r1.result_1,
           r2.result_2,
           r3.result_3,
           r4.result_4,
           r5.result_5,
           r6.result_6
    FROM results_boat_1 r1
    INNER JOIN results_boat_2 r2 ON r1.レースコード = r2.レースコード
    INNER JOIN results_boat_3 r3 ON r1.レースコード = r3.レースコード
    INNER JOIN results_boat_4 r4 ON r1.レースコード = r4.レースコード
    INNER JOIN results_boat_5 r5 ON r1.レースコード = r5.レースコード
    INNER JOIN results_boat_6 r6 ON r1.レースコード = r6.レースコード
"""

# Predictions と Results を結合するクエリ
final_query = f"""
    SELECT p.*,
           r.result_1, r.result_2, r.result_3, r.result_4, r.result_5, r.result_6
    FROM ({predictions_query}) p
    INNER JOIN ({results_query}) r ON p.レースコード = r.レースコード
"""

# オッズデータの読み込みと確認
odds_data_path = read_config("DATA_ODDS_NEW")
odds_data = pd.read_csv(odds_data_path)
print(odds_data.columns)  # オッズデータの列名を確認

# 必要に応じて列名を修正し保存
odds_data.to_sql('odds_data', conn, if_exists='replace', index=False)

# 正しい列名を確認して修正（例：オッズ情報の列名が 'odds_value' だった場合）
odds_column_name = 'レースコード'  # 適切な列名に変更してください

# Predictions, Results, Odds を結合するクエリ
odds_query = f"""
    SELECT f.*, o.{odds_column_name}
    FROM ({final_query}) f
    INNER JOIN odds_data o ON f.レースコード = o.レースコード
"""

# チャンクサイズを指定してデータを少しずつ読み込む
chunk_size = 10000  # メモリに負担がかからないように1万行ずつ処理
chunks = []

for chunk in pd.read_sql_query(odds_query, conn, chunksize=chunk_size):
    # 必要な処理をチャンクごとに行う
    result_columns = [f'result_{i}' for i in range(1, 7)]
    chunk['result'] = chunk[result_columns].apply(lambda row: '='.join([str(i+1) for i, val in enumerate(row) if val == 1]), axis=1)
    chunk.drop(columns=result_columns, inplace=True)
    chunks.append(chunk)

# 全てのチャンクを結合して最終的なデータフレームにする
final_df = pd.concat(chunks, ignore_index=True)

# 最終データをCSVに保存
output_path = read_config(f"ODDS_MERGED_FILE_{course_number_str}")
final_df.to_csv(output_path, index=False)

# 結果を確認
print(final_df.head())

# データベース接続を閉じる
conn.close()
