#! /usr/bin/env python
""" #원의 반지름

import math
import sys
#r = int(input('넓이를 구하고자 하는 원의 반지름 : '))

r = int(sys.argv[1])
pi = math.pi
s = round(r**2 * pi, 2) #소수점 둘 째 자리에서 끊김

if len(sys.argv) != 2: #이거 길이를 가지고 판단한다. 
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()
print(s)


#다음 두 변수의 사칙연산, 나머지 연산, 제곱을 구해보세요
num1 = 3
num2 = 5
if len(sys.argv) != 3:
    print(f"#usage: python {sys.argv[0]} [n1] [n2]")
    sys.exit

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} x {n2} = {n1*n2}")
print(f"{n1} / {n2} = {n1/n2}")
#홀짝 판별
import sys
if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

num = int(sys.argv[1])
result = "odd"
if num % 2 ==0:
    result = "even"
print(result)

#3배수인지 7배수인지 판별
import sys
if len(sys.argv) !=2:
    print(f"#usage: python {sys.argv[0]} [n1]")
    sys.exit()
n1 = int(sys.argv[1])
result = "neither 3,7"
if n1 % 3 == 0 and n1 % 7 == 0:
    result = "3,7"
elif n1 % 3 == 0:
    result = "3"
elif n1 % 7 == 0:
    result = "7"
print(result)

#006.for
#1부터 10까지 숫자 합을 구하는 프로그램
#나
import sys

if len(sys.argv) != 3:
    print(f"#usage: python {sys.argv[0]} [n1] [n2]")
    sys.exit()

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
 

#강사님
val = 0
for i in range(1,11):
    val += i
print(val) #pseudo code 의사 코드
""""""
In [1] : range(1,10)
Out [1] : range(1,10)

In [2] : list(range(1, 10))
Out [2] : [1,2,3,4,5,6,7,8,9]

In [3] : list(range(1,11))
Out [3] : [1,2,3,4,5,6,7,8,9,10]

In[4] : 

#006 for 이거 곱으로 바꿔보자

val = 1
for i in range(1,11):
    val *= i
print(val) #pseudo code 의사 코드

#007은 각자 하기

#008 while 문
#while문 사용하여 5! 값 구하기
import sys
n = int(sys.argv[1])
result = 1

while n > 0:
    result *= n
    n -= 1

print(result)

"""
#009 함수
#greet라는 이름의 함수를 만든 후 이 함수를 호출할 때마다 "Hello, Bioinformatics"를 ㅜㄹ력하는 프로그램을 작성해보시오.
def greet():
    print("Hello Bioinformatics")   #d여기까진 함수 정의만 한거
def greet1(name):
    print(f"Hello, {name}")        #여기서 함수값이 하나고 return이 없기 때문에 none으로 뜬다.
#num은 int다
def greet2(num): 
    return num * 2
greet()
ret1 = greet1("YJ")
print(ret1)   #이렇게 쓰면 none으로 나온다. "YJ"는 str이기 때문
greet1("YJ")

ret2 = greet2(3)
print(greet2(3))





