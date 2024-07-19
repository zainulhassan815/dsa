# https://leetcode.com/problems/sort-colors/
# 75. Sort Colors
from typing import List


def sort_colors(nums: List[int]) -> None:
    count_0, count_1, count_2 = 0, 0, 0

    for i in range(len(nums)):
        if nums[i] == 0:
            count_0 += 1
        elif nums[i] == 1:
            count_1 += 1
        else:
            count_2 += 1

    for i in range(count_0):
        nums[i] = 0

    for i in range(count_0, count_0 + count_1):
        nums[i] = 1

    for i in range(count_0 + count_1, len(nums)):
        nums[i] = 2


test_cases = [
    [2, 0, 2, 1, 1, 0],
    [2, 0, 1]
]

for case in test_cases:
    print(f'Input: {case}')
    sort_colors(case)
    print(f'Output: {case}')
