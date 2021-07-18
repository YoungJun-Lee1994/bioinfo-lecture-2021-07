# fr = open("sequence_protein_2.fasta", "r")
# title = ""
# seq_list = list()
# for line in fr:
#     line = line.strip()
#     if line == "":
#         continue
#     if line.startswith() != ">":
#         seq_list.append(line)
#     else:
#         title = line
# fr.close()

# seq = "".join(seq_list)
# # 나머지는 사진 봐라
seq_list = []
with open("sequence_protein_2.fasta", "r") as handle:
    title = handle.readline()
    print("title : ", title)
    for line in handle:
        line = line.strip()
        if line[0] != ">":
            seq_list.append(line)
    seq = "".join(seq_list)
    print("seq: ", seq)
