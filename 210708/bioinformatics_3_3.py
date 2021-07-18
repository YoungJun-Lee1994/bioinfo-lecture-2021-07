# with open("sequence_protein.fasta") as handle:
#     for line in handle:
#         print(line.strip())

fr = open("sequence_protein.fasta")
for line in fr:
    line = line.strip()
    print(line)
    # if line == "":
    #     continue

fr.close()
