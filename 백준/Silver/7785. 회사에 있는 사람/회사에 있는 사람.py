s=set()
_,*l=open(0)
for c in l:
    n,a=c.split()
    if a[0]=='e':s.add(n)
    else:s.remove(n)
print(*sorted(s)[::-1],sep='\n')