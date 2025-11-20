import pandas as pd

file_path = "02_oxide.csv"
oxide_df = pd.read_csv(file_path)

print(oxide_df)

#defect_count 값이 0인 데이터만 필터링(결함 X)
no_defect_df = oxide_df[oxide_df['defect_count'] == 0]
print(no_defect_df)
print(no_defect_df.describe())

#defect_count 값이 0보다 큰 데이터만 필터링(결함 O)
defect_df = oxide_df[oxide_df['defect_count'] > 0]
print(defect_df.describe())
defect_df = defect_df.sort_values(
    by='defect_count',
    ascending=False
)
print(defect_df)

high_defect_df = defect_df.head(10)
print(high_defect_df)
print(high_defect_df.describe())