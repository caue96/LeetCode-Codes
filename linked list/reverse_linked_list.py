'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''
class ListNode:
    def __init__(self, val=0, next=None):
        # Ensure node val is between -5000 and 5000
        while True:
            if -5000 <= val <= 5000:
                break
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        number_nodes = 0
        temp = head
        
        while temp:
            number_nodes = number_nodes + 1
            temp = temp.next

            # Ensure the number of nodes is in the range of 0 and 5000
            if number_nodes > 5000:
                return
            
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev