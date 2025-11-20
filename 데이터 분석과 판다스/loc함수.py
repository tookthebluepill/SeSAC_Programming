#각 행에 이름 붙이기(A, B, C)
import pandas as pd

#표 형태로 데이터 만들기
data = {
    '이름': ['철수', '영희', '민수'],
    '나이': [25, 30, 22],
    '성별': ['남자', '여자', '남자'],
    '점수': [90, 85, 95]
}

#데이터 프레임 만들기
df = pd.DataFrame(data, index=['A', 'B', 'C'])
print(df)

#행 선택
#A행의 모든 데이터 선택하기
row_a = df.loc['A', :]
print(row_a)

#열 선택
#하나의 열 전체를 선택하는 예시
scores = df.loc[:, '점수']
print(scores)

#특정 행과 특정 열에서 하나 값만 가져오기
age_b = df.loc['B', '나이']
print(age_b)

#특정 행과 여러 열을 동시에 선택하기
selected_df = df.loc[['A', 'C'], ['이름', '점수']]
print(selected_df)

#행과 열을 범위로 선택하기
subset = df.loc['A':'C', '나이':'점수']
print(subset)