word = input()
cnt = 0
cntLi = []
for i in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    cnt += word.count(i)
    wordNew = word.replace(i, ".")
    word = wordNew
    
print(cnt+len(word.replace(".", "")))