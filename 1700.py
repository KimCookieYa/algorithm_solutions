n, k = map(int, input().split())
order = list(map(int, input().split()))

multitab = []
for i in range(k):
    if order[i] not in multitab:
        multitab.append(order[i])
        if len(multitab) == n:
            break
answer = 0
for i in range(n, k):
    if order[i] in multitab:
        continue
    
    max_idx = -1
    del_plug = 0
    for j in range(n):
        if multitab[j] not in order[i:]:
            del_plug = j
            break
        elif order[i:].index(multitab[j]) > max_idx:
            max_idx = order[i:].index(multitab[j])
            del_plug = j
    
    multitab[del_plug] = order[i]
    answer += 1

print(answer)