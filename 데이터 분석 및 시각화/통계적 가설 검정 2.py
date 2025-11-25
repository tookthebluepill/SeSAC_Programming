#범주형 데이터 : 데이터가 몇 가지 정해진 카테고리로 나누어지는 데이터
#예를 들면: 성별, 날씨, 색상, 반도체 웨이퍼 품질
#정해진 카테고리에 속하는지 여부만 중요하고 숫자의 크기나 양은 의미가 없다
#연속형 데이터 : 숫자로 정확하게 표현하고, 중간값을 아주 세밀하게 나눠서 얼마든지 표시할 수 있는 데이터

#카이제곱 검정(Chi-square Test)
#카이제곱 검정은 두 가지의 범주형 데이터가 서로 관련이 있는지 없는지 판단하는 통계적 방법
#쉽게 말해 "두 범주(카테고리)가 서로 영향을 주는지 아니면 서로 관계가 없는지를 숫자로 판단해주는 방법"
#예로 들면 예상했던 숫자(기대값)와 실제 팔린 숫자 간의 차이를 나타낸게 카이제곱 통계량이다
#실제값과 기대값의 차이를 제곱한 뒤 기대값으로 나눈 값을 모두 더한 숫자

#카이제곱 검정 vs T-Test 차이
#카이제곱 검정은 두 가지 "카테고리"의 개수를 비교한다
#T-Test는 두 그룹의 "숫자 값(연속형)"을 비교한다

#반도체 공정에서 카이제곱 검정을 하는 이유
#반도체 회사는 웨이퍼 품질이 어떤 조건과 관련이 있는지 정확히 판단하고 싶어한다.
#예를 들어,
#장비 A에서 만든 웨이퍼 품질(Good 양호/Bad 품질) 개수
#장비 B에서 만든 웨이퍼 품질(Good 양호/Bad 품질) 개수
#처럼 장비라는 범주형 데이터와 웨이퍼 품질(Good 양호/Bad 품질)이라는 범주형 데이터 간에 실제로 관계가 있는지 확인할 때 카이제곱 검정을 사용한다.

#자유도란 "전체 결과 중에서 독립적으로(자유롭게) 선택할 수 있는 값의 개수"
#자유도 계산 공식
#자유도 = (범주형 데이터1 종류 개수 -1) * (범주형 데이터2 종류 개수 -1)


#문제
#압력 시간 이외의 다른 요소들의 T통계량, p밸류 값을 파이썬을 이용해 계산하고,
#Good, Bad에 영향을 주는 다른 요소가 있는지 찾아보아라
#defect_type에 영향을 주는 요소가 있는지 찾아보아라
#-> 2개씩 비교해도 되고(ttest) : t통계, pvalue
#-> ANOVA 테스트 해도 된다 : f통계, pvalue

import pandas as pd
from scipy.stats import ttest_ind, f_oneway

# 1. 데이터 불러오기
df = pd.read_csv('04_etching_process_1.csv')

# 분석 1: 웨이퍼 품질(Good/Bad)에 영향을 주는 다른 요소 찾기 (T-Test)
print("### 분석 1: 웨이퍼 품질(Good/Bad)에 영향을 주는 요소 분석 ###")
print("-" * 60)

# 분석할 대상 컬럼 리스트 정의 (압력, 공정 시간 제외)
# rf_power: RF 전력, etch_depth: 식각 깊이, uniformity: 균일도, defect_count: 결함 수
target_columns_1 = ['rf_power', 'etch_depth', 'uniformity', 'defect_count']

for col in target_columns_1:
    # Good 결과인 데이터의 해당 컬럼 값 추출 (결측치 제거)
    good_data = df[df['result'] == 'Good'][col].dropna()
    # Bad 결과인 데이터의 해당 컬럼 값 추출 (결측치 제거)
    bad_data = df[df['result'] == 'Bad'][col].dropna()

    # T-test 수행 (등분산 가정하지 않음: equal_var=False)
    t_statistic, p_value = ttest_ind(good_data, bad_data, equal_var=False)

    # 결과 출력
    print(f"변수명: {col}")
    print(f"  T-통계량 (T-statistic): {t_statistic:.5f}")
    print(f"  P-value (피밸류): {p_value:.5e}")

    # P-value에 따른 유의성 판단 (0.05 기준)
    if p_value < 0.05:
        print("  => 해석: Good/Bad 간에 통계적으로 유의미한 차이가 **있습니다** (영향을 줌).")
    else:
        print("  => 해석: Good/Bad 간에 통계적으로 유의미한 차이가 **없습니다**.")
    
    print("-" * 60)

print("\n" * 2) # 구분용 줄바꿈


# 분석 2: 결함 종류(defect_type)에 영향을 주는 요소 찾기 (ANOVA)
print("### 분석 2: 결함 종류(defect_type)에 영향을 주는 요소 분석 ###")
print("-" * 60)

# defect_type이 있는 데이터만 선택 (결함 종류 간 비교를 위함)
df_defects = df.dropna(subset=['defect_type'])

# 분석할 변수 목록 (압력, 공정 시간 포함 전체 확인)
target_columns_2 = ['pressure', 'rf_power', 'etch_depth', 'uniformity', 'process_time']

for col in target_columns_2:
    # 각 결함 종류(Particle, Scratch 등)별로 해당 변수 데이터 추출
    groups_data = []
    for dtype in df_defects['defect_type'].unique():
        data = df_defects[df_defects['defect_type'] == dtype][col].dropna()
        groups_data.append(data)
    
    # 데이터가 충분한지 확인 후 ANOVA 수행
    if all(len(g) > 1 for g in groups_data):
        f_statistic, p_value = f_oneway(*groups_data)
        
        print(f"변수명: {col}")
        print(f"  F-통계량 (F-statistic): {f_statistic:.5f}")
        print(f"  P-value (피밸류): {p_value:.5e}")
        
        if p_value < 0.05:
            print("  => 해석: 결함 종류(Particle vs Scratch) 간에 통계적으로 유의미한 차이가 **있습니다**.")
        else:
            print("  => 해석: 결함 종류 간에 통계적으로 유의미한 차이가 **없습니다**.")
    else:
        print(f"변수명: {col}")
        print("  => 데이터 부족으로 분석 불가")
    
    print("-" * 60)


    