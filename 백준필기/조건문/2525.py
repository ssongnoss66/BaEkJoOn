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


"""
조건 케이스별로 짜기의 중요성...
괄호 좀 제대로 쳐야됨...
사실 딱히 기록해둘건없이 노가다했지만...

너무 오래걸려서 기록해두고 싶음 어쩔노동
"""