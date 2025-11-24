#파이 차트는 전체를 100%로 놓고, 각각의 부분이 전체에서 차지하는 비율을 보여주는 원 모양의 그래프다
#반도체 공정은 복잡하고 다양한 단계로 이루어져 있다. Pie Chart를 사용하면 복잡한 공정 정보를 한눈에
#알아보기 쉽게 표현할 수 있어서 효율적인 분석과 관리에 도움을 준다

#한눈에 보는 인기 분석
#의사 결정에 도움
#단순하고 명확한 표현

#메뉴의 총 판매량 파이 그래프(Pie Chart)
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

#파이 그래프의 크기를 가로 10, 세로 7로 설정한다
plt.figure(figsize=(10, 7))
plt.pie(
    menu_sales,
    labels=menu_sales.index,
    autopct='%.1f%%',
    startangle=140
)

#그래프의 제목 설정
plt.title('Pie Chart - Total Sales Proportion by Product')

#Matplotlib의 기본 설정은 파이 그래프를 그릴 때 화면이나 창의 크기 비율에 따라 원이 아닌
#타원의 형태로 나타날 수도 있다.
#이 때, plt.axis("equal") 명령어를 사용하면 가로축과 세로축의 비율을 동일하게 맞추어,
#파이 그래프가 항상 완벽한 원 모양으로 표시되도록 해준다
plt.axis('equal')

print(plt.show())