# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hashset O(n) space
        # visited = set()

        # while head:
        #     if head in visited:
        #         return True
        #     visited.add(head)
        #     head = head.next
        # return False

        # slow fast pointer
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # 2 steps ahead
            
            if slow == fast:
                return True
        return False