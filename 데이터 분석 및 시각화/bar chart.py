#Bar Chart(막대 그래프)는 데이터를 길이가 서로 다른 막대 모양으로 나타내서 데이터끼리 쉽게 비교할 수 있도록 하는 그래프다.
#여러 가지 데이터를 막대의 길이로 나타내어 한눈에 차이를 볼 수 있게 해주는 도구다

#반도체 공정에서도 막대그래프를 자주 사용한다.
#반도체를 만드는 과정에서 다양한 조건들이 존재한다
#이 조건들이 얼마나 일정하게 유지되는지 막대그래프를 통해 쉽게 알 수 있다.

#빠른 문제 발견
#쉬운 비교 분석
#효율적인 관리

#메뉴별 판매량 막대그래프(Bar Chart)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#그래프를 보기 좋은 스타일로 설정
plt.style.use("ggplot")
df = pd.read_csv('03_cafe_1.csv')
print(df.head())

#메뉴 중 아메리카노부터 티라미수까지 메뉴별 판매 수량 데이터만 가져온다
#loc 함수는 DataFrame에서 행(row)과 열(column)을 레이블(label) 기반으로 선택할 때 사용하는 함수다
#정수 인덱스가 아니라 실제 행과 열의 이름(label)을 이용한다.

#기본형태:
#df.loc[행 선택 범위, 열 선택 범위]

menu_sales = df.loc[: , "americano":"tiramisu"]
print(menu_sales.head())

#메뉴별로 모든 날짜의 판매 수량을 더해서 총 판매량을 계산
print(menu_sales.sum())

#메뉴별로 모든 날짜의 판매 수량을 더해서 총 판매량을 계산
menu_sales = menu_sales.sum()
print(menu_sales)

#메뉴명을 조회
print(menu_sales.index)

#메뉴별 판매량을 조회
print(menu_sales.values)

#그래프의 크기(가로 10, 세로 6)를 설정
plt.figure(figsize=(10, 6))

#메뉴별 총 판매량을 막대그래프로 그린다
sns.barplot(
    x=menu_sales.values,
    y=menu_sales.index
)

#그래프 제목을 영어로 설정(한글 깨짐, 메뉴별 총 판매량)
plt.title('Total Sales by Menu')

#X축(가로축)의 제목을 설정(총 판매량)
plt.xlabel('Total Sales')

#Y축(세로축)의 제목을 설정(메뉴 이름)
plt.ylabel('Menu')

#그래프가 보기 좋도록 자동으로 간격 조정
plt.tight_layout()

print(plt.show())