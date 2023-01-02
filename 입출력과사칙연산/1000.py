# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)

# int 함수는 리스트를 정수형으로 바꿀 수 X
# map 함수 활용 ; map(적용할 함수, 반복 가능한 자료형)
# 모든 자료형 각각에 함수 적용 가능
# 이 문제의 경우에는 input().split()했을 때 생기는 (a, b)의 자료형에
# int 함수를 적용