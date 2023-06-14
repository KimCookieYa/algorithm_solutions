formula = input().strip() + '+'
num = 0
i = 0
answers = []
is_minus = 1
for i in range(len(formula)):
    
    if formula[i].isdigit():
        num = 10*num + int(formula[i])
    else:
        answers.append(num * is_minus)
        num = 0
        if formula[i] == '-':
            is_minus = -1
            
    i += 1
print(sum(answers))