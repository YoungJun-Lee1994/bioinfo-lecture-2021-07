"""
with open("title.txt") as handle:
    for line in handle:
        print(line)
"""

f = open("title.txt", "r")
for line in f:
    line = line.strip()
    break
f.close()
print("The first line is : ", line)
