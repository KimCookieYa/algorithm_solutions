import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for __ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

answer = 0
end_time = -1
for i in range(len(meetings)):
    if meetings[i][0] >= end_time:
        end_time = meetings[i][1]
        answer += 1

print(answer)