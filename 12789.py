n = int(input())

order = list(map(int, input().split()))
stack = []
for i in range(1, n + 1):
    if len(stack) > 0 and stack[-1] == i:
        stack.pop(-1)
    elif len(order) > 0:
        while len(order) > 0 and order[0] != i:
            temp = order.pop(0)
            stack.append(temp)

        if len(order) > 0 and order[0] == i:
            order.pop(0)

if len(stack) > 0 or len(order) > 0:
    print("Sad")
else:
    print("Nice")
