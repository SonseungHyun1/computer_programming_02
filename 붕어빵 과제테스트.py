class Bungeoppang:
    def __init__(self, contents):
        self.contents = contents

    def sell(self):
        print(f"{self.contents} 붕어빵이 판매되었습니다.")

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

shukcream_bungeoppang = Bungeoppang("슈크림")
pat_bungeoppang = Bungeoppang("팥")

shukcream_bungeoppang.sell()
shukcream_bungeoppang.eat()

pat_bungeoppang.sell()
pat_bungeoppang.eat()
