import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")

df = pd.read_csv("04_etching_process_1.csv")
print(df.head())

plt.figure(figsize=(15, 3))
sns.scatterplot(
    data=df,
    x='process_time',
    y='defect_count'
)

plt.title('Process Time vs Defect Count', fontsize=15)
plt.xlabel('Process Time', fontsize=12)
plt.ylabel('Defect Count', fontsize=12)
plt.tight_layout()
print(plt.show())