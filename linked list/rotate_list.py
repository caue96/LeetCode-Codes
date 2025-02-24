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
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        