ppap = input()
n = len(ppap)

state = False
stack = []
for i in range(n):
    if ppap[i] == 'P':
        if not state:
            stack.append('P')
        else:
            stack.pop()
            stack.pop()
            stack.pop()
            state = False
            stack.append('P')
    elif ppap[i] == 'A':
        stack.append('A')
        if stack[-3:] == ['P', 'P', 'A']:
            state = True

if len(stack) == 1 and stack[0] == 'P':
    print("PPAP")
else:
    print("NP")