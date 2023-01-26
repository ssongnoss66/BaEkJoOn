"""
1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
"""

num = int(input())

for i in range(0, num+1):
    i = 2 ** i
    print(i, end=" ")

# n ** m ; n의 m승