from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    temp = min(users)[0]
    if temp % 10 > 0:
        temp = (temp // 10 + 1) * 10

    n = len(emoticons)
    lsts = list(product(list(range(temp, 50, 10)), repeat=n))

    for lst in lsts:
        answer_temp = [0, 0]
        for flag, limit in users:
            result = 0
            for i in range(n):
                if lst[i] >= flag:
                    result += (emoticons[i] * (100 - lst[i])) // 100
            if result >= limit:
                answer_temp[0] += 1
            else:
                answer_temp[1] += result

        if answer[0] < answer_temp[0] or (
            answer[0] == answer_temp[0] and answer[1] < answer_temp[1]
        ):
            answer = answer_temp[:]
    return answer
