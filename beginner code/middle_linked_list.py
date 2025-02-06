'''
Link to the challenge: https://leetcode.com/problems/middle-of-the-linked-list/description/
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:        
    def middleNode(self, head: ListNode) -> ListNode:
        # Ensure Node.val is between 1 and 100
        while True:
            if (1 <= head.val <= 100):
                break

        middle = end = head
        count = 1

        while end and end.next:
            middle = middle.next
            end = end.next.next
            count = count + 2
        
        if end is None:
            count = count - 1

        # Ensure the number of nodes is between 1 and 100
        while True:
            if (1 <= count <= 100):
                break

        return middle