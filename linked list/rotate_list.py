'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
Given the head of a linked list, rotate the list to the right by k places.

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
'''
class ListNode:
    def __init__(self, val=0, next=None):
        # Ensure node val is between -100 and 100
        while True:
            if (-100 <= val <= 100):
                break
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n = n + 1

        k = k % n

        if k == 0:
            return head
        
        new_tail = head

        for _ in range(n - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head