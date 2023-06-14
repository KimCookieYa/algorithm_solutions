import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for __ in range(n)]
ropes.sort(reverse=True)

answer = 0
for i, rope in enumerate(ropes):
    answer = max(answer, (i+1)*rope)
print(answer)