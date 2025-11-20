# #input을 활용한 숫자 입력과 int 숫자 변환
num = input("숫자를 입력하세요 : ")
print(num * 3)


num = input("숫자를 입력하세요 : ")
num = int(num)
print(num * 3)


num = int(input("숫자를 입력하세요 : "))
print(num * 3)


#input()을 활용한 계산기
num1 = input("첫 번째 숫자를 입력하세요 : ")
num1 = int(num1)

num2 = input("두 번째 숫자를 입력하세요 : ")
num2 = int(num2)

sum1 = num1 + num2
print("두 숫자의 합 : ", sum1)

#input()을 활용한 BMI 계산기
weight = input("몸무게를 입력하세요 (kg) : ")
weight = float(weight)

tall = input("키를 입력하세요 (m) : ")
tall = float(tall)
BMI = weight / tall**2
print("당신의 BMI는", BMI, "입니다.")