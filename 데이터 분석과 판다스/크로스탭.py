#크로스탭이랑 두 가지 항목 사이의 관계를 쉽게 정리해서 보여주는 표를 만드는 기능이다.

import pandas as pd
data = {
    '성별': ['남자', '여자', '남자', '여자', '남자', '여자', '남자'],
    '메뉴': ['피자', '피자', '햄버거', '햄버거', '피자', '햄버거', '햄버거']
}

df = pd.DataFrame(data)
print(df)

table = pd.crosstab(df['성별'], df['메뉴'])
print(table)

table2 = pd.crosstab(df['메뉴'], df['성별'])
print(table2)

#합계 표시하기
table3 = pd.crosstab(df['성별'], df['메뉴'], margins=True)
print(table3)

#성별별 메뉴 선호도 퍼센트로 보기
table_percent = pd.crosstab(df['성별'], df['메뉴'], normalize=True) * 100
table_percent = table_percent.round(2)
print(table_percent)

#합계와 퍼센트를 모두 함께 표시하기
table_percent_all = pd.crosstab(df['성별'], df['메뉴'], margins=True, normalize='all') * 100
table_percent_all = table_percent_all.round(2)
print(table_percent_all)