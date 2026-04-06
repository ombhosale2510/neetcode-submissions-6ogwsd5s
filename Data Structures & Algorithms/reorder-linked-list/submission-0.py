# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        [1,2,3,4,5]
        [1,5,2,4,3]

        1. find middle, split 2 halves
        2. reverse second half,
        3. merge two lists
        """
        # find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None # split into 2 halves
        
        prev, cur = None, second
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # prev is now at the second reversed half
        
        # merge two halves
        first, second = head, prev
        while second:
            # 1,2,3,4,5
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2