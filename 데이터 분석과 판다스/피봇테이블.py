import pandas as pd
data = {
    '손님': ['철수', '영희', '민수', '철수', '영희', '민수'],
    '메뉴': ['피자', '피자', '피자', '햄버거', '햄버거', '햄버거'],
    '개수': [2, 1, 3, 2, 2, 1]
}

df = pd.DataFrame(data)
print(df)

#메뉴별로 총 개수 계산하기
pivot_menu = df.pivot_table(
    index = '메뉴',
    values = '개수',
    aggfunc= 'sum'
)
print(pivot_menu)

#손님별로 총 주문 수량 계산하기
pivot_customer = df.pivot_table(
    index = '손님',
    values = '개수',
    aggfunc= 'sum'
)
print(pivot_customer)

#메뉴별로 평균 계산하기
pivot_mean = df.pivot_table(
    index = '메뉴',
    values = '개수',
    aggfunc= 'mean'
)