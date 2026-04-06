"""
    including duplicates
"""

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        

    def add(self, val: int) -> int:
        # size management: k remains constant, so we'll never 
        # need the smallest value, value > k
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        # return sm
