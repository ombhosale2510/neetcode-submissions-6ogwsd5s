class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1. open == close == n: result.append
        2. only add open bracket if open < n
        3. only add close bracket if close < n

        """
        result = []
        stack = []

        def backtrack(openB, closeB):
            if openB == closeB == n:
                result.append("".join(stack))
                return
            
            if openB < n:
                stack.append('(')
                backtrack(openB+1, closeB)
                stack.pop()

            if closeB < openB:
                stack.append(')')
                backtrack(openB, closeB+1)
                stack.pop()
        backtrack(0,0)
        return result