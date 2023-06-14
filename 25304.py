import sys

input = sys.stdin.readline

x = int(input())
n = int(input())
info = [list(map(int, input().split())) for __ in range(n)]

result = 0
for item in info:
    result += item[0] * item[1]

if x == result:
    print("Yes")
else:
    print("No")
