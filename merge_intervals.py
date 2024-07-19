# https://leetcode.com/problems/merge-intervals
# 56. Merge Intervals

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) < 1:
        return intervals

    intervals.sort(key=lambda i: i[0])

    i = 0
    output = []

    while i <= (len(intervals) - 1):
        temp = intervals[i]
        count = 0
        for j in range(i + 1, len(intervals)):
            if temp[1] >= intervals[j][0]:
                if temp[1] > intervals[j][1]:
                    count += 1
                else:
                    count += 1
                    temp[1] = intervals[j][1]
            else:
                break

        i += count + 1
        output.append(temp)

    return output


def merge_v2(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])

    output = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = output[-1][1]

        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])

    return output


test_cases = [
    [[1, 3], [2, 6], [8, 10], [15, 18]],
    [[1, 4], [4, 5]],
    [[1, 4], [2, 3]]
]

print('-- Merge V1 --')
for case in test_cases:
    print(f'Input: {case}')
    print(f'Output: {merge(case)}')

print('-- Merge V2 --')
for case in test_cases:
    print(f'Input: {case}')
    print(f'Output: {merge_v2(case)}')