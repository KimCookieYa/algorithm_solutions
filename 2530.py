start_time = list(map(int, input().split()))
jobs = int(input())

start_time[2] += jobs % 60
jobs = jobs // 60
if start_time[2] >= 60:
    start_time[2] -= 60
    start_time[1] += 1
start_time[1] += jobs % 60
jobs = jobs // 60
if start_time[1] >= 60:
    start_time[1] -= 60
    start_time[0] += 1
start_time[0] += jobs % 24
if start_time[0] >= 24:
    start_time[0] -= 24
print(start_time[0], start_time[1], start_time[2])
