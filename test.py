n, t, p = map(int, input().split())
shirts = list(map(int, input().split()))
pants = list(map(int, input().split()))

shirts.sort()
pants.sort()

answer = 0
j = 0

for shirt in shirts:


print(min(answer, n))