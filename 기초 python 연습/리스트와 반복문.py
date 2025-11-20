# friends = ["철수", "영희", "민수"]

# for friends in friends:
#     print(f"{friends}야, 안녕!")


#리스트와 반복문을 활용한 평균 구하기
#5명의 학생 이름, 점수
#점수를 모두 더하고, 평균 점수를 구하는 프로그램
#단순히 숫자만 출력하는 게 아니라, 각 학생의 점수와 계산과정도 출력

students = ["민수", "영희", "철수", "지수", "준호"]
scores = [78, 92, 85, 88, 90]
total = 0
sum = "총합 = "

for idx, score in enumerate(scores):
    total += score

    sum += f"{students[idx]}({score})"

    if idx < len(scores) -1:
        sum += " + "
    
avg = total / len(scores)

print(sum + f" = {total}점")
print(f"평균 = {total} / {len(scores)}명 = {avg:.1f}점")
