hourNow, minNow = map(int, input().split())
minCook = int(input())

if minNow + minCook > 60:
    if hourNow + ((minNow + minCook)//60) > 23:
        print(((hourNow + ((minNow + minCook)//60))%24), ((minNow + minCook)%60))
    elif hourNow + ((minNow + minCook)//60) <= 23:
        print((hourNow + ((minNow + minCook)//60)), ((minNow + minCook)%60))
elif  minNow + minCook == 60:
    if hourNow + ((minNow + minCook)//60) > 23:
        print(0, 0)
    elif hourNow + ((minNow + minCook)//60) <= 23:
        print((hourNow + ((minNow + minCook)//60)), 0)
elif minNow + minCook < 60:
    print(hourNow, (minNow + minCook))