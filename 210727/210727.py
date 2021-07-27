#! /usr/bin/env python

# 181
# apart = [["101호" , "102호"],["201호", "202호"] ["301호", "302호"]]

# 182
# stock = [["시가",100,200,300],["종가",80,210,330]]

# 183
stock = {"시가": [100, 200, 300], "종가": [80, 210, 330]}

# 184
stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}

# 185
apart = [[101, 102], [201, 202], [301, 302]]
# for i in range(3):
#     for j in range(2):
#         print(f"{apart[i][j]}호")
# #풀이는 이렇게 했더라 row, col 이용
# for row in apart:
#     for col in row:
#         print(col, "호")

# 186
# for i in apart[::-1]:
#     for j in range(2):
#         print(f"{i[j]}호")

# 187
# for i in apart[::-1]:
#     for j in i[::-1]:
#         print(f"{j}호")

# 188
# for i in apart:
#     for j in i:
#         print(f"{j}호")
#         print("-----")

# 189
# for i in apart:
#     for j in i:
#         print(f"{j}호")
#     print("-" * 5)

# 190
# for i in apart:
#     for j in i:
#         print(f"{j}호")
# print("-" * 5)
