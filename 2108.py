import sys

input = sys.stdin.readline


def solution():
    temp = dict()
    for i in nums:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1

    max_v = max(temp.values())
    max_dict = []

    for i in temp:
        if max_v == temp[i]:
            max_dict.append(i)

    if len(max_dict) > 1:
        return max_dict[1]
    else:
        return max_dict[0]


n = int(input())
nums = [int(input()) for __ in range(n)]
nums.sort()

print(round(sum(nums) / n))
print(nums[n // 2])
print(solution())
print(nums[-1] - nums[0])
