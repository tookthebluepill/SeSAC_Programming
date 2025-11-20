#if-else문
#내가 가진 돈 10000원 설정
#음식 가격 5000원
#내 돈이 음식 가격보다 많거나 같으면 "식사를 합니다"
#그 외에는 "집에 갑니다" 출력

# money = int(input("가진 돈 : "))
# price = int(input("음식 가격 : "))
# if money >= price:
#     print("식사를 합니다")
# else:
#     print("집에 갑니다")


#if-elif-else문
#가진돈 10000원 이상-> 스테이크 주문
#가진돈 5000원 이상-> 피자 주문
#가진돈 3000원 이상-> 햄버거 주문
#그 외-> 라면 주문

money = int(input("가진 돈 : "))
if money >= 10000:
    print("스테이크를 주문합니다")
elif money >= 5000:
    print("피자를 주문합니다")
elif money >= 5000:
    print("햄버거를 주문합니다")
else:
    print("라면을 주문합니다")
