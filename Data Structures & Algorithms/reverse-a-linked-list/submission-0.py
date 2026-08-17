# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # head = createSinglyLinkedList(head)

        # No pointer to previous yet because there is no previous node yet
        previous = None

        # initialize the current node instance to be head (the first node)
        current = head 
        
        while current: # While there is a current node

            # 1. Save the next node
            nxt = current.next
            # 2. Point the current node backward at the previous node
            current.next = previous
            # 3. Step forward by:
            # i. Setting the previous node to the current node
            previous = current 
            # ii. Setting the current node to be the next node
            current = nxt

        return previous