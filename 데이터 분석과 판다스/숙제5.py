# [1] 라이브러리 임포트 및 데이터 로드
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats  # 통계 검정용 라이브러리

# 코랩에서는 파일을 먼저 업로드해야 합니다.
file_path = "02_oxide.csv"

try:
    df = pd.read_csv(file_path)
    print("✅ 데이터 로드 성공!")
except FileNotFoundError:
    print("❌ 파일을 찾을 수 없습니다. '02_oxide.csv' 파일을 업로드했는지 확인해주세요.")

# [2] 데이터 전처리 및 기본 확인
# Crack 분석을 위해 불량 여부를 0과 1로 변환합니다. (Crack=1, 정상=0)
# 'defect_type'이 'crack'인 경우만 1로 설정

#장비 갯수 확인 (칼럼의 고윳값 확인)
unique_equipments = df['equipment_id'].unique()
num_equipments = df['equipment_id'].nunique()

#챔버 갯수 확인
unique_chambers = df['chamber_id'].unique()
num_chambers = df['chamber_id'].nunique()

print(f"총 장비 개수: {num_equipments}")
print(f"장비 ID 목록: {unique_equipments}")

print(f"총 챔버 종류 개수: {num_chambers}")
print(f"챔버 ID 목록: {unique_chambers}")

df['is_crack'] = df['defect_type'].apply(lambda x: 1 if x == 'crack' else 0)

print("\n" + "="*20 + " 데이터 정보 (Info) " + "="*20)
print(df.info())
print("\n" + "="*20 + " 결함 유형별 카운트 " + "="*20)
print(df['defect_type'].value_counts())

# [3] 수치형 변수 분석: Crack 발생 그룹 vs 정상 그룹 비교
# Crack 여부에 따라 공정 변수들의 평균이 어떻게 다른지 확인합니다.
process_vars = ['oxidation_temperature', 'oxidation_time', 'gas_flow_rate', 'pressure', 'oxide_thickness']

print("\n" + "="*20 + " Crack 여부에 따른 공정 변수 평균값 " + "="*20)
# 0: 정상(No Crack), 1: 불량(Crack)
print(df.groupby('is_crack')[process_vars].mean())

# --- 시각화 1: 주요 변수 Boxplot (분포 비교) ---
# 평균만으로는 알 수 없는 데이터의 산포(퍼짐 정도)와 이상치(Outlier)를 확인합니다.
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# (1) 산화 온도 분포
sns.boxplot(data=df, x='defect_type', y='oxidation_temperature', ax=axes[0], order=['none', 'crack'])
axes[0].set_title('Oxidation Temp vs Defect Type')
axes[0].set_ylabel('Temperature (C)')
axes[0].grid(True, alpha=0.3)

# (2) 산화 시간 분포
sns.boxplot(data=df, x='defect_type', y='oxidation_time', ax=axes[1], order=['none', 'crack'])
axes[1].set_title('Oxidation Time vs Defect Type')
axes[1].set_ylabel('Time (min)')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# [4] 범주형 변수 분석: 챔버별 불량률 확인
# 챔버(Chamber)별로 Crack 발생 비율이 다른지 시각화합니다.
crack_rate_chamber = df.groupby('chamber_id')['is_crack'].mean()

print("\n" + "="*20 + " 챔버별 Crack 발생률 " + "="*20)
print(crack_rate_chamber)

# --- 시각화 2: 챔버별 Crack 발생률 막대그래프 ---
plt.figure(figsize=(8, 5))
sns.barplot(x=crack_rate_chamber.index, y=crack_rate_chamber.values, color='salmon')
plt.title('Crack Rate by Chamber ID')
plt.ylabel('Crack Rate (Probability)')
plt.ylim(0, 0.2) # 비율을 잘 보기 위해 y축 고정 (0~20%)
plt.grid(axis='y', alpha=0.3)
plt.show()


# [5] 통계적 가설 검정 (Statistical Hypothesis Testing)
# 눈으로 본 차이가 통계적으로 유의미한지(우연이 아닌지) 검증합니다. (P-value < 0.05 기준)

print("\n" + "="*30 + " 📊 통계적 검증 결과 " + "="*30)

# (1) 챔버별 불량률 차이 검증 (카이제곱 검정, Chi-square Test)
# 범주형 변수(챔버)와 범주형 변수(불량여부) 간의 관계를 볼 때 사용합니다.
contingency_table = pd.crosstab(df['chamber_id'], df['is_crack'])
chi2, p_val_chi2, dof, expected = stats.chi2_contingency(contingency_table)

print(f"\n[1] 챔버(Chamber)별 Crack 발생 차이 (Chi-square 검정)")
print(f"  - P-value : {p_val_chi2:.4f}")
if p_val_chi2 < 0.05:
    print("  => ✅ 결론: 통계적으로 유의미함! (특정 챔버에 문제가 있음)")
else:
    print("  => ❌ 결론: 챔버 간 차이는 통계적으로 없음")

# (2) 산화 온도 차이 검증 (T-Test)
# Crack 그룹과 정상 그룹 간의 평균 온도 차이가 있는지 확인합니다.
crack_temps = df[df['is_crack'] == 1]['oxidation_temperature'].dropna()
normal_temps = df[df['is_crack'] == 0]['oxidation_temperature'].dropna()

t_stat, p_val_ttest = stats.ttest_ind(crack_temps, normal_temps, equal_var=False)

print(f"\n[2] 산화 온도(Temp) 평균 차이 (Welch's T-Test)")
print(f"  - P-value : {p_val_ttest:.4f}")
if p_val_ttest < 0.05:
    print("  => ⚠️ 결론: Crack 그룹과 정상 그룹의 평균 온도가 다름")
else:
    print("  => ℹ️ 참고: 평균 온도의 차이는 통계적으로 유의하지 않음.")
    print("       (하지만 Boxplot에서 보듯 고온 이상치(Outlier)가 영향을 줄 수 있음)")

print("\n" + "="*60)
print(" [최종 결론 가이드]")
print(" 1. P-value가 0.05 미만인 '챔버(Chamber)' 이슈를 최우선으로 해결하세요.")
print(" 2. 온도는 평균 차이보다는 '극단적인 고온'을 막는 상한선 관리가 중요합니다.")
print("="*60)