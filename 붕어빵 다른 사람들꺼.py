



class 붕어빵가게:
    def __init__(self, 종류, 가격):
        self.종류 = 종류
        self.price = 가격
        self.total = 0  # 초기 총 판매금은 0으로 설정

    def sell(self):
        print(f"{self.종류} 붕어빵이 {self.price}원에 판매되었습니다.")
        self.total += self.price  # 가격을 총 판매금에 더함

    def eat(self):
        print(f"{self.종류} 붕어빵을 먹습니다.")

    def get_total_sales(self):
        print(f"총 판매금: {self.total}원")

# 객체 생성
슈크림붕어빵 = 붕어빵가게("슈크림", 1500)
팥붕어빵 = 붕어빵가게("팥", 1200)
피자붕어빵 = 붕어빵가게("피자", 2000)

# 붕어빵 판매 및 먹기
슈크림붕어빵.sell()
슈크림붕어빵.eat()

팥붕어빵.sell()
팥붕어빵.sell()
팥붕어빵.eat()

피자붕어빵.sell()
피자붕어빵.sell()
피자붕어빵.sell()
피자붕어빵.eat()

# 총 판매금 출력
슈크림붕어빵.get_total_sales()
팥붕어빵.get_total_sales()
피자붕어빵.get_total_sales()



class Bungeoppang:
    total_sales = 0

    def __init__(self, contents, price):
        self.contents = contents
        self.price = price

    def sell(self):
        print(f"{self.contents} 붕어빵이 {self.price}원에 판매되었습니다.")
        Bungeoppang.total_sales += self.price

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

cream_bungeoppang = Bungeoppang("슈크림", 2000)
redbean_bungeoppang = Bungeoppang("팥", 1500)

cream_bungeoppang.sell()
redbean_bungeoppang.sell()

cream_bungeoppang.eat()
redbean_bungeoppang.eat()

print(f"총 판매금은 {Bungeoppang.total_sales}원 입니다.")
