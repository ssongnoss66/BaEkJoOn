import sys
inpt = sys.stdin.readline

mxScore = 0
mxChef = 0
for i in range(1, 6):
    hap = sum(map(int, inpt().split())) 
    if hap > mxScore:
        mxScore = hap
        mxChef = i

print(f"{mxChef} {mxScore}")