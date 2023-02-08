max = 0
curr = 0

for i in range(4):
    leave, enter = map(int, input().split())
    curr = curr - leave + enter
    if curr > max:
        max = curr

print(max)