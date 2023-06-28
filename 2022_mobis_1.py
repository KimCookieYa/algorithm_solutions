# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

input = sys.stdin.readline

n = int(input())
cars = []
for i in range(n):
    temp = list(map(int, input().split()))
    cars.append(temp + [i + 1])
cars.sort()

car = [0, 0, 0]
answer = 0
for i in range(n):
    if cars[i][0] == car[0]:
        if cars[i][1] == car[1]:
            answer = answer - car[2] + cars[i][2]
            car = cars[i]
        elif cars[i][1] < car[1]:
            continue
        elif cars[i][1] > car[1]:
            car[1] = cars[i][1]
            answer = answer - car[2] + cars[i][2]
            car = cars[i]
    elif cars[i][0] > car[0]:
        car = cars[i]
        answer += car[2]
print(answer)
