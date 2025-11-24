import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")

df = pd.read_csv("04_etching_process_1.csv")
print(df.head())

#countplot 그리기
plt.figure(figsize=(12, 6))
sns.countplot(
     x='recipe',
     hue='result',
     data=df,
     palette={'Good':'green', 'Bad':'red'}
)

plt.title('Recipe vs Wafer Quality')
plt.xlabel('Recipe')
plt.ylabel('Number of Wafers')
plt.tight_layout()
print(plt.show())