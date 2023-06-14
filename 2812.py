n, k = map(int, input().split())
number = input()

stack = []
for i in range(n):
    if not stack:
        stack.append(number[i])
    else:
        top = int(stack[-1])
        cur = int(number[i])
        if k > 0:
            if n-i >= k:
                if top < cur:
                    while stack and k > 0:
                        if int(stack[-1]) >= cur:
                            break
                        stack.pop()
                        k -= 1
                    stack.append(number[i])
                else:
                    if n-i == k:
                        k -= 1
                    else:
                        stack.append(number[i])
        
        else:
            stack.append(number[i])

for s in stack:
    print(s, end='')