content = "감자"
if content == "고구마":
    print("그것은 고구마입니다.")
elif content =="양파":
    print("그것은 양파입니다.")
else :
    print("그것은 감자입니다.")
# content 를 감자로 지정
# if 문으로 고구마라면 "그것은 고구마 입니다" 출력
# elif 로 조건문을 순차적으로 검사, 1번 조건문이 거짓이면
# 해당 조건이 참일 경우 "그것은 양파입니다" 출력
# else로 모두 거짓일 경우 "그것은 감자입니다" 출력

#if 조건문 실습
# 사용자의 나이를 입력 받고 입력 받은 나이가 19 보다 크면 "성인 입니다"를 출력
# 그렇지 않으면 "미성년자입니다" 출력
# input() 함수 사용

a=input("나이를 입력하세요:")
a=int(a)
if a >= 19:
    print("성인입니다")
elif a<19:
    print("미성년자입니다.")
# 틀린 점 =>   int() 변환

# and 예제
x=5
y=10
if x>0 and y>0:
    print ("X와 Y는 모두 양수입니다.")

# or 연산자 예제
content = "사과"
if content == "사과" or content == "감자":
    print("content는 사과이거나 감자입니다.")

# fot 반목문 list 예제
fruits = ["사과","바나나","딸기"]
for fruit in fruits:
    print (fruit)
# 변수 할당 자료 fruits 가 리스트
# fruit에 반복적으로 변수 할 당으로 각각 사과, 바나나, 딸기가 출력

# for 반복문 dictionary 예제
dic = {"과일":"사과","숫자":3,'사람이름':'손승현'}
for i in dic:
    print(i,dic[i])

# for 반복문의 변수 할당 자료가 문자열일 경우 변수에 문자가 순서대로 할당
hangle = "가나다라마바사"
for j in hangle:
    print(j)

# for 반복문의 변수 할당 자료가 지정범위 함수(range) 경우
for k in range(0,10):
    print(k)

# while 조건문1 :
  #변수가 자료에 할당되는 동안 수행 할 코드
# else:
    # 변수가 자료에 할당되는 동안 수행 할 코드 -> 조건문 1이 거짓일 때 실행할 코드 블록이며 반복은 하지 않음.

# while 반복문 예제
content = "사과 같은 배"

while content == "사과":
    print("사과입니다.")
else:
    print("사과가 아닌 다른 것이므로 코드 실행을 중지합니다.")
# while 반복문은 범위 설정이 없는 무한 반복문이기 때문에 무한 반복이 되는 것을 멈추려면
# 조건문을 활용한 반복제어 또는 Break를 활용한 반복 제어로 중지시킬 수 있다.

# while 반복문의 종료
number =1

while number <5 :
    print(number)
    number=number+1
else:
    print("number 변수가 5 이상이면 종료합니다.")

# 이중반복문
# for 변수1 in 변수 2:
    #for 변수2 in 범위 2:
# 변수1과 변수2를 사용

# 이중반복문 활용 (구구단)
print("구구단을 출력합니다\n")
for x in range(2,10):    # 구구단 단수
    print("------[" +str(x) + "단]------")
    for y in range(1,10):  # 단수뒤에 곱해지는 수  # 1부터 9까지
        print(x,"X",y,"=",x*y)
print("---------------------------")

# 다차원 리스트를 활용한 이중 반복문
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0],matrix[1],matrix[2])

for row in matrix:
    for element in row:
        print(element)

#다차원 리스트를 활용한 이중 반복문
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0],matrix[1],matrix[2])

print(matrix[0][0])

for row in matrix:
    for element in row:
        print(element)

# 디버깅 = 버그를 찾아내고 해결하는 과정
matrix=[[1,2,3],4,[5,6,7,8,9]]
total = 0

for row in matrix:
    for element in row:
        total = total + element
  # TypeError: 'int' object is not iterable - 확인 할 수 있는 오류

for row in matrix:
    print("현재 행,첫번째 이중 반복문:",row)
    for element in row:
        print("현재 요소,두 번째 이중 반복문:",element)
        total = total + element
        # 현재 행,첫번째 이중 반복문: [1, 2, 3]
        # 현재 요소,두 번째 이중 반복문: 1
        # 현재 요소,두 번째 이중 반복문: 2
        # 현재 요소,두 번째 이중 반복문: 3
        # 현재 행,첫번째 이중 반복문: 4

# 이중반복문과 디버깅 실습
# 다차원 리스트(행렬)와 이중 반복문을 사용하여 1~9까지 숫자의 짝수
# 판별기 프로그램을 개발하시오. 1~9까지의 숫자 중 짝수인 숫자를
# results = [] 리스트에 추가하여 최종 결과 results를 출력하시오.
# 다차원 리스트 numbers = [[1,2,3], [4,5,6], [7,8,9]]
# 짝수 판별 방법 조건문과 % 연산자를 활용(% 연산자는, A % B A를 B로 나누었을 때의 나머지를 연산 결과로 출력)
# 리스트에 요소 추가 함수: “리스트 변수.append(추가할 요소)”

result=[]   # result 리스트 생성
numbers=[[1,2,3], [4,5,6], [7,8,9]]  # numbers 리스트 생성
for row in numbers: # numbers가 row에 포함되는 반복문
    for n in row: # row가 n에 포함되는 반복문
        if n%2 == 0:  #n을 순차적으로 2로 나눠 0이 되는 요소를 구함
            result.append(n) #if문으로 나온 요소를 result 리스트에 추가
print(result)

# 함수
# def 함수명 매개변수 :
 # 들여쓰기 / 코드블록, 함수에서 실행할 코드
 # return value / 코드블록 실행 이후 결과값

# 두 수를 더하는 함수
def add_numbers(a,b):
    result = a+b
    return  result

# 함수 호출 및 반환값 사용
sum_result = add_numbers(5,3)
print("합계:",sum_result)

#• 함수를 정의하고 사용하기 위해서는 다음과 같은 단계 필요
# 1. 함수 정의(함수 이름, 매개변수, 코드 블록, 리턴 값 설정)
# 2. 함수 호출(함수 이름과 함수에 필요한 매개변수 입력)
# 3. 함수 실행(함수 정의에 의해 설계된 코드 블록 실행)
# 4. 리턴 값 반환(코드 블록 실행 후 결과 값 반환)
# 5. 리턴 값을 변수에 재할당하여 사용

# 실습 탁구 대회 메일 보내기
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

# class
# 파스타 클래스 (레시피 북) 정의
class Pasta:
    def __init__(self,pasta_type,sauce):
        self.pasta_type=pasta_type
        self.sauce=sauce

    def cook(self):
        return f"{self.pasta_type} 파스타가 {self.sauce} 소스와 함께 완성되었습니다."

# 객체(요리) 생성
spaghetti = Pasta("토마토","토마토")
linguine = Pasta("린귄","크림")

# 요리 (객체) 출력ㄴ
print(spaghetti.cook())
print(linguine.cook())

#(출력) 토마토 파스타가 토마토 소스와 함께 완성되었습니다.
#(출력) 린귄 파스타가 크림 소스와 함께 완성되었습니다.



