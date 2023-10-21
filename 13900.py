n = int(input())
arr = list(map(int, input().split()))

answer = 0
sum_nums = sum(arr)
for a in arr:
    sum_nums -= a
    answer += sum_nums * a

print(answer)
