import sys

input = sys.stdin.readline

while True:
    n = input().strip()
    if n == "0":
        break

    l = len(n)
    for i in range(l // 2):
        if n[i] != n[l - i - 1]:
            print("no")
            break
    else:
        print("yes")
