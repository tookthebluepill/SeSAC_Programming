#최적의 레시피란 반도체 제조 공정에서 목표하는 특성(두께, 균일성)을 가장 효율적으로 달성할 수 있는 공정 변수들의 조합이다
#이상적인 레시피는 제품 품질을 극대화하면서 동시에 생산 비용과 시간을 최소화한다.
#반도체 산업에서 최적 레시피의 발견은 수율 향상, 품질 안정화, 비용 절감으로 이어져 기업의 경쟁력을 크게 향상시킨다

#최적의 레시피를 찾는 과정
#1단계: 목표 품질 기준 설정
#예를 들어, 박막의 목표 두께를 3100nm로 설정하고 +-100nm의 허용 범위를 설정
#2단계: 다양한 레시피로 실험 진행
#여러 가지 조건(온도, 시간, 가스양, 전력 등)을 바꿔가며 공정(증착 공정)을 수행한다
#3단계: 실험 결과 분석
#만들어진 박막의 품질을 측정한다. 즉, 두께나 균일성 등의 결과 데이터를 분석한다
#4단계: 최적의 레시피 선정
#분석 결과 목표 기준에 가장 근접하고, 제조 효율이나 균일성이 좋은 레시피를 최종 선정한다

#카페라떼와 카푸치노 히스토그램(Histogram)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#그래프를 보기 좋은 스타일로 설정
plt.style.use("ggplot")
df = pd.read_csv('03_wafer_receipe_2.csv')
print(df.head())

target_thickness = 3100
tolerance = 100 #오차

#1. 데이터 프레임 조건 검색
#df에서 최소 두께(Min_Thickness)가 3000nm(3100-100) 이상이고,
#최대 두께(Max_Thickness) 3200nm(3100+100) 이하인 레시피만 선택하는 조건을 설정한다

filtered_recipes = df[
    (df['Min_Thickness'] >= target_thickness - tolerance) &
    (df['Max_Thickness'] <= target_thickness + tolerance)
].copy()

#2. copy() 함수
#위의 조건으로 데이터를 선택하면 원본 데이터(df)에 영향을 줄 수도 있어서
#데이터가 안전하게 독립적으로 관리될 수 있도록 복사본(copy)을 만듭니다.
print(filtered_recipes)

max_thickness_diff = abs(filtered_recipes['Mean_Thickness'] - 3100).max()
print(max_thickness_diff)
filtered_recipes['Score_Thickness'] = 1 -(abs(filtered_recipes['Mean_Thickness'] - 3100) / max_thickness_diff)
print(filtered_recipes.head())

#균일성(Unif)의 최대값과 최소값의 차이
max_unif_diff = filtered_recipes['Unif'].max() - filtered_recipes['Unif'].min()
print(max_unif_diff)
filtered_recipes['Score_Unif'] = 1 -((filtered_recipes['Unif'] - filtered_recipes['Unif'].min()) / max_unif_diff)
print(filtered_recipes.head())

#박막 두께의 표준편차의 최대값과 최소값의 차이
max_std_diff = filtered_recipes['Std_Thickness'].max() - filtered_recipes['Std_Thickness'].min()
print(max_std_diff)
filtered_recipes['Score_Std'] = 1 - ((filtered_recipes['Std_Thickness'] - filtered_recipes['Std_Thickness'].min()) / max_std_diff)
print(filtered_recipes.head())

#증착속도(Deposition Rate)의 최대값과 최소값의 차이
max_deposition_diff = filtered_recipes['Deposition Rate'].max() - filtered_recipes['Deposition Rate'].min()
print(max_deposition_diff)
filtered_recipes['Score_Deposition'] = (filtered_recipes['Deposition Rate'] - filtered_recipes['Deposition Rate'].min()) / max_deposition_diff
print(filtered_recipes.head())

#평가지표로 중요도(가중치)를 설정한다
weight_thickness = 0.4 #두께가 목표값과 가까운 것이 가장 중요 (40%)
weight_unif = 0.2 #균일성 중요도 (20%)
weight_std = 0.2 #두께 표준편차의 중요도 (20%)
weight_deposition = 0.2 #증착속도 중요도 (20%)

#최종 점수를 계산하여 'Final_Score' 칼럼에 저장한다
#각 평가 지표의 점수에 설정도니 가중치를 곱해 최종 점수를 합산한다
filtered_recipes['Final_Score'] = (
    filtered_recipes['Score_Thickness'] * weight_thickness +
    filtered_recipes['Score_Unif'] * weight_unif +
    filtered_recipes['Score_Std'] * weight_std +
    filtered_recipes['Score_Deposition'] * weight_deposition
)
print(filtered_recipes.head())

#최종 점수로 정렬하여 최적의 레시피 찾기
#최종 점수가 가장 높은 레시피를 선택하여 최적의 레시피로 결정한다
#sort_values 함수는 데이터프레임을 지정된 칼럼 기준으로 정렬한다
# - by: 정렬할 칼럼명을 지정한다
# - ascending: 오름차순(True, 작은 값부터 큰 값으로 정렬), 내림차순(False, 큰 값부터 작은 값으로 정렬)을 설정한다
# iloc[0]: 정렬된 데이터에서 가장 첫 번째 행(최고점)을 선택한다

filtered_recipes = filtered_recipes.sort_values(by='Final_Score', ascending=False)
print(filtered_recipes.head())

optimal_recipe = filtered_recipes.iloc[0]
print(optimal_recipe)

print("[최적의 레시피 정보]")
print(optimal_recipe[['Recipe_Name', 'Mean_Thickness', 'Min_Thickness', 'Max_Thickness',
                      'Unif', 'Std_Thickness', 'Deposition Rate', 'Final_Score']])