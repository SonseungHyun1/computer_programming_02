print("구구단을 출력합니다.\n")
for x in range(2,10):
    print("------["+str(x)+"단]------")
    for y in range (1,10):
        print(x,"X",y,"=",x*y)
print("-----------------")

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0],matrix[1],matrix[2])

for row in matrix:
    for element in row:
        print(element)

matrix = [[1,2,3],4,[5,6,7,8,9]]

total=0
for row in matrix:
    for element in row:
        total=total + element
#TypeError:'int' object is not iterable

# 디버깅을 위한 print 함수 사용
matrix = [[1,2,3],4,[5,6,7,8,9]]
total=0

for row in matrix:
    print("현재 행,첫번째 이중 반복문:",row)
    for element in row:
        print("현재 요소,두 번째 이중 반복문:",element)
        total = total + element
#현재 행,첫번째 이중 반복문: [1, 2, 3]
#현재 요소,두 번째 이중 반복문: 1
#현재 요소,두 번째 이중 반복문: 2
#현재 요소,두 번째 이중 반복문: 3
#현재 행,첫번째 이중 반복문: 4

# 실습
result=[]
numbers = [[1,2,3],[4,5,6],[7,8,9]]
for row in numbers:
    for n in row:
        if n%2 ==0:
            result.append(n)
print(result)

pingpong_list = ["나영","예진","원빈","현빈"]
results = []
def create_contents_of_mail(name):
    content = f"한국교통대학교 천하제일 탁구대회, {name}님 탁구 대회에 참여해주셔서 감사합니다.\n 행사 일시: 2023-10-06, 시간: 10:30 AM, 복장: 트레이닝 복\n행사 당일에 뵙겠습니다. 감사합니다."
    return content

for participant in pingpong_list:
    mail_content = create_contents_of_mail(participant)
    results.append(mail_content)

for mail in results:
    print(mail)

a=input("몇 단까지 출력할까요?")

def 구구단 (a):
    print("구구단을 출력합니다.\n")
    for x in range(1,20):
        print("------["+str(x)+"단]------")
    for y in range (1,19):
        print(x,"X",y,"=",x*y)
    print("-----------------")
