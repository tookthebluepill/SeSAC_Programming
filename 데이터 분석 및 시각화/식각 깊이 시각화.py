import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")

df = pd.read_csv("04_etching_process_1.csv")
print(df)

#df['wafer_id'].str.extract('(\d+)') 설명
#-str.extract('(\d+)'): 글자(문자열)에서 숫자(\d)만 뽑아낸다
#-astype(int): 숫자를 정수(int)로 바꿔준다 (예: 001 -> 1로 변환)
df['wafer_num'] = df['wafer_id'].str.extract('(\d+)').astype(int)
print(df)

df.sort_values('wafer_num', inplace=True)
print(df)

#결측치 처리
#interpolate(): 빈칸이 있을 경우, 앞뒤 데이터를 이용하여 중간값으로 빈칸을 채워준다.
#method='linear': 선형으로 채우기(앞뒤 숫자를 연결한 직선에서 중간에 위치하는 값으로 채움)
#inplace=True: 변경된 내용을 바로 데이터에 적용한다
df.interpolate(method='linear', inplace=True)
print(df.info())


#이상치(특별히 튀는 값)를 찾기 위한 기준값을 계산
median = df["etch_depth"].median()
print(median)

std = df["etch_depth"].std()
print(std)

#이상치의 기준을 설정
#보통 "중앙값 +-3 * 표준편차"를 벗어나면 이상치로 본다
upper_bound = median + 3 * std
lower_bound = median - 3 * std

print(f"Upper Bound: {upper_bound}")
print(f"lower Bound: {lower_bound}")

#위 기준을 이용해서 이상치 데이터를 찾아낸다
outliers = df[(df["etch_depth"] > upper_bound) | (df["etch_depth"] < lower_bound)]
print(outliers)

#라인그래프로 시각화하기
plt.figure(figsize=(14, 5))
sns.lineplot(x='wafer_num', y='etch_depth', data=df, marker='o', color='green')
plt.scatter(outliers['wafer_num'], outliers['etch_depth'],
            color='red', s=100, edgecolor='black',
            label='Outliers (3σ)')

#정상 범위의 기준선을 빨간색 점선으로 표시
#plt.axhline(): 수평선을 그어주는 함수
plt.axhline(upper_bound, color='red', linestyle='--', label='Upper Bound (3σ)')
plt.axhline(lower_bound, color='red', linestyle='--', label='lower Bound (3σ)')

plt.title('Etching Depth')
plt.xlabel('Wafer Number')
plt.ylabel('Etching Depth')
plt.legend()
#레이아웃(배치)를 보기 좋게 자동으로 조정
plt.tight_layout()
print(plt.show())