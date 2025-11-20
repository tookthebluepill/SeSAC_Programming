#class 사용 연습

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def show_info(self):
        print(f"상품명: {self.name}, 가격: {self.price}원, 재고: {self.stock}개")
    
    def apply_discount(self, discount):
        self.price -= discount
        print(f"{self.name}의 가격이 {discount}원 할인되어 {self.price}원이 되었습니다.")

    def buy_product(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"{quantity}개 구매 완료! 남은 재고: {self.stock}개")
        else:
            print("재고가 부족합니다.")


product1 = Product("노트북", 1200000, 5)

print("\n=== 기존 상품 정보 ===")
product1.show_info()

print("\n=== 상품 구매 (2개) ===")
product1.buy_product(2)

print("\n=== 할인 적용 ===")
product1.apply_discount(100000)

print("\n=== 할인 후 상품 정보 ===")
product1.show_info()

print("\n=== 재고 부족 테스트 (5개) ===")
product1.buy_product(5)
