import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 0. 환경 설정 및 데이터 불러오기
# 한글 폰트 설정 (Windows 환경일 경우 'Malgun Gothic', Mac은 'AppleGothic' 등으로 변경)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 데이터 읽어오기
df = pd.read_csv("04_etching_process_1.csv")

# 데이터 정보 확인 (행/열 개수, 데이터 타입 등)
print("=== 데이터 기본 정보 ===")
print(df.info())

# 결측치(비어있는 값) 채우기: 선형 보간법 사용 (앞뒤 숫자의 중간값으로 채움)
df.interpolate(method='linear', inplace=True)


# [분석 1] 정확한 식각 깊이 목표 설정 (중앙값 활용)
print("\n=== [분석 1] 식각 깊이 목표 설정 ===")
# 전체 데이터의 중앙값(Median) 계산
target_depth = df["etch_depth"].median()
print(f"목표 식각 깊이(중앙값): {target_depth:.2f}")

# 식각 깊이 분포 시각화
plt.figure(figsize=(10, 6))
sns.histplot(df['etch_depth'], kde=True, color='blue')
plt.axvline(target_depth, color='red', linestyle='--', label=f'목표값(중앙값): {target_depth:.2f}')
plt.title('식각 깊이 분포 및 목표값')
plt.xlabel('식각 깊이')
plt.ylabel('빈도수')
plt.legend()
plt.show() # 그래프 출력


# [분석 2] 결함 개수(Defect)가 적은 반도체를 만들기 위한 관리 요소 찾기
print("\n=== [분석 2] 결함 최소화 관리 요소 찾기 ===")

# 1. 상관관계 분석: 어떤 변수가 결함 개수와 관련이 깊은가?
# 분석할 숫자형 변수 선택
numeric_cols = ['pressure', 'rf_power', 'process_time', 'etch_depth', 'uniformity', 'defect_count']
corr_matrix = df[numeric_cols].corr()

# 결함 개수(defect_count)와 다른 변수들 간의 상관계수 출력 (높을수록 영향 큼)
print("결함 개수와의 상관계수 (절댓값이 1에 가까울수록 영향력 큼):")
print(corr_matrix['defect_count'].sort_values(ascending=False))
# 결과 해석: RF Power와 Pressure가 결함 개수와 가장 큰 양의 상관관계를 가짐

# 2. 핵심 변수(RF Power)와 결함 개수의 관계 시각화 (산점도)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='rf_power', y='defect_count', hue='result', palette={'Good':'green', 'Bad':'red'})
plt.title('RF 파워에 따른 결함 개수 분포')
plt.xlabel('RF 파워')
plt.ylabel('결함 개수')
# 해석: RF 파워가 높을수록 빨간점(Bad)이 많고 결함 개수가 증가함
plt.show()

# 3. 레시피별 결함 개수 비교 (박스플롯)
plt.figure(figsize=(10, 6))
sns.boxplot(x='recipe', y='defect_count', data=df)
plt.title('레시피별 결함 개수 차이')
plt.xlabel('레시피')
plt.ylabel('결함 개수')
# 해석: Recipe A의 결함 개수가 가장 적음
plt.show()


# [분석 3] 수율(Yield, Good Result)을 높이기 위한 공정 요소 찾기
print("\n=== [분석 3] 수율 향상을 위한 공정 요소 ===")

# 1. 양품(Good)과 불량(Bad)의 공정 조건 비교 (압력)
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='pressure', hue='result', kde=True, palette={'Good':'green', 'Bad':'red'}, element="step")
plt.title('양품(Good) vs 불량(Bad)의 압력 분포')
plt.xlabel('압력')
plt.show()

# 2. 양품(Good) 데이터의 통계치 확인 (최적 공정 범위 산출)
good_wafers = df[df['result'] == 'Good']
print("양품(Good) 웨이퍼의 주요 공정 변수 평균값:")
print(good_wafers[['pressure', 'rf_power']].mean())

# 3. 레시피별 수율(Good 비율) 확인
print("\n레시피별 수율(Good/Bad 비율):")
recipe_yield = df.groupby('recipe')['result'].value_counts(normalize=True).unstack().fillna(0)
print(recipe_yield)

# 4. 레시피별 수율 시각화
plt.figure(figsize=(10, 6))
sns.countplot(x='recipe', hue='result', data=df, palette={'Good':'green', 'Bad':'red'})
plt.title('레시피별 양품/불량 빈도')
plt.show()