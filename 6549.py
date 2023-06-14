import sys
input = sys.stdin.readline

def solution(a, stack):
    if len(stack) == 1:
        return stack[0]
    
    return max(a[stack[0]] * len(stack), solution(a, stack[1:]))

while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    
    n = a[0]
    a = a[1:]
    
    answer = a[0]
    stack = [0]
    for i in range(1, n):
        if a[stack[-1]] > a[i]:
            answer = max(answer, solution(a, stack), (i-stack[-1]+1)*a[i])
            del stack
            stack = [i]
        else:
            stack.append(i)
            answer = max(answer, solution(a, stack))
    
    a.reverse()
    stack = [0]
    for i in range(1, n):
        if a[stack[-1]] > a[i]:
            answer = max(answer, solution(a, stack), (i-stack[-1]+1)*a[i])
            del stack
            stack = [i]
        else:
            stack.append(i)
            answer = max(answer, solution(a, stack))
    
    print(answer)