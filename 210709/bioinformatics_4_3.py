seq = list()
a = False
with open("sequence.protein.gb", "r") as handle:
    title = handle.readline()
    print("Title: ", title)
    for line in handle:
        line = line.strip().split()
        for c in line:
            if c.isalpha():
                line = "".join(line)

                if line.startswith("ORIGIN"):
                    a = True
                if a:
                    if line.startswith("ORIGIN"):
                        pass
                    seq.append(line)

seq1 = "".join(seq)
print("seq: ", seq1)
