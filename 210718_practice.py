#! /usr/bin/env python

# 121번
# i = input("문자를 하나 입력하세요: ")
# m = list()

# for l in i:
#     if l.islower():
#         l = l.upper()
#     else:
#         l = l.lower()
#     m.append(l)
# result = "".join(m)
# print(result)


# 122
# score = input("점수를 입력하세요: ")
# score = int(score)
# if 81 <= score <= 100:
#     Grade = "A"
# elif 61 <= score <= 80:
#     Grade = "B"
# elif 41 <= score <= 60:
#     Grade = "C"
# elif 21 <= score <= 40:
#     Grade = "D"
# elif 0 <= score <= 20:
#     Grade = "E"

# print("Your grade is ", Grade)

# # 123
# i = input("금액(공백)단위 : ")
# change = {"달러": 1167, "엔": 10.96, "유로": 1268, "위안": 171}
# num, currency = i.split()
# print(float(num) * change[currency], "원")

# # 124
# i1 = int(input("첫번째 숫자: "))
# i2 = int(input("두번째 숫자: "))
# i3 = int(input("세번째 숫자: "))
# print(max(i1, i2, i3))

# 125
# n = input("휴대폰 번호를 입력하세요(XXX-XXXX-XXXX): ")
# tel_dict = {"011": "SKT", "016": "KT", "019": "LGU", "010": "알수없음"}
# print(f"당신의 통신사는 {tel_dict[n[0:3]]}입니다.")

# # 126
# i = input("우편번호를 입력하세요: ")
# i_dict = {
#     "010": "강북구",
#     "011": "강북구",
#     "012": "강북구",
#     "013": "도봉구",
#     "015": "도봉구",
#     "016": "노원구",
#     "017": "노원구",
#     "018": "노원구",
#     "019": "노원구",
# }
# print(i_dict[i[0:3]])

# # 127
# i = input("주민등록번호(xxxxxx-xxxxxxx): ")
# if i[7] == "1" or i[7] == "3":
#     print("남자")
# elif i[7] == "2" or i[7] == "4":
#     print("여자")
# else:
#     print("주민등록 번호를 잘못 입력하셨습니다.")

# 128
# i = input("주민등록번호(xxxxxx-xxxxxxx): ")
# i = i.split("-")[1]
# if 0 <= int(i[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

# 129
# i = input("주민등록번호(xxxxxx-xxxxxxx): ")
# i = "-".join(i)
# i = i.replace("-", "")
# n = (
#     int(i[0]) * 2
#     + int(i[1]) * 3
#     + int(i[2]) * 4
#     + int(i[3]) * 5
#     + int(i[4]) * 6
#     + int(i[5]) * 7
#     + int(i[6]) * 8
#     + int(i[7]) * 9
#     + int(i[8]) * 2
#     + int(i[9]) * 3
#     + int(i[10]) * 4
#     + int(i[11]) * 5
# )
# j = n % 11
# k = (11 - j) % 10
# if k == int(i[12]):
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")


# 130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'])
# #엥? 이건 무조건 상승장 기원하고 만든 문제인가 문제가 이상하네

# 131~138 pass
# 139
# I = ["++++", 10, 20, 30]
# for i in I:
#     print(i)
# print("++++")
# 140 pass

# 141
# l = [100, 200, 300]
# for i in l:
#     print(i + 10)

# 142
# menu = ["김밥", "라면", "튀김"]
# for i in menu:
#     print("오늘의 메뉴: ", i)

# 143
# l = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in l:
#     print(len(i))


# 144, 145
# l = ["dog", "cat", "parrot"]
# for i in l:
#     print(i, len(i))

# for i in l:
#     print(i[0])

# 146
# l = [1, 2, 3]
# for i in l:
#     print("3 x", i)

# 147
# l = [1, 2, 3]
# for i in l:
#     print(f"3 x {i} =", 3 * i)

# 148
# l = ["가", "나", "다", "라"]
# for i in l:
#     if i == "가":
#         pass
#     else:
#         print(i)

# 149
# l = ["가", "나", "다", "라"]
# for i in l:
#     if i == "나" or i == "라":
#         pass
#     else:
#         print(i)

# 150
# l = ["가", "나", "다", "라"]
# l = l[::-1]
# for i in l:
#     print(i)
