file_name = "covid19.fasta"

data = dict() # data = {}
#data = {"A":0, "G":0, "C":0, "T":0}
with open(file_name, 'r') as handle:
    for line in handle:
        if line.startswith(">"):  #">" 로 시작을 하면 넘어가게 했다.
            continue
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1

print(data)



