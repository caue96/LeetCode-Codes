'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9
'''
class ListNode:
    def __init__(self, val=0, next=None):
        # Ensure val is between 0 and 9
        while True:
            if (0 <= val <= 9):
                break
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Ensure number of nodes is in the range 1 and 10^5
        number_nodes = 0
        temp = head
        while temp:
            number_nodes = number_nodes + 1
            temp = temp.next
            if number_nodes > 10**5:
                return
            
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True