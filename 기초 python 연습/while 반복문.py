#ATM 비밀번호 입력 기능 프로그램
#비밀번호를 3번까지 입력
#비밀번호를 맞추면 "서비스 시작"
#3번 다 틀리면 "서비스 이용 제한" 출력 후 프로그램 종료

password = "1234"
tries = 0

while tries < 3:
    input_password = input("비밀번호를 입력하세요: ")
    
    if input_password == password:
        print("비밀번호 확인 완료! 서비스 시작합니다.")
        break
    else:
        tries += 1
        print(f"비밀번호가 틀렸습니다. 남은 기회: {3 - tries}번")

if tries == 3:
    print("비밀번호 3회 실패! 서비스 이용이 제한됩니다.")