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
        
        #new head will always end up being the end of the forward linked list / start of reversed.
        #But we need to set it out here just in case there's no head.next
        new_head = head


        if head.next:
            new_head = self.reverseList(head.next)
            #adding the reverse pointer
            head.next.next = head
            #removing the the old forward pointer
            head.next = None

        #returns 
        return new_head

        #4 -> 3 -> 2
