problem = input()

stack = []
answer = 0
try:
    for c in problem:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            result = 0
            while True:
                temp = stack.pop()
                if temp == '(':
                    break
                else:
                    result += int(temp)
            
            if result == 0:
                result = 2
            else:
                result *= 2
            
            if stack:
                if stack[-1].isdigit():
                    result += int(stack.pop())
            stack.append(str(result))
        elif c == ']':
            result = 0
            while True:
                temp = stack.pop()
                if temp == '[':
                    break
                else:
                    result += int(temp)
            
            if result == 0:
                result = 3
            else:
                result *= 3
            
            if stack:
                if stack[-1].isdigit():
                    result += int(stack.pop())
            stack.append(str(result))
    
    if len(stack) == 1:
        print(int(stack.pop()))
    else:
        print(0)
except:
    print(0)

