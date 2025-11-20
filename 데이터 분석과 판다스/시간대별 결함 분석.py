import pandas as pd

file_path = "02_oxide.csv"
oxide_df = pd.read_csv(file_path)

print(oxide_df)

#process_data(날짜)와 process_time(시간)을 합쳐서 process_datetime 칼럼을 새로 만든다.
oxide_df['process_datetime'] = pd.to_datetime(oxide_df['process_date'] + ' ' + oxide_df['process_time'])
print(oxide_df)

#하루를 오전(Morning), 오후(Afternoon), 밤(Night)으로 나누는 함수
def get_time_of_day(hour):
    if 6<=hour<12:
        return 'Morning'
    elif 12<=hour<18:
        return 'Afternoon'
    else:
        return 'Night'
    
#각 데이터에 시간대 정보 추가(오전, 오후, 밤)
#dt.hour -> process_datetime에서 시간만 추출
#.apply(get_time_of_day) -> 추출한 시간을 get_time_of_day() 함수로 변환하여 시간 분류
oxide_df['time_of_day'] = oxide_df['process_datetime'].dt.hour.apply(get_time_of_day)
print(oxide_df)

defect_df = oxide_df[oxide_df['defect_type'] != 'none']
print(defect_df)

#시간대별로 결함 유형별 결함 수를 피벗 테이블로 정리
time_defect_analysis = pd.pivot_table(
    defect_df,
    index='time_of_day',
    columns='defect_type',
    values='defect_count',
    aggfunc='sum',
    fill_value=0
)

print(time_defect_analysis)