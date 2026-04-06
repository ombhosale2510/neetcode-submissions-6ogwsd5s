# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1.  count if enoug nodes
        """

        dummy = ListNode(0, head)
        prevGroup = dummy
        while True:
            count = 0
            tail = prevGroup.next
            while tail and count < k:
                tail = tail.next
                count += 1
            if count < k:
                break  # not enough nodes
            
            # 2. reverse nodes
            prev = None
            cur = prevGroup.next
            nxt = cur.next
            for i in range(k):
                cur.next = prev
                prev = cur
                cur = nxt
                if nxt:
                    nxt = nxt.next
            
            # 3. group nodes
            temp = prevGroup.next
            prevGroup.next = prev
            temp.next = cur
            prevGroup = temp
        return dummy.next