#Line Chart(선 그래프)는 데이터를 선으로 이어서 시간에 따른 변화를 쉽게 확인할 수 있게 하는 그래프
#시간에 따라 변화하는 모습을 사진처럼 찍어 연결한 것

#반도체 공정에서도 Line Chart를 자주 사용한다.
#반도체는 작은 변화에도 품질이 크게 달라지기 때문에 항상 데이터의 변화를 꼼꼼하게 체크해야 한다.
#예를 들어, 반도체를 만들 때 중요한 온도나 압력 같은 데이터를 Line Chart를 그려서 확인한다.
#온도 변화
#압력 변화
#불량률 추이

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#그래프를 보기 좋은 스타일로 설정
plt.style.use("ggplot")
df = pd.read_csv('03_cafe_1.csv')
print(df.head())

#그래프의 크기 설정(가로 15, 세로 6)
plt.figure(figsize=(15, 6))

#아메리카노 판매량을 선 그래프로 나타낸다
sns.lineplot(
    x='date',
    y='americano',
    data=df,
    marker='o'
)

#그래프의 제목 설정
plt.title('Daily Americano Sales')

#그래프의 가로축(x축)의 제목을 날짜(Date)로 설정
plt.xlabel('Date')

#그래프의 세로축(y축)의 제목을 아메리카노 판매량(Americano Sales)으로 설정
plt.ylabel('Americano Sales')

#날짜가 많이 겹치므로 글자를 45도 돌려 보기 좋게 만든다
plt.xticks(rotation=45)

#그래프 내용이 겹치지 않도록 자동으로 간격을 조정한다
plt.tight_layout()

plt.show()