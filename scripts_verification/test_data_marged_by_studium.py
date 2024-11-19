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
# odds_data = read_config("DATA_ODDS_05") #2020-2024の多摩川と、2024年前半の全場のオッズ
# final_df = pd.merge(predictions_df, odds_data, on='レースコード', how='inner')

# result_columns = [f'result_{i}' for i in range(1, 7)]
# final_df['result'] = final_df[result_columns].apply(lambda row: '='.join([str(i+1) for i, val in enumerate(row) if val == 1]), axis=1)

# final_df.drop(columns=result_columns, inplace=True)

# output_path = read_config(f"ODDS_MEARGED_FILE_{course_number_str}")
# final_df.to_csv(output_path, index=False)

# # 結果を確認
# print(final_df.head())



import pandas as pd
from functools import reduce
import sys
import os

# 初期設定とパスの取得
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

from path_read_def import read_config
from race_studium_data import race_course_to_course_number

race_stadium = "多摩川"
course_number_str = race_course_to_course_number[race_stadium]
course_number_int = int(course_number_str)

# ファイルパスの設定
file_paths = [
    read_config(f"BOAT1_PREDICTION_DATA_FILE_{course_number_str}"), 
    read_config(f"BOAT2_PREDICTION_DATA_FILE_{course_number_str}"), 
    read_config(f"BOAT3_PREDICTION_DATA_FILE_{course_number_str}"), 
    read_config(f"BOAT4_PREDICTION_DATA_FILE_{course_number_str}"), 
    read_config(f"BOAT5_PREDICTION_DATA_FILE_{course_number_str}"), 
    read_config(f"BOAT6_PREDICTION_DATA_FILE_{course_number_str}")
]

result_file_paths = [
    read_config(f"BOAT1_PROCESSED_DATA_FILE_{course_number_str}"), 
    read_config(f"BOAT2_PROCESSED_DATA_FILE_{course_number_str}"), 
    read_config(f"BOAT3_PROCESSED_DATA_FILE_{course_number_str}"), 
    read_config(f"BOAT4_PROCESSED_DATA_FILE_{course_number_str}"), 
    read_config(f"BOAT5_PROCESSED_DATA_FILE_{course_number_str}"), 
    read_config(f"BOAT6_PROCESSED_DATA_FILE_{course_number_str}")
]

# オッズデータを読み込み
odds_file_path = read_config(f"DATA_ODDS_{course_number_str}")
odds_data = pd.read_csv(odds_file_path)

# データ構造を確認
print(odds_data.head())
print(odds_data.columns)
odds_data['レースコード'] = odds_data['レースコード'].astype('category')

# 1000行ごとに書き出し
chunk_size = 100
output_path = read_config(f"ODDS_MEARGED_FILE_{course_number_str}")

# 結果ファイルのヘッダーを書き込む
with open(output_path, 'w') as f:
    header_written = False

    # Predictions データの結合
    data_frames = []
    for idx, file_path in enumerate(file_paths, start=1):
        df = pd.read_csv(file_path, usecols=['レースコード', 'predict_result'])  # 必要な列のみ読み込む
        df = df.drop_duplicates(subset='レースコード')  # レースコードで重複を削除
        df['レースコード'] = df['レースコード'].astype('category')
        df = df[['レースコード', 'predict_result']].astype({'predict_result': 'int8'}).rename(columns={'predict_result': f'predict_result_{idx}'})
        data_frames.append(df)

    predictions_df = reduce(lambda left, right: pd.merge(left, right, on='レースコード', how='inner'), data_frames)

    # Results データの結合
    result_data_frames = []
    for idx, file_path in enumerate(result_file_paths, start=1):
        df = pd.read_csv(file_path, usecols=['レースコード', '3連複_結果'])
        df = df.drop_duplicates(subset='レースコード')  # レースコードで重複を削除
        df['レースコード'] = df['レースコード'].astype('category')
        df = df[['レースコード', '3連複_結果']].astype({'3連複_結果': 'int8'}).rename(columns={'3連複_結果': f'result_{idx}'})
        result_data_frames.append(df)

    results_df = reduce(lambda left, right: pd.merge(left, right, on='レースコード', how='inner'), result_data_frames)

    # バッチごとにデータを結合し、ファイルに書き込む
    for i in range(0, len(predictions_df), chunk_size):
        # 1000行ずつ予測データを取り出す
        predictions_chunk = predictions_df.iloc[i:i + chunk_size]
        
        # 結果データと結合
        merged_chunk = pd.merge(predictions_chunk, results_df, on='レースコード', how='inner')

        # オッズデータの追加
        merged_chunk = pd.merge(merged_chunk, odds_data, on='レースコード', how='inner')

        # 結果の計算と不要な列の削除
        result_columns = [f'result_{i}' for i in range(1, 7)]
        merged_chunk['result'] = merged_chunk[result_columns].apply(lambda row: '='.join([str(i+1) for i, val in enumerate(row) if val == 1]), axis=1)
        merged_chunk.drop(columns=result_columns, inplace=True)

        # CSVに書き込み（初回はヘッダーを含む）
        if not header_written:
            merged_chunk.to_csv(f, mode='a', index=False)
            header_written = True
        else:
            merged_chunk.to_csv(f, mode='a', index=False, header=False)

        # 進捗を表示
        print(f"{i + chunk_size} 行まで処理完了")
