a = int(input())
b = int(input())
c = int(input())

answer = [0] * 10
result = str(a*b*c)

for i in range(10):
    answer[i] = result.count(str(i))

for a in answer:
    print(a)