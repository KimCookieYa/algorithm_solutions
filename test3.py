import sys

N, K = map(int, sys.stdin.readline().split())
num = list(map(int,input()))
stack = []
def findMax():
    for i in range(N):
        print(i, 'stack', stack)
        while K > i-len(stack) and len(stack) > 0:
            if stack[-1] < num[i]:
                stack.pop()
            else:
                break
        stack.append(num[i])
        

    result=''
    for i in range(N-K):
        result += str(stack[i]) 
    return result

print(findMax())