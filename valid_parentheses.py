# https://leetcode.com/problems/valid-parentheses/description/
# 20. Valid Parentheses

def is_valid(s: str) -> bool:
    braces = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    stack = []

    for ch in s:
        if ch in braces:
            stack.append(ch)
        elif len(stack) == 0:
            return False
        else:
            if braces[stack.pop()] != ch:
                return False

    return len(stack) == 0


test_case = ["()", "()[]{}", "(]"]
for case in test_case:
    print(f'Input: {case}')
    print(f'Output: Valid = {is_valid(case)}')
