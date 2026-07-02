# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursive way; O(n) time and O(n). Not the most optimal way.

        #base case
        if not head:
            return None
        
        #this is just so if there's no head.next but if there is one, 
        #this is going to be overwritten
        new_head = head


        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head

        #removing the the old forward pointer
            head.next = None

        return new_head

        #4 -> 3 -> 2
