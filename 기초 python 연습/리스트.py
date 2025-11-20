#장바구니 예제
cart = []

while True:
    print("\n===== 장바구니 프로그램 ====")
    print("1. 물건 추가")
    print("2. 물건 삭제")
    print("3. 장바구니 보기")
    print("4. 프로그램 종료")

    choice = input("원하는 기능의 번호를 입력하세요: ")

#1. 물건을 장바구니에 추가하는 기능
    if choice == "1":
        item = input("추가할 물건의 이름을 입력하세요: ")
        cart.append(item)
        print(f"'{item}'이(가) 장바구니에 추가되었습니다.")
        print(f"현재 장바구니에는 {len(cart)}개의 물건이 있습니다.")

#2. 물건을 장바구니에서 삭제하는 기능

    elif choice == "2":
        if len(cart) == 0:
            print("삭제할 물건이 없습니다!")
        else:
            item = input("삭제할 물건의 이름을 입력하세요: ")
            if item in cart:
                cart.remove(item)
                print(f"'{item}'이(가) 장바구니에서 삭제되었습니다.")
                print(f"현재 장바구니에는 {len(cart)}개의 물건이 있습니다.")
            else:
                print("장바구니에는 없는 물건입니다.")


#3. 장바구니에 있는 물건들을 확인하는 기능
    elif choice == "3":
        if len(cart) == 0:
            print("장바구니가 비어 있습니다.")
        else:
            print("현재 장바구니 내용:", cart)
            print(f"현재 장바구니에는 {len(cart)}개의 물건이 있습니다.")

#4. 프로그램을 종료하는 기능
    elif choice == "4":
        print("프로그램을 종료합니다. 감사합니다!")
        break
    else:
        print("잘못된 입력입니다! 1~4번 중에서 선택해주세요.")