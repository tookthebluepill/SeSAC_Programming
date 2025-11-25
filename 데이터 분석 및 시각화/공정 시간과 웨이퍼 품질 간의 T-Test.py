import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv('04_etching_process_1.csv')
print(df.head())
good_process_time = df[df['result'] == 'Good']['process_time'].dropna()
print(good_process_time.head())

bad_process_time = df[df['result'] == 'Bad']['process_time'].dropna()
print(bad_process_time.head())

print(good_process_time.mean())
print(bad_process_time.mean())

t_statistic, p_value = ttest_ind(
    good_process_time,
    bad_process_time,
    equal_var=False
)

print("T-통계량(T-statistic):", t_statistic)
print("p-value(피밸류):", p_value)