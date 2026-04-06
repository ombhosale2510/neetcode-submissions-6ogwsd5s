class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        same as subsets 1, just need to handle duplicates, 
        only 2 things to keep in mind
            1. sort to group duplicates,
            2. use check inside for loop, nums[i] == nums[i-1] and continue 
        
        whole code is worse case time complexity anyways, 
        so sorting isnt gonna do anything
        """

        nums.sort()
        result = []

        def backtrack(start, cur):
            result.append(cur[:])

            for i in range(start, len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()

        backtrack(0, [])
        return result