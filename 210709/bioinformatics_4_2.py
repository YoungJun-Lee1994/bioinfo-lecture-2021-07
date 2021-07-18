# seq = list()
# a = False
# with open("sequence.protein.gb", "r") as handle:
#     title = handle.readline()
#     print("Title: ", title)
#     for line in handle:
#         line = line.strip()
#         if line == "":
#             continue
#         if line == "//":
#             continue
#         if line.startswith("ORIGIN"):
#             a = True
#         if a:
#             seq.append(line)

# seq1 = "".join(seq)
# print("seq: ", seq1)


# for i in range(len(line)):
#     if line[i].isdigit():
#         pass
#     else:


seq = list()
a = False
with open("sequence.protein.gb", "r") as handle:
    title = handle.readline()
    print(title)
    for line in handle:
        line = line.strip().split()
        line = "".join(line)
        if line == "":
            continue
        if line == "//":
            continue
        if line.startswith("ORIGIN"):
            a = True
        if line.startswith("ORIGIN"):
            continue
        if a:
            seq.append(line)
    seq = " ".join(seq)

d = list()
for i in seq:
    i = i.strip()
    if i.isdigit():
        continue
    if i == "":
        continue
    print(i)
    seq1 = "".join(i)
