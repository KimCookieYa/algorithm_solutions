def check_day(today, prev, s):
    today = today.split(".")
    year1 = int(today[0])
    month1 = int(today[1])
    day1 = int(today[2])

    prev = prev.split(".")
    year2 = int(prev[0])
    month2 = int(prev[1])
    day2 = int(prev[2])

    result1 = year1 * 12 * 28 + month1 * 28 + day1
    result2 = year2 * 12 * 28 + month2 * 28 + day2

    return True if result1 >= result2 + s * 28 else False


def solution(today, terms, privacies):
    answer = []

    db = dict()
    for term in terms:
        k, v = term.split()
        db[k] = int(v)

    info_db = []
    for privacie in privacies:
        k, v = privacie.split()
        info_db.append((k, v))

    for idx, info in enumerate(info_db):
        if check_day(today, info[0], db[info[1]]):
            answer.append(idx + 1)

    return answer
