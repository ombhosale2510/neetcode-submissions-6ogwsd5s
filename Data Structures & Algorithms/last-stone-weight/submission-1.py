class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)
        while len(stones)>1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)

            heapq.heappush(stones, -abs(y-x))
        return -stones[0]
