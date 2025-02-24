'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        # Ensure val is between -100 and 100
        while True:
            if (-100 <= val <= 100):
                break
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Ensure the number of nodes in list1 and list2 is in the range 0 and 50
        def check_list_size(head):
            size = 0

            while head:
                size = size + 1
                head = head.next

                if size > 50:
                    break

        check_list_size(list1)
        check_list_size(list2)

        dummy = ListNode(0)
        current = dummy
        p1 = list1
        p2 = list2
        
        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next

            current = current.next
        
        if p1:
            current.next = p1
        else:
            current.next = p2
        
        return dummy.next