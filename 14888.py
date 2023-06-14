import sys
input = sys.stdin.readline

n = int(input())
progressions = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))
op_list = ['+', '-', '*', '//']
max_val = -1e9
min_val = 1e9

def dfs(num_idx, op_cnt, result):
    global max_val, min_val
    
    if num_idx == n:
        if max_val < result:
            max_val = result
        if min_val > result:
            min_val = result
        return
    
    new_op_cnt = op_cnt.copy()
    
    for i in range(4):
        if new_op_cnt[i] > 0:
            new_op_cnt[i] -= 1
            if result < 0 and i == 3:
                result = -result
                new_result = eval(str(result) + op_list[i] + str(progressions[num_idx]))
                new_result = -new_result
            else:
                new_result = eval(str(result) + op_list[i] + str(progressions[num_idx]))
            dfs(num_idx+1, new_op_cnt, new_result)
            new_op_cnt[i] += 1
            
dfs(1, op_cnt, progressions[0])
print(max_val)
print(min_val)