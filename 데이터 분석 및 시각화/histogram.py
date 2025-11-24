#히스토그램이란 "데이터가 특정 범위에서 얼마나 자주 나타나는지"를 막대 모양으로 보여주는 그래프다
#히스토그램은 주로 다음과 같이 구성되어 있다
#가로축(X축):데이터를 나눈 구간
#세로축(Y축):그 구간에 속한 데이터가 몇 개인지 나타낸다

#히스토그램은 데이터의 분포를 아주 쉽게 눈으로 볼 수 있게 해주는 그래프다
#히스토그램과 일반 막대그래프는 비슷하게 생겼지만 용도에 차이가 있다

#막대그래프(Bar Chart)는 항목별로 값을 나타낼 때 사용한다
#히스토그램(Histogram)은 데이터를 구간으로 나누어서 그 안에 몇 개의 데이터가 있는지 나타낼 때 사용
#즉, 막대그래프는 항목 간 비교에 좋고, 히스토그램은 "데이터의 분포(흐름)"를 파악할 때 적합하다

#카페라떼와 카푸치노 히스토그램(Histogram)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#그래프를 보기 좋은 스타일로 설정
plt.style.use("ggplot")
df = pd.read_csv('03_cafe_1.csv')
print(df.head())

#데이터에 있는 결측치(NaN, 빈 값)를 0으로 채운다
#fillna()는 데이터에 빈 값이 있으면 원하는 값으로 채워주는 함수다
#매개변수 inplace=True를 사용하면 현재의 데이터(df)에 직접 반영된다
df.fillna(0, inplace=True)


#히스토그램 그래프를 그리기 전에 그림의 크기를 설정한다
plt.figure(figsize=(10, 6))

#bins=20 : 데이터를 총 20개의 구간으로 나누어 히스토그램을 그린다
#kde=True : 히스토그램 위에 밀도곡선(KDE)을 함께 그린다
#alpha=0.5 : 그래프 색상을 약간 투명하게 만들어 다른 그래프와 겹쳐져도 잘 보이게 한다
#label='메뉴명' : 그래프에서 해당 데이터의 이름(범례로 나타날 이름)을 지정한다
#카푸치노(Cappuccino) 메뉴의 판매 데이터를 이용해 히스토그램을 그린다
sns.histplot(df['cappuccino'], bins=20, kde=True, alpha=0.5, label='Cappuccino')

#카페라떼(Cafe Latte) 메뉴의 판매 데이터를 이용해 히스토그램을 그린다
sns.histplot(df['cafe_latte'], bins=20, kde=True, alpha=0.5, label='cafe_latte')

#그래프의 제목을 설정
plt.title('Sales Frequency Comparison: Cappuccino vs Cafe Latte')

plt.xlabel('Sales per Day')
plt.ylabel('Frequency (Days)')

#그래프에서 데이터의 범례를 추가
plt.legend()

#그래프에 격자 무늬를 추가하여 그래프를 보기 쉽게 만든다
plt.grid(True)

print(plt.show())


#그래프에서 곡선은 무엇인가?
#밀도곡선(KDE)라고 하는데 쉽게 말해 "이 음료는 대체로 어느 판매량 주변에서 많이 팔리는가?"를
#부드럽게 이어주는 선이다.