"""1225 이상한 곱셈 / 수학 구현 문자열 / https://www.acmicpc.net/problem/1225"""

# internetVer

import sys

a, b = map(list, sys.stdin.readline().split())
a = list(map(int, a))
b = list(map(int, b))
print(sum(a) * sum(b))

"""시간초과...
import sys
inpt = sys.stdin.readline

a, b = map(str, inpt().split())
hap = 0
strt = 0

while True:
    if strt > (len(b) - 1):
        print(hap)
        break
    for i in a:
        hap += int(i)*int(b[strt])
    strt += 1
"""