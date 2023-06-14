import sys
input = sys.stdin.readline

while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    
    n = a[0]
    a = a[1:]
    
    answer = a[0]
    stack = [0]
    for i in range(1, n):
        while stack and a[stack[-1]] > a[i]:
            mIdx = stack.pop()
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            answer = max(answer, width*a[mIdx])
        stack.append(i)
    
    while stack:
        mIdx = stack.pop()
        if stack:
            width = n - stack[-1] - 1
        else:
            width = n
        answer = max(answer, width*a[mIdx])
    
    print(answer)