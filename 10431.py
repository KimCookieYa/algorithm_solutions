import sys

input = sys.stdin.readline

t = int(input())
for __ in range(t):
    temp = list(map(int, input().split()))
    n = temp[0]
    childs = temp[1:]

    answer = 0
    result = [-1]
    for i in range(20):
        if max(result) < childs[i]:
            result.append(childs[i])
        else:
            for j in range(len(result)):
                if result[j] > childs[i]:
                    answer += len(result[j:])
                    result = result[:j] + [childs[i]] + result[j:]
                    break

    print(n, answer)
