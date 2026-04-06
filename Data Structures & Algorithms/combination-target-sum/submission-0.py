class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums: [2,5,6,9]
        # target = 9
        
        res = []
        n = len(nums)

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i>=n or total > target:
                return
            
            cur.append(nums[i])
            dfs(i,cur,total+nums[i])
            cur.pop()

            dfs(i+1, cur, total)
        
        dfs(0,[], 0)
        return res