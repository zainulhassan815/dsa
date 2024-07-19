from typing import List


def find_second_largest(nums: List[int]) -> int:
    return sorted(nums, reverse=True)[1]


test_cases = [
    [12, 35, 1, 10, 34, 1],
    [10, 5, 17]
]

for case in test_cases:
    print(f'Input: {case}')
    print(f'Output: {find_second_largest(case)}')
