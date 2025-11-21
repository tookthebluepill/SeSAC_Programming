import pandas as pd
df = pd.read_csv('03_wafer_receipe_1.csv')
print(df.head())
print(df.info())
print(df.describe())


#df에서 박막 두께를 측정한 열만 선택해서 thickness_df에 저장
thickness_df = df.loc[ : , "THK_Pos_1":"THK_Pos_10"]
print(thickness_df.head())

#thick_df에 있는 10개의 박막 두께를 행별로 평균 내서 Mean_Thckness라는 새로운 열을 만들어 df에 추가한다.
df['Mean_Thickness'] = thickness_df.mean(axis=1)
df['Max_Thickness'] = thickness_df.max(axis=1)
df['Min_Thickness'] = thickness_df.min(axis=1)
#표준편차
df['Std_Thickness'] = thickness_df.std(axis=1)

#박막 두께의 균일도
df['Unif'] = (df['Max_Thickness'] - df['Min_Thickness'] / (2 * df['Mean_Thickness'])) * 100
print(df.head)

#증착 속도
df['Deposition Rate'] = df['Mean_Thickness'] / df['Time']
print(df.head)

#새롭게 계산된 데이터를 다시 CSV 파일 형태로 저장
#encoding='utf-8-sig' : 파일의 한글이나 특수 문자가 깨지지 않도록 안전하게 저장
df