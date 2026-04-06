class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        BF - O(n2)
        [3,4,5,6,1,2]

        check which side is sorted,
        check if it can hold target in terms of range, 
        4<target<8  if target==0? then this cannot happen


        """

        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            
            # check which direction is sorted
            if nums[left]<=nums[mid]:
                # left is sorted
                if nums[left] <= target <nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left= mid+1
                else:
                    right = mid-1
        return -1