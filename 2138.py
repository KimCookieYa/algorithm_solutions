from collections import deque
n = int(input())
s = list(input().strip())
target = list(input().strip())

def flip(idx):
    if s[idx] == '0':
        s[idx] = '1'
    else:
        s[idx] = '0'

s_list = [''.join(s)]
answer = 0
while True:
    queue = deque()
    i = 0
    while i < n:
        if s[i] != target[i]:
            queue.append(i)
        i += 1
    if len(queue) == 0:
        break
    
    while queue:
        cur = queue.popleft()
        
        for idx in [cur-1, cur, cur+1]:
            if 0 <= idx < n:
                flip(idx)
        answer += 1
    
    ss = ''.join(s)
    if ss in s_list:
        answer = -1
        break
    else:
        s_list.append(ss)

print(answer)