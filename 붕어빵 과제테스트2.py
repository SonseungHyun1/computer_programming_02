class Bungeoppang:
    total_sales_all = 0  # 클래스 변수로 모든 객체의 총 판매금을 관리

    def __init__(self, contents, price):
        self.contents = contents
        self.price = price
        self.total_sales = 0

    def sell(self):
        print(f"{self.contents} 붕어빵이 {self.price}원에 판매되었습니다.")
        self.total_sales += self.price
        Bungeoppang.total_sales_all += self.price

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

    def display_total_sales(self):
        print(f"{self.contents} 붕어빵의 개별 판매금: {self.total_sales}원")
        print(f"전체 총 판매금: {Bungeoppang.total_sales_all}원")


shukcream_bungeoppang = Bungeoppang("슈크림", 1500)
pat_bungeoppang = Bungeoppang("팥", 1200)

shukcream_bungeoppang.sell()
shukcream_bungeoppang.eat()
shukcream_bungeoppang.display_total_sales()

pat_bungeoppang.sell()
pat_bungeoppang.eat()
pat_bungeoppang.display_total_sales()
