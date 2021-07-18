s1 = input("s1: ")
s2 = input("s2: ")

l1 = len(s1)
l2 = len(s2)

if l1 % 2 == 1 and l1 < l2:
    print(s1 + s2)
else:
    print(s2 + s1)

