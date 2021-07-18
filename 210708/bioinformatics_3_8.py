seq_list = []
with open("sequence_protein_2.fasta", "r") as handle:
    title = handle.readline()
    for line in handle:
        line = line.strip()
        if line[0] != ">":
            seq_list.append(line)
    seq = "".join(seq_list)

while True:
    Loc = input("Searching for: ")
    if Loc == "XXX":
        print("Okay, I will stop")
        break
    else:
        ll = list()
        i = 1
        for c in seq:
            if c == Loc:
                ll.append(str(i))  # join에 넣고 돌릴 때는 str이어야 한다.
            i += 1
        print("Found at: ", (",".join(ll)))
