hourNow, minNow = map(int, input().split())
minCook = int(input())

if hourNow == 23 and (minNow + minCook) >= 60:
    print(0, ((minNow + minCook)%60))
else:
    print((hourNow + ((minNow + minCook)//60)), ((minNow + minCook)%60))