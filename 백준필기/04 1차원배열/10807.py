"""문제
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
"""

# input.txt 파일을 생성하고,입력을 작성해주세요.
# 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.
import sys

# 이하 입력 코드

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(numbers.count(v))

# input() 대신 import sys 이후 sys.stdin.readline() 사용