class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ']':'[',
            ')':'(',
            '}':'{',
        }

        stack = []

        for bracket in s:
            if bracket in parentheses and stack:
                if parentheses[bracket] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(bracket)
        if stack:
            return False
        return True