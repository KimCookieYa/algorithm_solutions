n = int(input())
heap = []
for i in range(1, n+1):
    last_child = len(heap)
    heap.append(i)
    heap[last_child-1], heap[last_child] = heap[last_child], heap[last_child-1]
    
    child = last_child-1
    temp = heap[child] # n의 값
    while child >= 0:
        parent = (child-1)//2
        heap[child] = heap[parent]
        child = parent
    heap[0] = temp

for i in range(n):
    print(heap[i], end=' ')