'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Constraints:
The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6
'''
class ListNode:
    def __init__(self, val=0, next=None):
        # Ensure val is between -10^6 and 10^6
        while True:
            if (-10**6 <= val <= 10**6):
                break       
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Ensure node val is in the range 0 and 10^4
        number_nodes = 0
        temp = head
        while temp:
            number_nodes = number_nodes + 1
            temp = temp.next
            if number_nodes > 10**4:
                break
        
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return head