a = int(input())
b = c = int(input())
while b > 0:
    print(a*(b%10))
    b = b//10
print(a*c)