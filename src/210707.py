#! /usr/bin/env python

# 210707
# 오늘 할 내용 Visual Studio Code 설정
# 생물정보학 파일 다루기
# Txt, csv, tsv, json, FASTA, BAM, VCF
# 비쥬얼 스튜디오는 컴퓨터에서 작업하고 ssh에 저장 가능함.(푸티처럼 컴퓨터에서 작업하면 서버에 저장 가능함.)

# 오늘은 vscode 썼다.

# 오후 2시 50분
# 프로그래밍 과제
# 5.번부터해봐
# 059 fasta 하는거
# biopython 은 이렇게 하면 되고
# from Bio import SeqIO
# f = "./059.fasta"

# record = SeqIO.read(f, "fasta")

# 다르게
# data = dict()
# with open("059.fasta", "r") as handle:
#     for line in handle:
#         if line.startswith(">"):
#             continue
#         for base in line.strip():
#             if base not in data:
#                 data[base] = 0
#             data[base] += 1

# print(data)

# 061.fastq 받아서 세는거

# cnt = 0
# data = dict()
# with open("061.fastq", "r") as handle:
#     for line in handle:
#         if cnt % 4 == 0:  # header
#             pass
#         elif cnt % 4 == 1:  # base
#             for base in line.strip():
#                 if base not in data:
#                     data[base] = 0
#                 data[base] += 1
#         elif cnt % 4 == 2:  # delimiter
#             pass
#         elif cnt % 4 == 3:  # qual
#             pass
#         cnt += 1

# print(cnt / 4)  # 100.0
# print(data)  # {'G': 2446, 등}

# BED파일 구하는거
# result = 0
# with open("077.bed", "r") as handle:
#     for line in handle:
#         data = line.strip().split("\t")
#         # result = int(data[2]) - int(data[1])
#         chrom, start, end = data
#         length = int(end) - int(start)
#         result += length
# print(result)
# BED파일 구하는거 수정 문제
# i = int(input("n째 줄 길이 : "))
# data = dict()
# idx = 1
# with open("077.bed") as handle:
#     for line in handle:
#         chrom, start, end = line.strip().split("\t")
#         length = int(end) - int(start)
#         if chrom not in data:
#             data[chrom] = dict()
#         data[chrom][str(idx)] = length
#         idx += 1
#         if idx == i + 1:
#             print(f"{i}번째 줄 길이 = ", length)

# with open("077.bed,'r'") as handle:
#     for line in handle:
#         data = line.strip().split('\t')
#         chrom, start, end = data
#         length = int(end) - int(start)
#         print("의 길이 : ", length)


# 070 VCF 파일
# cnt = 0
# with open("070.vcf", "r") as handle:
#     for line in handle:
#         if line.startswith("#"):
#             continue
#         if line.startswith("##"):
#             continue
#         cnt += 1

# print(cnt)

# --------------------------------------
# cnt_all = 0
# cnt_pass = 0
# with open("070.vcf", "r") as handle:
#     for line in handle:
#         if line.startswith("#"):
#             continue
#         data = line.strip().split("\t")
#         cnt_all += 1
#         if data[6] == "PASS":
#             cnt_pass += 1

# print(cnt_pass, cnt_all, cnt_pass / cnt_all)

# 이 때 84번 때 라인에 FILTER가 [6]인걸 신경 안쓰고 파이썬보고 찾아서 고치라고 하고 싶을 때는
# cnt_all = 0
# cnt_pass = 0
# with open("070.vcf", "r") as handle:
#     for line in handle:
#         if line.startswith("##"):  # 여기 ##부터 거른건 #하나 에서 인덱스 설정할거기 때문에
#             continue
#         elif line.startswith("#"):
#             header = lin.strip().split("\t")
#             filter_idx = header.index("FILTER")
#             continue
#         data = line.strip().split("\t")
#         cnt_all += 1
#         if data[filter_idx] == "PASS":
#             cnt_pass += 1

# print(cnt_pass, cnt_all, cnt_pass / cnt_all)
# 슬라이드 179

# cnt_all = 0
# cnt_pass = 0
# with open("070.vcf", "r") as handle:
#     for line in handle:
#         if line.startswith("##"):  # 여기 ##부터 거른건 #하나 에서 인덱스 설정할거기 때문에
#             continue
#         elif line.startswith("#"):
#             header = lin.strip().split("\t")
#             filter_idx = header.index("FILTER")
#             continue
#         data = line.strip().split("\t")
#         cnt_all += 1
#         if data[filter_idx] == "PASS":
#             cnt_pass += 1
#
# 재귀 Recursive Programming
# 피보나치 수열
# n = int(input("Fibo(n) = "))


# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
# #              여기에 n=0,1이 아닐 때
# #              함수를 반환함
# print(fibo(n))
