import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. 데이터 로드 및 전처리
# ==========================================
# 데이터 불러오기
df = pd.read_csv("semiconductor.csv")

# 데이터 기본 정보 확인
print("=== 데이터 기본 정보 (전처리 전) ===")
print(df.info())

# 결측치(NaN)가 있는 행 제거 (분석의 정확도를 위해 중요)
df_clean = df.dropna()
print(f"\n[전처리 완료] 결측치 제거 후 데이터 개수: {len(df_clean)}개 (원본: {len(df)}개)")

# 날짜와 시간을 합쳐서 datetime 형식으로 변환 (시계열 분석 준비)
df_clean['datetime'] = pd.to_datetime(df_clean['date'] + ' ' + df_clean['time'])

# ==========================================
# 2. 전체 변수 상관관계 분석 (Heatmap)
# ==========================================
# 수치형 데이터만 선택
numeric_cols = ['process_temp', 'process_pressure', 'process_rf_power', 'gas_flow_rate', 
                'uniformity', 'reflectance', 'film_thickness_nm', 'defect_count']
corr_matrix = df_clean[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Process Parameters Correlation Matrix')
plt.savefig('01_correlation_heatmap.png')
plt.close()
print("1. 상관관계 히트맵 저장 완료 (01_correlation_heatmap.png)")

# ==========================================
# 3. 공장(Fab) 및 장비(Equipment)별 불량률 비교
# ==========================================
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Fab 별 불량 수 비교 (경고 해결: errorbar=None, hue 추가)
sns.barplot(data=df_clean, x='fab_location', y='defect_count', ax=ax[0], 
            errorbar=None, hue='fab_location', legend=False, palette='viridis')
ax[0].set_title('Average Defect Count by Fab Location')
ax[0].set_ylabel('Average Defect Count')

# 장비 별 불량 수 비교 (경고 해결: errorbar=None, hue 추가)
sns.barplot(data=df_clean, x='equipment', y='defect_count', ax=ax[1], 
            errorbar=None, hue='equipment', legend=False, palette='viridis')
ax[1].set_title('Average Defect Count by Equipment')
ax[1].set_ylabel('Average Defect Count')
# X축 라벨 회전 (장비 이름이 겹치지 않게)
ax[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('02_fab_equipment_defect.png')
plt.close()
print("2. 공장 및 장비별 불량률 그래프 저장 완료 (02_fab_equipment_defect.png)")

# ==========================================
# 4. 공정 타입별 결함 유형 분포
# ==========================================
plt.figure(figsize=(12, 6))
# 'none'이 아닌 실제 결함만 필터링하여 시각화
sns.countplot(data=df_clean[df_clean['defect_type'] != 'none'], x='process_type', hue='defect_type')
plt.title('Defect Type Distribution by Process Type')
plt.savefig('03_process_defect_type.png')
plt.close()
print("3. 공정별 결함 유형 그래프 저장 완료 (03_process_defect_type.png)")

# ==========================================
# 5. [심화] OXID_03 장비 집중 분석
# ==========================================
# 문제의 장비 데이터만 추출
oxid_03_df = df_clean[df_clean['equipment'] == 'OXID_03'].copy()

# 양품(Good)과 불량(Bad) 구분 (결함 개수가 0이면 Good, 아니면 Bad)
oxid_03_df['quality'] = oxid_03_df['defect_count'].apply(lambda x: 'Good' if x == 0 else 'Bad')

# 시각화: 온도와 가스 유량 분포 비교
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# 온도(Temp) 분포 비교
sns.histplot(data=oxid_03_df, x='process_temp', hue='quality', element="step", stat="density", common_norm=False, ax=ax[0], palette={'Good':'green', 'Bad':'red'})
ax[0].set_title('OXID_03: Temp Distribution (Good vs Bad)')

# 가스 유량(Gas Flow) 분포 비교
sns.histplot(data=oxid_03_df, x='gas_flow_rate', hue='quality', element="step", stat="density", common_norm=False, ax=ax[1], palette={'Good':'green', 'Bad':'red'})
ax[1].set_title('OXID_03: Gas Flow Distribution (Good vs Bad)')

plt.tight_layout()
plt.savefig('04_oxid_03_deep_dive.png')
plt.close()
print("4. OXID_03 장비 심화 분석 그래프 저장 완료 (04_oxid_03_deep_dive.png)")

print("\n=== 모든 분석이 완료되었습니다. 생성된 이미지를 확인해주세요. ===")