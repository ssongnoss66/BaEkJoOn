import sys

# 이하 입력 코드

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(numbers.count(v))