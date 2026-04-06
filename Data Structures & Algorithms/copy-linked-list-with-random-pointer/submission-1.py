"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        how do we copy random pointer if it connects to a node at the end
        since we are going iteratively, we cant say random.next = 5th node
        if 5th node hasnt been made yet

        thus 2 passes
        1st pass: hashmap for all nodes
        2nd pass: pointer connecting next and random
        """

        curr = head
        hashmap = {}

        while curr:
            hashmap[curr] = Node(curr.val)
            curr=curr.next

        # restart curr for second pass
        curr = head
        while curr:
            hashmap[curr].next = hashmap[curr.next] if curr.next else None        
            hashmap[curr].random = hashmap[curr.random] if curr.random else None        
            curr = curr.next
        return hashmap[head] if head else None