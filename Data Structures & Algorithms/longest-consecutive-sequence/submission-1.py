class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2,20,4,10,3,4,5]
        set(), looking up O(n)
        output: 4

        start counting cur-1 does not exists
        longest = max(cur+1 exists)
        """

        numSet = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in numSet:
                total = 1
                while num+total in numSet:
                    total+=1
                longest = max(longest, total)
        return longest
