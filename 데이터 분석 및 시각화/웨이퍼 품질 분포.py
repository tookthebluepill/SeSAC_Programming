import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")

df = pd.read_csv("04_etching_process_1.csv")
print(df.head())

quality_counts = df['result'].value_counts()
print(quality_counts)
print(quality_counts.index)
print(quality_counts.values)


#파이차트 그리기
plt.figure(figsize=(10, 8))
plt.pie(
    quality_counts.values,
    labels=quality_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightgreen', 'lightcoral'],
    explode=[0.05, 0]
)

#파이차트가 원형으로 균일하게 보이도록 설정
plt.axis('equal')

plt.title('Wafer Quality Distribution (Good vs Bad)')
plt.show()