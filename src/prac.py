#! /usr/bin/env python
# 210706 자습용 연습장
"""
#008 while문 사용하여 5!의 값을 구해보시오
i = 5
s = 1
while i >0:
    s *= i
    i -= 1
print(s)

#008-1 사용자로부터 입력값을 받아(n) n!의 값을 구해보시오
#풀이1

i = input("값을 입력하시오. :")

try:
    s = int(i)
    r = 1
    while s > 0:
        r *= s
        s -= 1
    print(f"{i}! : ", r)
except ValueError:
    print("숫자를 입력하세요.")

#009 greet라는 이름의 함수를 만든 후, 이 함수를 호출할 때마다 "Hello, BI"를 출력하는 프로그램을 작성해보시오.

def greet():
    print("Hello, BI")
greet()

#10 muSum이라는 이름의 함수를 만든 후, 이 함수에 (2, 3), (5,7),(10,15)를 함수의 값으로 전달하여 전달한 두 수를 더하여 출력하는 프로그램을 작성해보시오.

def mySum(n1, n2):
    r = int(n1) + int(n2)
    print(f"{n1} + {n2} : ", r)

mySum(2, 3)
mySum(5, 7)
mySum(10, 15)


#11     *여기 문자 입력했을 때 출력 마지막에 {}! none! 뜨는데 왜 뜨지
inPut = input("값을 입력하시오. : ")
def Factorial():
    try:
        result = 1
        num = int(inPut)
        while num >0:
            result *= num
            num -= 1
        return result
    except ValueError:
        print("숫자를 입력하시오.")
     
result = Factorial()
print(f"{inPut}! = ", result)


n = int(input("값을 넣으시오. :"))
def Factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

result = Factorial(n)
print(f"{n}! = : ", result)
#13
name = input("이름을 입력하세요. : ")
print(f"Hello, {name}")

#14
i = input("한 글자 : ")
w_cnt = " ".join(i)

if len(w_cnt) >= 2:
    print("한글자만 입력하세요")
else: 
    if i.isalpha():
        print("moooonjja")
    else: 
        print("soootjja")

#15
import sys
s = sys.argv[1]
print(f"Hello, {s}")
"""

# 재귀호출 연습
# 재귀호출로 회문 판단하기.

