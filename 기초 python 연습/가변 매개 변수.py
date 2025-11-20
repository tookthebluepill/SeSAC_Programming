def FixedBox(물건1, 물건2):
    print(f"첫 번째 물건: {물건1}")
    print(f"두 번째 물건: {물건2}")

FixedBox("사과", "바나나")

def FixedBox(*물건들):
    print("상자에 담긴 물건 목록:")
    for 물건 in 물건들:
        print(f"- {물건}")

FixedBox("사과", "바나나", "오렌지")
FixedBox("연필", "공책")
FixedBox("노트북", "마우스", "키보드", "스피커")



#소개글 만들기 예제
def make_introduction_letter(name, age, *hobbies):
    print(f"안녕하세요, 저는 {name}입니다.")
    print(f"나이는 {age}살입니다.")

    if hobbies:
        print("제 취미는 다음과 같습니다.")

        for hobby in hobbies:
            print(f"- {hobby}")
    else:
        print("취미는 아직 없습니다.")
    print()

#예시
make_introduction_letter("철수", 25, "축구", "독서", "게임")
make_introduction_letter("영희", 30, "요리", "등산")
make_introduction_letter("민수", 20)