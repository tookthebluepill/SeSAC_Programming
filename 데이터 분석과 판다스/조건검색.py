import pandas as pd

#표 형태로 데이터 만들기
data = {
    '이름': ['철수', '영희', '민수', '수진'],
    '나이': [25, 30, 22, 28],
    '성별': ['남자', '여자', '남자', '여자'],
    '점수': [90, 85, 95, 88]
}

#데이터 프레임 만들기
df = pd.DataFrame(data)
print(df)


#성별이 여자인 사람만 고르기
female_df = df[df['성별'] == '여자']
print(female_df)
age_over_25 = df[df['나이'] > 25]
print(age_over_25)

#두 가지 조건을 모두 만족하는 검색
#성별이 여자인 사람이면서 점수가 85점 이상인 사람만 뽑기
female_high_score = df[(df['성별'] == '여자') & (df['점수'] >= 85)]
print(female_high_score)

#두 가지 조건 중 하나만 만족해도 뽑기
#나이가 30살 이상이거나 점수가 90점 넘는 사람 뽑기
age_or_score = df[(df['나이'] >= 30) | (df['점수'] >= 90)]
print(age_or_score)