# https://leetcode.com/problems/move-zeroes/
# 283. Move Zeroes
from typing import List


def move_zeroes(nums: List[int]) -> None:
    # [0, 1, 0, 3, 12]
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
