class Bungeoppang:
    print("---------메뉴판---------")
    menu = { "팥": 1000, "슈크림": 1200, "피자": 1500,"대왕":8000}
    total_sales_all = 0

    def __init__(self, contents, quantity):
        self.contents = contents
        self.price = Bungeoppang.menu[contents]
        self.quantity = quantity

    def sell(self):
        print(f"{self.contents} 붕어빵 {self.quantity}개가 {self.price * self.quantity}원에 판매되었습니다.")
        Bungeoppang.total_sales_all += self.price * self.quantity

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

    def total_sales(self):
        print(f"전체 총 판매금: {Bungeoppang.total_sales_all}원")
        print("---------------------------------------------")


def main():
    for item, price in Bungeoppang.menu.items():
        print(f"{item}: {price}원")

    while True:
        choice = input("무슨 붕어빵을 드시겠습니까? (팥, 슈크림, 피자, 대왕): ")

        quantity = int(input(f"{choice} 붕어빵 몇 개를 구매하시겠습니까? "))
        bungeoppang = Bungeoppang(choice, quantity)

        bungeoppang.sell()
        bungeoppang.eat()
        bungeoppang.total_sales()


if __name__ == "__main__":
    main()
