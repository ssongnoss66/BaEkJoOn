"""2941 크로아티아 알파벳"""

# my ver

wordInput = input()
word = wordInput
cnt = 0
cntLi = []

for i in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    cnt += word.count(i)
    wordNew = word.replace(i, ".")
    word = wordNew
    
print(cnt+len(word.replace(".", "")))

# teammate ver

wordInput = input()
word = wordInput
cnt = 0
cntLi = []

for i in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    cnt += wordInput.count(i)
    
print(len(wordInput) - cnt)

# teammate ver

wordInput = input()
word = wordInput
cnt = 0
cntLi = []

croat = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for i in croat:
    word = word.replace(i,"#")
print(len(word))