import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv('04_etching_process_1.csv')
print(df.head())

equipment_table = pd.crosstab(
    df['equipment'],
    df['result']
)
print(equipment_table)
chi2, p, dof, expected = chi2_contingency(equipment_table)
print("실제 데이터(실제값)")
print(equipment_table)

print("\n카이제곱 통계량:", chi2)
print("\np-value(피밸류):", p)
print("\n자유도:", dof)