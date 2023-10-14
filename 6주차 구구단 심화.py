var = int(input("몇 단까지 출력할까요?"))
print(var, type(var))

print("구구단을 출력합니다.\n")
def 구구단(var):
    if var < 10:
        for x in range(2, var+1):
            print("------["+str(x)+"단]------")
            for y in range (1, 10):
                print(x, "X", y, "=", x*y)
    elif var < 19:
        for x in range(2, var+1):
            print("------["+str(x)+"단]------")
            for y in range (1, var+1):
                print(x, "X", y, "=", x*y)

구구단(var)
print("-----------------")

