a=10
b=3

if a+b < 14:
    print ("Yeah,it it true.")


content="감자"
if content == "고구마" :
    print ("그것은 고구마입니다.")
elif content == "양파":
    print("그것은 양파입니다.")
else :
    print("그것은 감자입니다.")


age=input("나이를 입력하세요")
int(age)
if age < "19":
    print("미성년자입니다")
elif age >= "19":
    print("성인입니다")

x=5
y=10
if x>0 and y>0:
    print ("x와 y는 모두 양수입니다.")

content = "사과"
if content == "사과" or content =="감자" :
    print ("content는 사과이거나 감자입니다")

fruits=['키위','바나나','딸기']
for fruit in fruits:
    print (fruits)

dic={"과일":"키위",'숫자':'5','사람 이름':'맹구'}
for i in dic:
    print(dic[i])

hangle="가나다라마바사"
for j in hangle:
    print(j)

number = 1
while number < 5 :
    print(number)
    number = number + 1
else :
    print("number 변수가 5이상이면 종료합니다")

number =1
while number < 5:
    print(number)
    break
    number = number + 1
