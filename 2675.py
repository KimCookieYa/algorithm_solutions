t = int(input())

while t > 0:
    r, s = input().split()
    r = int(r)
    
    answer = "".join([c * r for c in s])
    print(answer)
                     
    t -= 1