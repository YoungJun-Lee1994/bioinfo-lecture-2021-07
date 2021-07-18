f1 = open("sequence_protein.fasta", "r")

seq_list = list()
for line in f1:
    line = line.strip()
    if line == "":
        continue
    seq_list.append(line)
f1.close()

seq = "\n".join(seq_list)
f2 = open("sequence_protein_2.fasta", "w")
f2.write("%s\n" % (seq))
f2.close()

