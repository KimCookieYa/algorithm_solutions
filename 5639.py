import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
    
def postorder(start, end):
    if start >= end:
        print(preorder[start])
        return
    root = preorder[start]

    if preorder[end] <= root or root < preorder[start+1]:
        postorder(start+1, end)
        print(root)
        return

    for i in range(start+2, end+1):
        if preorder[i] > root:
            postorder(start + 1, i-1)
            postorder(i, end)
            print(root)
            return

postorder(0, len(preorder)-1)