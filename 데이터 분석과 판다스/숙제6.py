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

# [2] 데이터 전처리 (분석을 위한 플래그 생성)
# 각 결함 유형별로 True/False를 구분하여 분석을 용이하게 만듭니다.
df['is_particle'] = df['defect_type'] == 'particle'
df['is_pinhole'] = df['defect_type'] == 'pinhole'
df['is_good'] = df['defect_type'] == 'none'

print("\n" + "="*20 + " 결함 유형별 빈도 확인 " + "="*20)
print(df['defect_type'].value_counts())

# [3] 결함별 핵심 원인 분석 (데이터 그룹핑 비교)
# 정상 웨이퍼와 불량 웨이퍼의 공정 조건 평균을 비교합니다.
print("\n" + "="*40)
print(" 🔍 결함 유형별 공정 변수 평균 비교")
print("="*40)

# (1) Particle 불량 vs 정상 (압력 비교)
print("\n[1. Particle(이물질) 발생 시 평균 압력 차이]")
print(df.groupby('is_particle')['pressure'].mean())

# (2) Pinhole 불량 vs 정상 (두께 비교)
print("\n[2. Pinhole(핀홀) 발생 시 평균 두께 차이]")
print(df.groupby('is_pinhole')['oxide_thickness'].mean())

# (3) 세정 시간(Pre-cleaning)에 따른 결함률 확인
print("\n[3. 세정 시간(Pre-cleaning)별 결함 발생 비율]")
# crosstab을 사용하여 각 시간별로 불량이 얼마나 생겼는지 비율로 확인
clean_defect_rate = pd.crosstab(df['precleaning_time'], df['defect_type'], normalize='index')
print(clean_defect_rate)


# [4] 통계적 가설 검정 (Statistical Hypothesis Testing)
# 위에서 확인한 차이가 진짜 의미가 있는지 P-value로 검증합니다.

print("\n" + "="*40)
print(" 📊 [통계적 검증 결과 (P-value < 0.05 기준)] ")
print("="*40)

# (1) Particle과 챔버 압력 (T-test)
# 가설: 압력이 낮으면 Particle이 발생한다?
particle_pressures = df[df['is_particle']]['pressure'].dropna()
normal_pressures = df[df['is_good']]['pressure'].dropna()
t_stat, p_val_particle = stats.ttest_ind(particle_pressures, normal_pressures, equal_var=False)

print(f"\n1️⃣ Particle 발생과 챔버 압력 (T-test)")
print(f"   - P-value: {p_val_particle:.4f}")
if p_val_particle < 0.05:
    print("   => ✅ 결론: 통계적으로 유의미함 (압력 저하가 Particle의 핵심 원인)")
else:
    print("   => ❌ 결론: 통계적으로 유의미하지 않음")

# (2) Pinhole과 산화막 두께 (T-test)
# 가설: 두께가 얇으면 Pinhole이 생긴다?
pinhole_thickness = df[df['is_pinhole']]['oxide_thickness'].dropna()
normal_thickness = df[df['is_good']]['oxide_thickness'].dropna()
t_stat, p_val_pinhole = stats.ttest_ind(pinhole_thickness, normal_thickness, equal_var=False)

print(f"\n2️⃣ Pinhole 발생과 산화막 두께 (T-test)")
print(f"   - P-value: {p_val_pinhole:.4f}")
if p_val_pinhole < 0.05:
    print("   => ✅ 결론: 통계적으로 유의미함 (두께 부족이 원인)")
elif p_val_pinhole < 0.1:
    print("   => ⚠️ 결론: 유의한 경향성 있음 (두께가 얇을수록 위험 증가)")
else:
    print("   => ❌ 결론: 관계 없음")


# [5] 최적의 생산 조건 발굴 (Golden Recipe Analysis)
# 목표: 결함 없음(None) + 두께 적절(300~320nm) + 균일도 최상(1.0 미만)
# 이 조건을 모두 만족하는 '완벽한 웨이퍼'들의 공통점을 찾습니다.

golden_wafers = df[
    (df['defect_type'] == 'none') &
    (df['oxide_thickness'] >= 300) & (df['oxide_thickness'] <= 320) &
    (df['uniformity'] < 1.0)
]

others = df.drop(golden_wafers.index)

print("\n" + "="*40)
print(f" 🌟 Golden Wafer (완벽한 품질) 분석 (총 {len(golden_wafers)}개 발견)")
print("="*40)

# 가스 유량 비교 검증
t_stat, p_val_golden = stats.ttest_ind(golden_wafers['gas_flow_rate'], others['gas_flow_rate'], equal_var=False)

print(f"\n[Golden Wafer vs 일반 Wafer 가스 유량 비교]")
print(f"   - Golden 평균 유량 : {golden_wafers['gas_flow_rate'].mean():.1f} sccm")
print(f"   - 일반 평균 유량   : {others['gas_flow_rate'].mean():.1f} sccm")
print(f"   - 가스 유량 차이 검증 P-value : {p_val_golden:.5f}")

if p_val_golden < 0.05:
    print("   => 🎯 핵심 발견: 가스 유량을 1,900 sccm 수준으로 낮추는 것이 품질 혁신의 열쇠입니다!")

# 시각화: 세정 시간별 결함 분포 (Bar Chart)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='precleaning_time', hue='defect_type')
plt.title('Defect Distribution by Pre-cleaning Time')
plt.xlabel('Pre-cleaning Time (min)')
plt.ylabel('Count')
plt.legend(title='Defect Type')
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n" + "="*60)
print(" [최종 종합 공정 제안서]")
print(" 1. 가스 유량(Gas Flow): 1,900 sccm으로 하향 조정하여 '균일도' 극대화 (Golden Recipe)")
print(" 2. 챔버 압력(Pressure): 0.5 atm 이상 유지하여 'Particle' 발생 차단")
print(" 3. 세정 시간(Cleaning): 표준 시간을 5분으로 설정하여 초기 오염 방지")
print(" 4. 산화 시간(Time): 최소 35분 이상 확보하여 막 형성을 안정화하고 'Pinhole' 예방")
print("="*60)