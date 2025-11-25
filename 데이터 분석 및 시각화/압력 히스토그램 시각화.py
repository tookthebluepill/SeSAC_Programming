import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")

df = pd.read_csv("04_etching_process_1.csv")
print(df.head())

good_pressure = df[df['result'] == 'Good']['pressure']
print(good_pressure.head())
bad_pressure = df[df['result'] == 'Bad']['pressure']
print(bad_pressure.head())

#좋은 웨이퍼 히스토그램 그리기
plt.figure(figsize=(12, 6))
sns.histplot(
    good_pressure,
    bins=20,
    kde=True,
    alpha=0.6,
    label='Good',
    color='green'
)

#나쁜 웨이퍼 히스토그램 그리기
sns.histplot(
    bad_pressure,
    bins=20,
    kde=True,
    alpha=0.6,
    label='Bad',
    color='red'
)

plt.title('Pressure Distribution for Good vs Bad Wafers')
plt.xlabel('Pressure')
plt.ylabel('Number of Wafers')
plt.legend()
print(plt.show())