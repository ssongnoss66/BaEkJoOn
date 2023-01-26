from collections import deque

for i in range(int(input())):
    stack = []
    inpt = input()
    for j in inpt:
        if j == "(":
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")