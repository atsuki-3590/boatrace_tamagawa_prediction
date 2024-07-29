# データ前処理
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# ファイルパスを変数に格納
raw_file_path = 'data/raw/merged_data.csv'
processed_dir = 'data/processed/'

os.makedirs(processed_dir, exist_ok=True)

modified_file_path = f"{processed_dir}data_by_course.csv"

df = pd.read_csv(raw_file_path, low_memory=False)

# 削除する列を指定
columns_to_drop = [
    '1枠_艇番', '2枠_艇番', '3枠_艇番', '4枠_艇番', '5枠_艇番', '6枠_艇番',
    '1枠_登録番号', '2枠_登録番号', '3枠_登録番号', '4枠_登録番号', '5枠_登録番号', '6枠_登録番号',
    '1枠_年齢', '2枠_年齢', '3枠_年齢', '4枠_年齢', '5枠_年齢', '6枠_年齢',
    '1枠_モーター番号', '2枠_モーター番号', '3枠_モーター番号', '4枠_モーター番号', '5枠_モーター番号', '6枠_モーター番号',
    '1枠_ボート番号', '2枠_ボート番号', '3枠_ボート番号', '4枠_ボート番号', '5枠_ボート番号', '6枠_ボート番号',
    '1枠_選手名', '2枠_選手名', '3枠_選手名', '4枠_選手名', '5枠_選手名', '6枠_選手名',
    '1枠_支部', '2枠_支部', '3枠_支部', '4枠_支部', '5枠_支部', '6枠_支部',
    '1着_登録番号', '2着_登録番号', '3着_登録番号', '4着_登録番号', '5着_登録番号', '6着_登録番号',
    '1着_着順', '2着_着順', '3着_着順', '4着_着順', '5着_着順', '6着_着順', 
    '1着_選手名', '2着_選手名', '3着_選手名', '4着_選手名', '5着_選手名', '6着_選手名',
    '1着_展示タイム', '2着_展示タイム', '3着_展示タイム', '4着_展示タイム', '5着_展示タイム', '6着_展示タイム',
    '1着_進入コース', '2着_進入コース', '3着_進入コース', '4着_進入コース', '5着_進入コース', '6着_進入コース', 
    '日次', 'レース日', '距離', '決まり手'
]

# 指定した列を削除
new_data = df.drop(columns=columns_to_drop)

print("データ前処理を開始します")

# 新しいカラムを追加
# new_data['1号艇勝敗'] = new_data['1着_艇番'].apply(lambda x: 1 if x == 1 else 0)


def transform_data(df):
    # 変換したデータを格納するリスト
    transformed_rows = []
    
    # 1行ずつループ
    for _, row in df.iterrows():
        for i in range(1, 7):
            # 枠別データ抽出
            frame_data = {
                '枠': i,
                '体重': row[f'{i}枠_体重'],
                '級別': row[f'{i}枠_級別'],
                '全国勝率': row[f'{i}枠_全国勝率'],
                '全国2連対率': row[f'{i}枠_全国2連対率'],
                '当地勝率': row[f'{i}枠_当地勝率'],
                '当地2連対率': row[f'{i}枠_当地2連対率'],
                'モーター2連対率': row[f'{i}枠_モーター2連対率'],
                'ボート2連対率': row[f'{i}枠_ボート2連対率']
            }
            # 共通データ抽出
            frame_data.update({
                'レースコード': row['レースコード'],
                'レース場': row['レース場'],
                'レース回': row['レース回'],
                '天気': row['天気'],
                '風向': row['風向'],
                '風速': row['風速'],
                '波の高さ': row['波の高さ'],
                # '距離': row['距離'],
                # '決まり手': row['決まり手'],
            })
            # 順位と結果を設定
            for j in range(1, 7):
                if row[f'{j}着_艇番'] == i:
                    frame_data['順位'] = int(j)
                    frame_data['結果'] = int(1 if j == 1 else 0)
                    frame_data['3連複_結果'] = int(1 if j >= 1 and 3 >= j else 0)
                    break

            transformed_rows.append(frame_data)

    transformed_df = pd.DataFrame(transformed_rows)
    # columns_order = ['レースコード', 'レース場', 'レース回', '天気', '風向', '風速', '波の高さ', '距離', '決まり手', '枠', '体重', '級別', '全国勝率', '全国2連対率', '当地勝率', '当地2連対率', 'モーター2連対率', 'ボート2連対率', '順位', '結果']
    columns_order = ['レースコード', 'レース場', 'レース回', '天気', '風向', '風速', '波の高さ', '枠', '体重', '級別', '全国勝率', '全国2連対率', '当地勝率', '当地2連対率', 'モーター2連対率', 'ボート2連対率', '順位', '結果', '3連複_結果']
    transformed_df = transformed_df[columns_order]

    return transformed_df


transformed_df = transform_data(new_data)

os.makedirs(processed_dir, exist_ok=True)
transformed_df.to_csv(modified_file_path, index=False)

print("データ前処理が完了しました")



# 1号艇のデータのみ抽出
boto1_df = transformed_df[transformed_df['枠'] == 1]
boto1_file_path = f"{processed_dir}data_boto1.csv"

# CSVファイルとして保存
transformed_df.to_csv(modified_file_path, index=False)
boto1_df.to_csv(boto1_file_path, index=False)

print("1号艇のデータを作成しました")