class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)
        
        freq = [[] for i in range(len(nums)+1)] # freq could be the entire list num

        # fill the buckets
        for num, f in counter.items():
            freq[f].append(num)
        
        result = []
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result