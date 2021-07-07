#! /usr/bin/env python
# 앞에꺼는 클래스고 뒤에꺼는 거기 있는 함수나 밸류
from ValueCalculator import ValueCalculator

value_calculator_1 = ValueCalculator("a")
value_calculator_2 = ValueCalculator("b")

res = value_calculator_1 + value_calculator_2
print(res)
