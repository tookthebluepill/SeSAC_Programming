import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv('04_etching_process_1.csv')
print(df.head())

recipe_table = pd.crosstab(
    df['recipe'],
    df['result']
)
print(recipe_table)
chi2, p, dof, expected = chi2_contingency(recipe_table)
print("실제 데이터(실제값)")
print(recipe_table)

print("\n카이제곱 통계량:", chi2)
print("\np-value(피밸류):", p)
print("\n자유도:", dof)

#레시피가 defect_type 3가지에 영향을 주는지 검정
# 1. 고유한 불량 유형과 그 개수 확인 (NaN 포함)
defect_counts = df['defect_type'].value_counts(dropna=False)
print("불량 유형별 개수 (NaN 포함):")
print(defect_counts)

# 2. defect_type이 NaN인 행은 제외 (NaN은 불량 없음(defect_count=0)을 의미함)
df_defects = df.dropna(subset=['defect_type'])

# 3. 'recipe'와 'defect_type'을 이용한 교차표(분할표) 생성
recipe_defect_table = pd.crosstab(
    df_defects['recipe'],
    df_defects['defect_type']
)
print("\n교차표 (레시피 대 불량 유형):")
print(recipe_defect_table)

# 4. 카이제곱 독립성 검정 수행
if recipe_defect_table.empty:
    print("\n오류: 필터링 후 교차표가 비어있습니다.")
else:
    # 카이제곱 통계량, p-value, 자유도, 기대 빈도 계산
    chi2, p, dof, expected = chi2_contingency(recipe_defect_table)
    
    print("\n카이제곱 통계량:", chi2)
    print("p-value:", p)
    print("자유도:", dof)
    print("\n기대 빈도 (Expected Frequencies):")
    # 기대 빈도를 DataFrame 형태로 출력하여 가독성 높임
    print(pd.DataFrame(expected, index=recipe_defect_table.index, columns=recipe_defect_table.columns))