import gzip
#나 이거 왜 안되냐
file_name = "covid19.fasta.gz"

data = dict() # data = {}
#data = {"A":0, "G":0, "C":0, "T":0}
"""
#with open(file_name, 'r') as handle:  #텍스트로 하고 싶으면 'rt'로 하던가 'rb'로 하고 밑에 if line말고 line = line.decode("utf-8") 쓰면 된다.
"""
with open(file_name, 'rt') as handle:  
    for line in handle:
        if line.startswith(">"):  #">" 로 시작을 하면 넘어가게 했다.
            continue
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1

print(data)



