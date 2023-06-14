n, s = map(int, input().split())
a = list(map(int, input().split()))

temp = [0]
answer = 0
for item in a:
    buff = []
    for t in temp:
        buff.append(t)
        buff.append(t + item)
        if t + item == s:
            answer += 1
    
    temp = buff
    del buff

print(answer)