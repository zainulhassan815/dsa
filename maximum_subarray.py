# https://leetcode.com/problems/maximum-subarray/description/
# 53. Maximum SubArray
import math
from typing import List


def max_sub_array(nums: List[int]) -> int:
    max_sum = -math.inf
    current_max = max_sum

    for n in nums:
        current_max = max(current_max + n, n)
        max_sum = max(max_sum, current_max)

    return max_sum
