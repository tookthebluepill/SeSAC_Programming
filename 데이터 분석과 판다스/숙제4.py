#4.02_oxide.csv 에서 균일도에 영향을 미치는 요소를 분석하고
#균일도가 고르게 유지하기 위해서 공정을 어떻게 관리해야 하는지 제안하고 이유를 설명해 주세요

# [1] 라이브러리 임포트 및 데이터 로드
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats  # 통계 검정용 라이브러리

file_path = "02_oxide.csv"
df = pd.read_csv(file_path)

# [2] 데이터 기본 확인
print(df.info())
print(df.head())

# [3] 수치형 변수 상관관계 분석
# 분석할 공정 변수 리스트 정의
# 인과 관계(원인과 결과)를 분석할 수 있는 '수치형(숫자)' 데이터를 공정 변수로 선택
# 1.숫자가 아니라서 계산 불가 (범주형/문자열 데이터)
# 2.분석 목적과 맞지 않음 (메타 데이터)
# 다음 두 변수들을 제거
process_vars = ['precleaning_time', 'oxidation_temperature', 'oxidation_time',
                'pressure', 'gas_flow_rate', 'oxide_thickness', 'uniformity']

# 상관계수 계산
corr_matrix = df[process_vars].corr()

print("\n" + "="*20 + " 균일도(Uniformity)와 상관관계 순위 " + "="*20)
print(corr_matrix['uniformity'].sort_values(ascending=False))

# --- 시각화 1: 상관관계 히트맵 ---
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Process Parameters Correlation Matrix')
plt.show()
# --- 시각화 2: 가스 유량 vs 균일도 산점도 ---
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='gas_flow_rate', y='uniformity')
plt.title('Gas Flow Rate vs. Uniformity (Positive Correlation)')
plt.xlabel('Gas Flow Rate (sccm)')
plt.ylabel('Uniformity (%)')
plt.grid(True, alpha=0.3)
plt.show()

# [4] 범주형 변수 영향 분석 (Boxplot)
# 장비나 챔버에 따라 균일도 차이가 있는지 눈으로 확인합니다.

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# --- 시각화 3: 장비별 균일도 ---
sns.boxplot(data=df, x='equipment_id', y='uniformity', ax=axes[0])
axes[0].set_title('Equipment ID vs Uniformity')
axes[0].set_ylabel('Uniformity (%)')
axes[0].grid(True, alpha=0.3)

# --- 시각화 4: 챔버별 균일도 ---
sns.boxplot(data=df, x='chamber_id', y='uniformity', ax=axes[1])
axes[1].set_title('Chamber ID vs Uniformity')
axes[1].set_ylabel('Uniformity (%)')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# [5] 통계적 가설 검정 (Statistical Hypothesis Testing)
# 눈으로 본 결과가 수학적으로도 의미가 있는지 검증합니다. (P-value < 0.05 기준)

print("\n" + "="*30 + " 📊 통계적 검증 결과 " + "="*30)

# 결측치 제거 (검정을 위해 필수)
df_clean = df.dropna(subset=['uniformity', 'gas_flow_rate'])

# (1) 가스 유량과 균일도의 상관성 검증 (Pearson)
r, p_val_r = stats.pearsonr(df_clean['gas_flow_rate'], df_clean['uniformity'])

print(f"\n[1] 가스 유량 vs 균일도 (Pearson 검정)")
print(f"  - 상관계수 (r): {r:.4f}")
print(f"  - P-value    : {p_val_r:.4e}")
if p_val_r < 0.05:
    print("  => ✅ 결론: 통계적으로 매우 유의미함! (가스 유량이 핵심 영향 인자)")
else:
    print("  => ❌ 결론: 통계적으로 의미 없음")

# (2) 장비별 성능 차이 검증 (ANOVA)
# 장비 그룹별 데이터를 모음
groups_eq = [group['uniformity'].values for name, group in df_clean.groupby('equipment_id')]
f_stat, p_val_anova = stats.f_oneway(*groups_eq)

print(f"\n[2] 장비별 균일도 차이 (ANOVA 검정)")
print(f"  - P-value : {p_val_anova:.4f}")
if p_val_anova < 0.05:
    print("  => ⚠️ 결론: 장비 간 성능 차이가 있음 (점검 필요)")
else:
    print("  => ✅ 결론: 장비 간 성능 차이는 통계적으로 없음 (설비 문제 아님)")

# (3) 웨이퍼 타입별 차이 검증 (T-Test)
# n-type과 p-type 그룹 나누기
n_type = df_clean[df_clean['wafer_doping_type'] == 'n-type']['uniformity']
p_type = df_clean[df_clean['wafer_doping_type'] == 'p-type']['uniformity']
t_stat, p_val_ttest = stats.ttest_ind(n_type, p_type)

print(f"\n[3] 웨이퍼 타입(n/p)별 차이 (T-Test 검정)")
print(f"  - P-value : {p_val_ttest:.4f}")
if p_val_ttest < 0.05:
    print("  => ⚠️ 결론: 웨이퍼 타입에 따라 균일도가 다름")
else:
    print("  => ✅ 결론: 웨이퍼 타입은 균일도에 영향 없음")

print("\n" + "="*60)
print("="*60)
