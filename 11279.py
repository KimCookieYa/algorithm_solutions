class Heapq:
    def __init__(self, n):
        self.heapq = [None] + [0] * n
        self.length = 0
    
    def print(self):
        print(self.heapq[1:self.length+1])
    
    def heapify(self, left, right):
        parent = left
        temp = self.heapq[parent]
        
        while parent < right//2+1:
            cl = parent*2
            cr = cl+1
            child = cr if cr <= right and self.heapq[cr] > self.heapq[cl] else cl
            if temp >= self.heapq[child]:
                break
            self.heapq[parent] = self.heapq[child]
            parent = child
        self.heapq[parent] = temp
    
    def heappush(self, item):
        self.length += 1
        self.heapq[self.length] = item
        
        child = self.length
        temp = self.heapq[child]
        
        while child//2 > 0:
            parent = child // 2
            if temp <= self.heapq[parent]:
                break
            self.heapq[child] = self.heapq[parent]
            child = parent
        self.heapq[child] = temp
    
    def heappop(self):
        if self.length == 0:
            return 0
        root = self.heapq[1]
        
        self.heapq[1] = self.heapq[self.length]
        self.length -= 1
        if self.length > 0:
            self.heapify(1, self.length)
        return root


import sys
input = sys.stdin.readline

answer = []
n = int(input())
hq = Heapq(100000)

for i in range(n):
    x = int(input())
    if x > 0:
        hq.heappush(x)
    else:
        root = hq.heappop()
        print(root)