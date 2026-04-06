class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        for i in hashmap:
            if hashmap[i]>1: 
                return True
        return False