#귀무가설과 대립가설
#귀무가설이란? H_0
#현재 상태가 정상이고 변화가 없다는 기본적인 주장
#원래 상태가 정상이라고 믿는 주장

#대립가설이란? H_1
#귀무가설과 반대로 "변화가 생겼다", "정상이 아니다"는 주장
#우리가 이상이나 변화가 있다고 생각하는 주장

#반도체 공정에서 통계적 가설 검증은 어떻게 사용되나?
#실제 공정에서 두 장비 각각 웨이퍼 몇 장을 뽑아 두꼐, 저항값, 전기적 특성 등 품질 데이터를 측정한다.
#만약 우연히 품질 차이가 발생할 확률이 매우 낮다면(예: 확률 5% 이하) 귀무가설을 버리고 "장비 간 품질 차이가 존재한다"라고 결론 내린다

#T-Test(티 검정)
#티 검정은 두 그룹의 평균(평균값)이 서로 의미 있게 다른지, 아니면 차이가 별로 없는지 통계적으로 확인할 때 사용.
#특히 표본 크기가 작을 때 유용하며, 반도체 공정에서는 장비 간 성능 차이, 공정 변수의 영향 등을 객관적으로 분석하는 데 활용

#T-Test는 크게 두 가지로 나뉜다
#-독립 표본 T-Test
#서로 다른 두 집단 간의 평균 비교할 때 사용 (예: 서로 다른 압력 조건으로 만든 웨이퍼 품질 비교)
#-대응 표본 T-Test
#같은 대상에서 처리 전후를 비교할 때 사용한다 (예: 장비 수리 전 vs 수리 후 비교)

#p-value란?
#우연히 평가 점수 차이가 이렇게 크게 날 확률이 얼마나 되는가?를 숫자로 나타낸 값
#일반적으로 p-value의 기준점은 0.05(5%)이다.

#p-value <= 0.05
#우연이 아닌 실제 의미 있는 차이

#p-value > 0.05
#우연히 나타난 결과일 가능성이 큼

import pandas as pd
from scipy.stats import ttest_ind
df = pd.read_csv('04_etching_process_1.csv')
df.head()

good_pressure = df[df['result'] == 'Good']['pressure'].dropna()
print(good_pressure.head())
bad_pressure = df[df['result'] == 'Bad']['pressure'].dropna()
print(bad_pressure.head())

print(good_pressure.mean())
print(bad_pressure.mean())

t_statistic, p_value = ttest_ind(
    good_pressure,
    bad_pressure,
    equal_var=False
)

print("T-통계량(T-statistic):", t_statistic)
print("p-value(피밸류):", p_value)