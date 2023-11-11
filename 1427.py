n = input().strip()
arr = [int(i) for i in n]
arr.sort(key=lambda x: -x)
for a in arr:
    print(a, end="")
