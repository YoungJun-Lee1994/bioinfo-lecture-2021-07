# fr = open("sequence.protein.gb", "r")
# 1. 실패
# title = fr.readline()
# seq = ""
# seq_list = list()

# for line in fr:
#     line = line.strip()
#     if line == "":
#         pass
#     if line[1].isalpha():
#         seq_list.append(line)
# fr.close()

# seq = "\t".join(seq_list)
# print(title)
# print(seq)

# 2.
seq = list()
a = False
with open("sequence.protein.gb", "r") as handle:
    title = handle.readline()
    print(title)
    for line in handle:
        line = line.strip()

        if line.startswith("ORIGIN"):
            a = True
        if a:
            seq.append(line)

seq = "\n".join(seq)
print(seq)
