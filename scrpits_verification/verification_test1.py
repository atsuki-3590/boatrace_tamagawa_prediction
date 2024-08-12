import pandas as pd
from itertools import combinations

# データの読み込み
predict_data = pd.read_csv('data/processed/test_predict_with_odds.csv')

# 'predict_result_{i}'の各カラムで1が3つあるデータの抽出
predict_columns = [f'predict_result_{i}' for i in range(1, 7)]
predict_data['count_ones'] = predict_data[predict_columns].sum(axis=1)

# '1'がちょうど3つのデータのカウント
count_three_ones = (predict_data['count_ones'] == 3).sum()

# 1が3つのデータを抽出
three_ones_data = predict_data[predict_data['count_ones'] == 3]

print(count_three_ones)

# すべてのペアが一致しているデータをフィルタリング
matches = (predict_data['predict_result_1'] == predict_data['result_1']) & \
          (predict_data['predict_result_2'] == predict_data['result_2']) & \
          (predict_data['predict_result_3'] == predict_data['result_3']) & \
          (predict_data['predict_result_4'] == predict_data['result_4']) & \
          (predict_data['predict_result_5'] == predict_data['result_5']) & \
          (predict_data['predict_result_6'] == predict_data['result_6'])

# 完全に一致しているデータの数をカウント
total_matches = matches.sum()

print(total_matches)

# すべての predict_result と result が一致するデータを抽出
filtered_data = predict_data[matches]

# 6つから3つを選ぶ組み合わせのリストを生成
combinations_of_three = list(combinations(range(1, 7), 3))

# パターンリストの生成
patterns = [
    {'columns': list(comb), 'odds_column': f"{'='.join(map(str, comb))}"}
    for comb in combinations_of_three
]

# 合計オッズを計算
total_payout = 0
for pattern in patterns:
    # 各カラムの一致条件を作成
    match_condition = filtered_data.copy()
    for i in pattern['columns']:
        match_condition = match_condition[match_condition[f'predict_result_{i}'] == 1]
    for i in range(1, 7):
        if i not in pattern['columns']:
            match_condition = match_condition[match_condition[f'predict_result_{i}'] == 0]

    # 該当するデータのオッズを合計
    if not match_condition.empty:
        odds_to_sum = match_condition[pattern['odds_column']].sum()
        total_payout += odds_to_sum

print(f"Total payout based on specific conditions: {total_payout}")
