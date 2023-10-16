import sys

input = sys.stdin.readline

s = []

m = int(input())
for i in range(m):
    op = input().split()

    if op[0] == "add" and int(op[1]) not in s:
        s.append(int(op[1]))
    elif op[0] == "remove" and int(op[1]) in s:
        s.remove(int(op[1]))
    elif op[0] == "check":
        if int(op[1]) in s:
            print("1")
        else:
            print("0")
    elif op[0] == "toggle":
        if int(op[1]) in s:
            s.remove(int(op[1]))
        else:
            s.append(int(op[1]))
    elif op[0] == "all":
        s = [i for i in range(1, 21)]
    elif op[0] == "empty":
        s = []
