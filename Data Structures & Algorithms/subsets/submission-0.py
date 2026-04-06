class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(cur, start):
            result.append(cur[:])

            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(cur, i+1)
                cur.pop()

        backtrack([], 0)

        return result