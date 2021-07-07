#! /usr/bin/env python
class ValueCalculator:
    def __init__(self, val:str):
        self.val = val
    def __add__(self, other):
        return self.val + other.val
#10번 라인 추가한거는 파이썬 인터프리터 실행될 때만 실행되게 만들어주는 구문
if __name__ == "__main__":
    print('Hi~')

