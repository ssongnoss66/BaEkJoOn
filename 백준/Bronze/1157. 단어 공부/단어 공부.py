strng = input().upper()
mxCnt = 0
mxWrd = ""
for i in set(strng):
    num = strng.count(i)
    if num > mxCnt:
        mxCnt = num
        mxWrd = i
    elif num == mxCnt:
        mxCnt = num
        mxWrd = "?"
    else:
        continue

print(mxWrd)