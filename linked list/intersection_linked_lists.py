'''
Link to the challenge: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

Constraints:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 10^4
1 <= Node.val <= 10^5
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
'''
class ListNode:
    def __init__(self, x):
        # Ensure Node val is between 1 and 100000
        if not (1 <= x <= 100000):
            return None
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        lenA, lenB = 0, 0
        currA, currB = headA, headB

        while currA:
            lenA = lenA + 1
            
            # Ensure lenA is between 1 and 30000
            if lenA > 30000:
                return None
            
            currA = currA.next

        while currB:
            lenB = lenB + 1
            
            # Ensure lenB is between 1 and 30000
            if lenB > 30000:
                return None
            
            currB = currB.next

        currA, currB = headA, headB
        
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        while currA and currB:
            if currA == currB:
                return currA
            
            currA = currA.next
            currB = currB.next

        return None