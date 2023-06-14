import sys
input = sys.stdin.readline

n = int(input())
bt = [input().split() for _ in range(n)]

def visit_preorder(bt, parent):
    for i in range(n):
        if bt[i][0] == parent:
            cl = bt[i][1]
            cr = bt[i][2]
            print(parent, end='')
            if cl != '.':
                visit_preorder(bt, cl)
            if cr != '.':
                visit_preorder(bt, cr)
            break

def visit_inorder(bt, parent):
    for i in range(n):
        if bt[i][0] == parent:
            cl = bt[i][1]
            cr = bt[i][2]
            if cl != '.':
                visit_inorder(bt, cl)
            print(parent, end='')
            if cr != '.':
                visit_inorder(bt, cr)
            break

def visit_postorder(bt, parent):
    for i in range(n):
        if bt[i][0] == parent:
            cl = bt[i][1]
            cr = bt[i][2]
            if cl != '.':
                visit_postorder(bt, cl)
            if cr != '.':
                visit_postorder(bt, cr)
            print(parent, end='')
            break



visit_preorder(bt, 'A')
print('')
visit_inorder(bt, 'A')
print('')
visit_postorder(bt, 'A')