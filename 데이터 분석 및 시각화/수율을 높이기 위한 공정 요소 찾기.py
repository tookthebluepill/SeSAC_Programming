# 식각공정데이터의 시각화를 통해서 정확한 식각깊이(정확한 스펙이 안나와 있으니 중앙값을 타겟으로 설정)
# 결함개수(defect count)가 적은 반도체를 만들기 위해 관리해야 하는 압력, rf_powr 등을 찾아보고
# 수율을 높이기 위한(result 칼럼 값이 good) 공정 요소를 찾아보아라.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정 (필요시 시스템에 맞는 폰트로 변경 필요)
plt.rcParams['font.family'] = 'Malgun Gothic' # 윈도우의 경우
plt.rcParams['axes.unicode_minus'] = False    # 마이너스 기호 깨짐 방지

# 데이터 불러오기
df = pd.read_csv("04_etching_process_1.csv")

# 기본 정보 출력
print("데이터 정보:")
print(df.info())
print("\n상위 5개 행:")
print(df.head())

# 데이터 정제
# 결측치 보간 (선형 보간법 사용)
df.interpolate(method='linear', inplace=True)

# --- 분석 1: 식각 깊이 (중앙값 타겟 설정) ---
median_depth = df["etch_depth"].median()
std_depth = df["etch_depth"].std()
print(f"\n식각 깊이 중앙값: {median_depth}")
print(f"식각 깊이 표준편차: {std_depth}")

# 타겟 범위 설정 (예: 중앙값 +/- 3 표준편차를 벗어나면 이상치로 간주)
upper_bound = median_depth + 3 * std_depth
lower_bound = median_depth - 3 * std_depth

# 시각화 1: 식각 깊이 분포
plt.figure(figsize=(10, 6))
sns.histplot(df['etch_depth'], kde=True, color='blue')
plt.axvline(median_depth, color='red', linestyle='--', label=f'중앙값: {median_depth:.2f}')
plt.title('식각 깊이 분포')
plt.xlabel('식각 깊이')
plt.ylabel('빈도수')
plt.legend()
plt.savefig('etch_depth_dist.png')
plt.close()

# 식각 깊이는 정규분포에 가까운 형태를 띠며, 붉은색 점선인 중앙값(505.57) 부근에 데이터가 집중되어 있습니다.
#전체 데이터의 중앙값은 505.57
#양품(Good) 데이터의 중앙값은 505.14

#1. 목표 식각 깊이 (Etch Depth Target)
# 데이터 분석 결과, 전체 공정의 식각 깊이 중앙값은 약 505.57입니다. 이를 공정의 기준 타겟(Target)으로 설정하는 것을 권장합니다.

# Target Etch Depth: 505.57
# Good Wafer 평균: 506.10 (양품 웨이퍼들도 중앙값에 매우 근접하게 분포함)

# --- 분석 2: 압력 및 RF 파워와 결과(수율)의 관계 ---
# 시각화 2: 결과에 따른 압력 분포
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='pressure', hue='result', kde=True, palette={'Good':'green', 'Bad':'red'}, element="step")
plt.title('압력 분포: 양품(Good) vs 불량(Bad)')
plt.xlabel('압력')
plt.savefig('pressure_yield.png')
plt.close()

# 초록색(Good)은 22 부근에 집중되어 있는 반면, 붉은색(Bad)은 더 낮은 압력이나 높은 압력으로 퍼져 있는 경향을 보입니다.

# 시각화 3: 결과에 따른 RF 파워 분포
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='rf_power', hue='result', kde=True, palette={'Good':'green', 'Bad':'red'}, element="step")
plt.title('RF 파워 분포: 양품(Good) vs 불량(Bad)')
plt.xlabel('RF 파워')
plt.savefig('rf_power_yield.png')
plt.close()

# 초록색(Good)은 260 부근에서 높은 밀도를 보입니다

# 양품(Good) 웨이퍼에 대한 통계 계산
good_wafers = df[df['result'] == 'Good']
print("\n'양품(Good)' 웨이퍼 통계:")
print(good_wafers[['pressure', 'rf_power', 'etch_depth']].describe())


# --- 분석 3: 결함 개수와 공정 변수 간의 관계 ---
# 시각화 4: RF 파워 vs 결함 개수
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='rf_power', y='defect_count', hue='result', palette={'Good':'green', 'Bad':'red'})
plt.title('RF 파워 vs 결함 개수')
plt.xlabel('RF 파워')
plt.ylabel('결함 개수')
plt.savefig('rf_power_defect.png')
plt.close()

# RF Power가 최적 범위를 벗어날수록 붉은색(Bad) 점들이 나타나며 결함 개수(Y축)가 증가하는 경향을 확인할 수 있습니다.

# 시각화 5: 압력 vs 결함 개수
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='pressure', y='defect_count', hue='result', palette={'Good':'green', 'Bad':'red'})
plt.title('압력 vs 결함 개수')
plt.xlabel('압력')
plt.ylabel('결함 개수')
plt.savefig('pressure_defect.png')
plt.close()

# Recipe A에서 초록색(Good) 비율이 가장 높고, C에서는 붉은색(Bad) 비율이 현저히 높음을 시각적으로 확인할 수 있습니다.

# 2. 수율(Good Result) 및 결함 최소화를 위한 공정 조건결함(Defect) 분석:
# Good (양품): 평균 결함 개수 약 1.9개 (대부분 0~3개)Bad (불량): 평균 결함 개수 약 8.8개 (최소 4개 이상)
# 따라서, 아래의 조건을 유지하면 결함 개수를 3개 이하로 관리하여 양품률을 높일 수 있습니다.
# 최적 공정 파라미터 (Good 웨이퍼 기준):양품(Good) 웨이퍼들이 주로 분포하는 범위(25% ~ 75% 구간)를 최적 관리 범위로 제안합니다.
# 공정 요소최적 관리 범위 (권장)평균값Pressure (압력)21.0 ~ 22.921.98RF Power256.8 ~ 263.2259.87

# --- 분석 4: 레시피 분석 ---
# 시각화 6: 레시피별 결과 빈도 그래프
plt.figure(figsize=(10, 6))
sns.countplot(x='recipe', hue='result', data=df, palette={'Good':'green', 'Bad':'red'})
plt.title('레시피 vs 결과')
plt.xlabel('레시피')
plt.ylabel('빈도수')
plt.savefig('recipe_yield.png')
plt.close()

# 레시피별 수율 계산
recipe_stats = df.groupby('recipe')['result'].value_counts(normalize=True).unstack().fillna(0)
print("\n레시피별 수율:")
print(recipe_stats)

# 3. 레시피(Recipe)별 수율 비교
# 각 레시피 별 양품률을 분석한 결과, Recipe A가 가장 압도적인 품질을 보여줍니다.

# Recipe A: 양품률 90% (가장 우수)
# Recipe B: 양품률 62%
# Recipe C: 양품률 30% (가장 저조, 불량률 70%)

# 결론: 생산 효율을 높이기 위해서는 Recipe A를 주력으로 사용하고, 압력과 RF Power를 위에서 도출한 최적 범위 내에서 유지하는 것이 좋습니다.