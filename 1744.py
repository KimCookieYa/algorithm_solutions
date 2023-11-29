n = int(input())

arr = [int(input()) for __ in range(n)]
arr.sort(reverse=True)
for i in range(n):
    if arr[i] <= 0:
        arr = arr[:i] + arr[i:][::-1]
        break

answer = 0
prev = 10000
for a in arr:
    if a == 0:
        if prev != 10000:
            if prev > 0:
                answer += prev
            else:
                answer += prev * a
        prev = a
    elif a > 0:
        if prev == 10000:
            prev = a
        else:
            answer += max(a * prev, a + prev)
            prev = 10000
    else:
        if prev == 10000:
            prev = a
        elif prev < 0:
            answer += max(a * prev, a + prev)
            prev = 10000
        else:
            if a * prev > a + prev:
                answer += a * prev
                prev = 10000
            else:
                answer += prev
                prev = a

if prev != 10000:
    answer += prev
print(answer)
