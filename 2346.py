from collections import deque

n = int(input())
arr = list(map(int, input().split()))
arr = [(arr[i], i) for i in range(n)]

arr = deque(arr)
while n > 0:
    print(arr[0][1] + 1, end=" ")
    step = arr[0][0]
    arr.popleft()
    if step > 0:
        for i in range(step - 1):
            if arr:
                temp = arr.popleft()
                arr.append(temp)
    else:
        for i in range(-1 * step):
            if arr:
                temp = arr.pop()
                arr.appendleft(temp)
    n -= 1
