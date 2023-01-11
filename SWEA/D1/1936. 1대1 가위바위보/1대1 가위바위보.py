abDict = {
    (1, 2): 'B', 
    (2, 3): 'B', 
    (3, 1): 'B', 
    (2, 1): 'A', 
    (3, 2): 'A', 
    (1, 3): 'A'
}

abList = list(map(int, input().split()))
result = abDict.get(tuple(abList))
if result:
    print(result)