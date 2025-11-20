# Series는 하나의 열을 나타낸다.
# import pandas as pd
# ages = pd.Series([25, 30, 22, 28, 35])
# print(ages)


# 리스트로 데이터프레임 만들기
import pandas as pd
data = [
    ["김철수", 25, 175],
    ["이영희", 30, 162],
    ["박지민", 22, 168]
]

df = pd.DataFrame(data, columns=["학생 이름", "나이", "키"])
print(df)

# 딕셔너리로 데이터프레임 만들기
import pandas as pd
data = {
    "학생이름" : ["김철수", "이영희", "박지민"],
    "나이" : [25, 30, 22],
    "키" : [172, 162, 168]
}

df = pd.DataFrame(data)
print(df)
