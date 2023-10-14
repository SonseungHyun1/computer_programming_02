# 붕어빵 판매를 해보겠습니다.
class fishbread:
    def __init__(self,kind,bread):
        self.kind = kind
        self.bread = bread

    def Redbeen(self):
        print(self.kind+"이 팔렸습니다")
    def Cream(self):
        print(self.kind+"이 팔렸습니다")


my_fishbread2 = fishbread("팥","붕어빵")
my_fishbread = fishbread("크림","붕어빵")

my_fishbread2.Redbeen()
my_fishbread.Cream()

a=input("뭐드릴까요")
