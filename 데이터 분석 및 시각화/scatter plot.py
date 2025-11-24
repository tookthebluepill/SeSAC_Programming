#Scatter Plot(산점도)은 두 가지 항목 간의 관계를 쉽게 확인할 때 사용하는 그래프다.
#산점도의 모양으로 알 수 있는 사실은 다음과 같다
#1. 점들이 오른쪽 위로 올라가는 형태일 때(비례관계)
#2. 점들이 아무런 규칙 없이 여기저기 흩어져 있을 때(무관계)
#3. 점들이 오른쪽 아래로 내려가는 형태일 때(반비례 관계)

#산점도로 얻을 수 있는 정보
#두 가지 제품이 서로 연관이 있는지 쉽게 이해
#메뉴나 제품의 전략을 짤 떄, 같이 판매하면 좋은 조합을 쉽게 찾을 수 있다
#서로 관계가 없는 제품끼리는 별도의 판매 전략을 세울 수 있게 도와준다

#반도체 공정에서 산점도의 사용
#반도체 공정에서 산점도는 반도체가 만들어지는 과정에서 생길 수 있는 문제나 품질 변화를
#쉽고 빠르게 확인할 때 사용하는 그래프다.

#반도체는 아주 작은 전자 부품이어서 만들 때 온도, 압력, 습도 등 다양한 조건이 매우 중요하다
#예를 들어, 반도체 공정 중 온도와 제품의 품질 관계를 살펴볼 때
#반도체를 만들 때 온도(X축)와 완성된 반도체의 성능(Y축)을 점으로 찍어 살펴본다
#만약 점들이 일정한 규칙으로 나타난다면, 그 온도에서 좋은 성능을 내는 반도체를 만들 것이다
#하지만 점들이 이곳저곳에 흩어져 있다면, 온도와 성능 간에 별다른 관계가 없다는 것을 의미한다

#카페라떼와 뉴욕 치즈 케이트 Scatter Plot(산점도)
#카페라떼를 구매할 때 뉴욕치즈케이크도 함께 구매하는지 확인하는 용도
#인기 메뉴와 디저트 간 관계 확인이 가능하다
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#그래프를 보기 좋은 스타일로 설정
plt.style.use("ggplot")
df = pd.read_csv('03_cafe_1.csv')
print(df.head())

#그래프를 그릴 종이의 크기를 설정한다
plt.figure(figsize=(10, 6))

#카페라떼(cafe_latte) 판매량과 뉴욕 치즈케이크(ny_cheese_cake) 판매량 사이의 관계를
#점으로 찍어 확인한다(scatter plot)
sns.scatterplot(
    x='cafe_latte',
    y='ny_cheese_cake',
    data=df
)

#그래프의 제목을 영어로 쉽게 알아 볼 수 있도록 붙여준다
plt.title('Scatter Plot - Cafe Latte vs NY Cheese Cake')

plt.xlabel('Caffe Latte Sales')
plt.ylabel('NY Cheese Cake Sales')
plt.legend(['Sales Data'])
plt.tight_layout()
print(plt.show())
