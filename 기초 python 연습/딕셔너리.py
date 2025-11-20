# #성적 관리 예제
# scores = {
#     "철수" : 85,
#     "영희" : 92,
#     "민수" : 78
# }

# #특정 학생 점수 출력
# print(scores["영희"])

# #새로운 학생 추가
# scores["지수"] = 90
# print(scores)

# #점수 수정
# scores["철수"] = 95
# print(scores)


# #딕셔너리 반복문
# for name, score in scores.items():
#     print(f"{name}의 점수는 {score}점입니다.")



# #음식 주문 목록 관리 예제
# orders = {
#     "김철수" : {"김치찌개" : 1, "불고기" : 2},
#     "이영희" : {"된장찌개" : 1, "비빔밥" : 2}
# }

# for customer, menu in orders.items():
#     print(f"{customer}님의 주문 내역:")

#     for food, quantity in menu.items():
#         print(f"- {food}: {quantity}개")

#     print()


#최근 3개월 미구매 고객 찾기
from datetime import datetime
orders = [
    {"고객명": "철수", "구매일": "2024-01-01"},
    {"고객명": "영희", "구매일": "2024-10-10"}
]

cutoff = datetime.strptime("2024-03-01", "%Y-%m-%d")

inactive_customers = []

for order in orders:
    name = order["고객명"]
    date = datetime.strptime(order["구매일"], "%Y-%m-%d")
    if (cutoff - date).days > 90:
        inactive_customers.append(name)

print(f"이탈 고객: {inactive_customers}")