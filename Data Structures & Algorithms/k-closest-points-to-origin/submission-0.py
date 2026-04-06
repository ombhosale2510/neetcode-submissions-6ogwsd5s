class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
            minHeap of distances
            minHeap = [dist, x, y]

            after k heappops:
                result.append(x,y)
            return x,y

        """

        minHeap = []

        for x, y in points:
            distance = math.sqrt(x**2+y**2)

            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)

        result = []

        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            result.append([x,y])
        return result
