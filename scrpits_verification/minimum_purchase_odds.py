# 予測の検証用スクリプト

import pandas as pd

# Data for the values associated with each number
data = {
    1: 0.82,
    2: 0.64,
    3: 0.58,
    4: 0.68,
    5: 0.56,
    6: 0.52
}

# Generating combinations and calculating the products
combinations = []
products = []
for i in range(1, 7):
    for j in range(i+1, 7):
        for k in range(j+1, 7):
            combinations.append(f"{i}={j}={k}")
            products.append(data[i] * data[j] * data[k])

# Creating a DataFrame to display the results
result_df = pd.DataFrame({
    "Combination": combinations,
    "Product": products
})

# Calculating the inverse of the products
result_df['Inverse Product'] = 1 / result_df['Product']
result_df.drop('Product', axis=1, inplace=True)

print(result_df)