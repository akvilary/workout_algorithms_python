"""
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: text = "()"
Output: true

Example 2:

Input: text = "()[]{}"
Output: true

Example 3:

Input: text = "(]"
Output: false
 
Constraints:
    1 <= text.length <= 104
    text consists of parentheses only '()[]{}'.
"""

def is_valid(text: str) -> bool:
    """Is text with valid parentheses"""
    close_mapping = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    # fast check
    if text[0] in close_mapping:
        return False

    # detailed check
    stack = []
    for char in text:
        closing = close_mapping.get(char, None)
        if closing is None:
            stack.append(char)
        elif not stack or closing != stack.pop():
            return False

    return not stack
