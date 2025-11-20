# import pandas as pd

# #표 형태로 데이터 만들기
# data = {
#     '이름': ['철수', '영희', '민수'],
#     '나이': [25, 30, 22],
#     '성별': ['남자', '여자', '남자'],
#     '점수': [90, 85, 95]
# }

# #데이터 프레임 만들기
# df = pd.DataFrame(data)
# print(df)

# #하나의 열 선택
# #이름 선택
# name_column = df['이름']
# print(name_column)

# #두 개 이상의 열 선택하기
# #'이름'과 '점수' 두 개의 열 선택하기
# name_score_columns = df[['이름', '점수']]
# print(name_score_columns)

# #열 선택 후 특정 값만 보기
# #점수 열 선택 후 첫 번째 사람의 점수 보기
# first_score = df['점수'][0]
# print(first_score)

# #'이름', '나이' 열을 선택하고 두 번째 사람 정보만 보기
# second_person = df[['이름', '나이']].iloc[1]
# print(second_person)





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