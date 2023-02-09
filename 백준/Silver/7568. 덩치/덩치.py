dcLi = []
num = int(input())

for i in range(num):
    dcLi.append(list(map(int, input().split())))

# print(dcLi)
# [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]

j = 0
prntLi = [0 for _ in range(num)]

while True:
    if j == num:
        break
    cnt = 0
    for k in range(num):
        if j == k:
            pass
        elif dcLi[j][0] < dcLi[k][0] and dcLi[j][1] < dcLi[k][1]:
            cnt += 1
    prntLi[j] = cnt + 1
    # print(f"j {j} prntLi {prntLi}")
    j += 1

print(*prntLi)