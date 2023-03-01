# 문자열 재정렬 p.322

"""
(입력예시)
K1KA5CB7

(출력)
ABCKK13
"""

import re

N = input()

alphabetArr = sorted(re.findall(r'[^0-9]', N))
numberArr = list(map(int, re.findall(r'[0-9]', N)))

print(''.join(alphabetArr)+str(sum(numberArr)))

