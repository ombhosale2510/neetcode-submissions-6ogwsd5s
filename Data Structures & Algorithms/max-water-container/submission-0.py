class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force will result in TLE

        left, right = 0 , len(heights)-1

        result = 0
        while left<right:
            # calculate area
            area = (right-left) * min(heights[left], heights[right])

            result = max(result, area)

            # condition to move
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return result