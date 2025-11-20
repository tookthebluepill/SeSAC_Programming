# #Cp 계산
# import numpy as np
# import pandas as pd

# #파일 읽기
# pd.read_csv("02_oxide.csv")

# #1. 산화막 두께 데이터 가져오기
# oxide_df = pd.read_csv("02_oxide.csv")
# #oxide_df 확인
# print(oxide_df.head())

# oxide_thickness = oxide_df["oxide_thickness"]
# print(oxide_thickness)

# #2. 표본 표준 편차 계산
# std_thickness = oxide_df["oxide_thickness"].std()

# #3. 공정에서 허용되는 산화막 두께의 범위를 설정
# LSL = 220 # 최소 두께 (하한 한계)
# USL = 400 # 최대 두께 (상한 한계)

# #4. 공정능력지수(cp) 계산 공식 적용
# cp_value = (USL - LSL) / (6 * std_thickness)

# #5. 계산된 cp 값을 소숫점 2자리까지 출력
# print(f"공정능력지수 (cp):{cp_value: .2f}")


#Cpk 계산
import numpy as np
import pandas as pd

#파일 읽기
# pd.read_csv("02_oxide.csv")

#1. 산화막 두께 데이터 가져오기
oxide_df = pd.read_csv("02_oxide.csv")
#oxide_df 확인
print(oxide_df.head())

oxide_thickness = oxide_df["oxide_thickness"]
print(oxide_thickness)

#2. 표본 표준 편차 계산
mean_thckness = oxide_thickness.mean()
std_thickness = oxide_thickness.std()

#3. 공정에서 허용되는 산화막 두께의 범위를 설정
LSL = 220 # 최소 두께 (하한 한계)
USL = 400 # 최대 두께 (상한 한계)

#4. 공정능력지수(cp) 계산 공식 적용
cpk_lower = (mean_thckness - LSL) / (3 * std_thickness)
cpk_upper = (USL - mean_thckness) / (3 * std_thickness)
cpk_value = min(cpk_lower, cpk_upper)

#5. 결과 출력
print(f"공정 성능 지수 Cpk: {cpk_value:.2f}")