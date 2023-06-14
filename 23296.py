import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().strip().split()))

indegree = [0] * (n+1)
for floor in a:
    indegree[floor] += 1

answer = []
checked = [False] * (n+1)
for i in range(1, n+1):
    if checked[i]:
        continue
    
    cur = i
    while True:
        
        next = a[cur-1]
        
        indegree[next] -= 1
        if indegree[next] >= 0 and not checked[cur]:
            
            checked[cur] = True
            answer.append(next)
            cur = next
            continue
        break
print(checked)
print(len(answer))
for a in answer:
    print(a, end=' ')