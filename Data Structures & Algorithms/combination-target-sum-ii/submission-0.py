class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start, cur, total):
            if total == target:
                result.append(cur[:])
                return
            
            if total > target:
                return
            
            for i in range(start, len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                
                cur.append(nums[i])
                backtrack(i+1, cur, total+nums[i])
                cur.pop()
        backtrack(0, [], 0)
        return result