#! /usr/bin/env python
"""
#아니 2시까지 스크립트 다 날아감.....
#울어

#020 문자열 더하기
#두 개의 변수를 선언한 후 각각 Bio와 Informatics를 넣은 후 다른 변수에는 두 변수를 합친 값을 집어넣고 출력해보세요.
a1 = "Bio"
a2 = 'Informatics'
a3 = a1 + a2
print(a3)

#여기서 부터 클래스 간단히 설명

class A:
    def __init__(self):
        val = ""

a1 = A() -> a1.val 출력하면 ''(아무것도 없는거) 나옴
a2 = A() -> a2.val 마찬가지
al.val = "a"
a2.val = "b"

a1.val + a2.val -> ab가 나올 것
근데 해보고 싶은건
Calss A:
    def __init__(self.val):
    def __add__(self,other):
        return self.val + other.val
a1 = A("a")
a2 = A("b")
a1.val + a2.val -> "ab"
a1+a2

#여기에 다시 코딩으로 설명해볼게
class A:
    def __init__(self,val):
        self.val = val
    def __add__(self,other):
        return self.val + other.val

    def __mul__(self, other):
        return "__mul__"

a1 = A("a")
a2 = A("b")

print(a1.val + a2.val)
print(a1 +a2)
print(a1 * a2)

#vcf : 정의를 담고 있는 파일
""""""
#ValueCalculator 이거 Class 만들어서 해보겠음

class ValusCalculator:
    def __init__(self, val:str):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

#그리고 calculatorrunner 하나 더 해 봄. 이거 새로운 파일 만들거임

#021 문자열 n번째 출력하기

seq1 = "AGTTTATAG"
print(seq1[5])


#022문자열 나누기

seq1 = "AGTTTATAG"
print(seq1[3:6])

#023 문자열 길이 구하기

seq1 = "AGTTTATAG"
print(len(seq1))

#024 문자열 대소문자 변환하기

seq1 = "ATGttATaG"
print(seq1.upper())
print(seq1.lower())

#025 문자열 n씩 건너뛰며 출력하기
seq1 = "ATGTTATAG"

print(seq1[0:9:3])

#강사님
for i in range(0, len(seq1),3):
    print(seq1[i])
#026
for i in range(0, len(seq1), 3):
    print(seq1[i:i+3])

#027
#print(seq1[::-1])

#028 문자열 바꾸기
comp_seq = ""
comp_data = {"A":"T", "T":"A","G":"C","C":"G"}
for s in seq1:
    comp_seq += comp_data[s]
print(seq1)
print(comp_seq)
print()
for i in range(len(seq1)):
    s = seq1[i]
    cs = comp_seq[i]
    bond = "≡"
    if s == "A" or s == "T":
        bond = "="
    print(f"{s}{bond}{cs}")

#029
print("C" in seq1)

#030 문자열 index 번호 출력하기  이거 마크로젠 입사 코딩 문제
seq1 = "AGTTTATAG"
#강사님 1번

for i in range(len(seq1)):
    s = seq1[i:i+2]
    print(i, s, s=="TT")

#내가 한 거 = 강사님 2번
for i in range(len(seq1)):
    s = seq1[i:i+2]
    if s =="TT":
        print(i)
"""
#031
#문자열 AA, AC, AG, AT를 쉼표 기준으로 리스트로 바꿔보세요
#split(",") 쓰면 된다
s = "AA,AC,AG,AT"
data = s.split(",")
print(data)
#032
data.append("CA")
print(data)
#033
print(data[::-1])

#034
data = [3,1,1,2,0,0,2,3,3]
print(max(data))
print(min(data))

#035
#리스트 [3,1,1,2,0,0,2,3,3]에서 각 요소의 출현 빈도를 사전으로 세어보세요.

cnt = dict()

for i in data:
    if i not in cnt:
        cnt[i]=0
    cnt[i] += 1
print(cnt)

