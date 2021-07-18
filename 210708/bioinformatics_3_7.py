# 이거 선생님 빠르게 하셔서 못풀고 들음.
# 나중에 스크립트 얻어라
seq_list = []
with open("sequence_protein_2.fasta", "r") as handle:
    title = handle.readline()
    for line in handle:
        line = line.strip()
        if line[0] != ">":
            seq_list.append(line)
    seq = "".join(seq_list)

while True:
    p = input("position: ")
    if p == "XXX":
        print("Okay, I will stop")
        break
    else:
        aa = int(p)
        ppp = seq[aa - 1 : aa + 2]
    print("Three amino acid: ", ppp)
