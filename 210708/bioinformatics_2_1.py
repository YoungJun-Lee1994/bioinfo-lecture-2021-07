i = int(input("Which times table : "))

if 1 <= i <= 9:
    for n in range(1, 10, 1):
        print(f"{i} * {n} = ", i * n)

else:
    print("What?")
