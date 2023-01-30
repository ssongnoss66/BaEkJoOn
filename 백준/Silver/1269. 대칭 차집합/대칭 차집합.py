a, b = map(int, input().split())

aSt = set(map(int, input().split()))
bSt = set(map(int, input().split()))

print((len(aSt - bSt))+(len(bSt - aSt)))