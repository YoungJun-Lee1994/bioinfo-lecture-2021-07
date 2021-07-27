#! /usr/bin/env python

# 181
# apart = [["101호" , "102호"],["201호", "202호"] ["301호", "302호"]]

# 182
# stock = [["시가",100,200,300],["종가",80,210,330]]

# # 183
# stock = {"시가": [100, 200, 300], "종가": [80, 210, 330]}

# # 184
# stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}

# # 185
# apart = [[101, 102], [201, 202], [301, 302]]
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

# 191
data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [15450, 15050, 15550, 14900],
]
# for i in data:
#     for j in i:
#         print(j * 1.00014)

# 192
# for i in data:
#     for j in i:
#         print(j * 1.00014)
#     print("-" * 4)

# 193
# result = []
# for i in data:
#     for j in i:
#         result.append(j * 1.00014)
# print(result)

# 194
# result = []
# for i in data:
#     r1 = []
#     for j in i:
#         r1.append(j * 1.00014)
#     result.append(r1)
# print(result)

# 풀이에는 이렇게 되어있음
# for line in data:
#     sub = []
#     for column in line:
#         sub.append(column * 1.00014)
#     result.append(sub)
# print(result)

# 195
ohlc = [
    ["open", "high", "low", "close"],
    [100, 110, 70, 100],
    [200, 210, 180, 190],
    [300, 310, 300, 310],
]

# for i in ohlc[1:]:
#     print(i[3])

# 196
# for i in ohlc[1:]:
#     if i[3] >= 150:
#         print(i[3])

# 197
# for i in ohlc[1:]:
#     if i[3] >= i[0]:
#         print(i[3])

# 198
# volatility = []
# for i in ohlc[1:]:
#     volatility.append(i[1] - i[2])
# print(volatility)

# 199
# for i in ohlc[1:]:
#     if i[3] > i[0]:
#         print(i[1] - i[2])

# 200
# l = 0
# for i in ohlc[1:]:
#     l += i[3] - i[0]
# print(l)

# 201
def print_coin():
    print("비트코인")


# 202
print_coin()

# 203
for i in range(100):
    print_coin()

# 204
def print_coin():
    for i in range(100):
        print("비트코인")


# 205~210 pass
