c = int(input())
while c > 0:
    n = list(map(int, input().split()))
    score = n[1:]
    n = n[0]
    
    avg_score = sum(score) // len(score)
    print("{:.3f}%".format(100 * len(list(filter(lambda x: x > avg_score, score))) / n))
    
    c -= 1