import pickle
import os # 파일 존재 여부를 확인하기 위해 os 모듈을 import 합니다.

FILE_NAME = 'cart_data.pickle'
cart = []

#1. 파일에서 장바구니 내용 불러오기
if os.path.exists(FILE_NAME):
    try:
        with open(FILE_NAME, 'rb') as f:
            cart = pickle.load(f)
        print(f"[{FILE_NAME} 로딩 완료] 장바구니에 {len(cart)}개의 물건이 로드되었습니다.")
    except Exception as e:
        print(f"데이터 로드 중 오류 발생: {e}")
        cart = [] # 오류 발생 시 장바구니 초기화
else:
    print(f"[{FILE_NAME} 파일 없음] 새로운 장바구니를 시작합니다.")

def save_cart():
    """장바구니 내용을 파일에 저장하는 함수"""
    try:
        with open(FILE_NAME, 'wb') as f:
            pickle.dump(cart, f)
        # print(f"장바구니 내용이 {FILE_NAME}에 성공적으로 저장되었습니다.") # 불필요한 메시지는 생략
    except Exception as e:
        print(f"데이터 저장 중 오류 발생: {e}")


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
        save_cart()

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
                save_cart()
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
        # save_cart() # 종료 시점에 저장하는 대신, 변경 시마다 저장하도록 처리 (선택 사항)
        print("프로그램을 종료합니다. 감사합니다!")
        break
    else:
        print("잘못된 입력입니다! 1~4번 중에서 선택해주세요.")