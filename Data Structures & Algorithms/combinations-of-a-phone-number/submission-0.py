class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        res = []

        if not digits:
            return []

        # digits = "34"
        # outputs : 'dg', 'dh'....
        def dfs(i, cur):
            # make sure dg length == 2 == len(digits)
            if i == len(digits):
                res.append(cur[:])
                return
            
            for letter in digits_to_letters[digits[i]]:
                dfs(i+1, cur+letter)
        
        dfs(0, "")
        return res
                