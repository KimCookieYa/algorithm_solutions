from collections import deque


def check(t, s):
    if s in t:
        return True
    elif s[::-1] in t:
        return True
    return False


s = input().strip()
t = input().strip()
lt = len(t)

answer = 0
queue = deque([s])
while len(queue) > 0:
    cur = queue.pop()

    if cur == t:
        answer = 1
        break
    elif len(cur) == lt:
        continue

    a = cur + "A"
    if check(t, a):
        queue.append(a[:])

    b = (cur + "B")[::-1]
    if check(t, b):
        queue.append(b[:])

print(answer)
