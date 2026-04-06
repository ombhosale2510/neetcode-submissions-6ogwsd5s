class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        result = []
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])
        return result