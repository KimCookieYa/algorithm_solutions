a, b = map(int, input().split())
t = int(input())

scissors = [[0, b], [0, a]]
while t > 0:
    i, n = map(int, input().split())
    scissors[i].append(n)
    t -= 1

scissors[0].sort()
scissors[1].sort()

dif_y = [scissors[0][i+1] - scissors[0][i] for i in range(len(scissors[0])-1)]
dif_x = [scissors[1][i+1] - scissors[1][i] for i in range(len(scissors[1])-1)]

print(max(dif_x) * max(dif_y))