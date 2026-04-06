class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        stack = []

        for bracket in s:
            # if closing bracket
            if bracket in parentheses:
                if stack and parentheses[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False