import string
alph = list(string.ascii_uppercase)

phoneDict = {}

for i in range(2, 10):
    if i < 7 or i == 8:
        phoneDict[i+1] = alph[0:3]
        alph = alph[3::]
    if i == 7:
        phoneDict[i+1] = alph[0:4]
        alph = alph[4::]
    if i == 9:
        phoneDict[i+1] = alph

def get_key(val):
    for key, value in phoneDict.items():
         if val == value:
             return key

hap = 0
wordInpt = map(str, input().strip())

for k in wordInpt:
    for j in phoneDict.values():
        if k in j:
            num = get_key(j)
            hap += num

print(hap)