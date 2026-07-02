# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #doing it the iterative way first

        #can do two pointers, a prev and curr and just reverse the pointers

        prev, curr = None, head

        while curr:
            #have to remember the old next before we overwrite
            old_next = curr.next
            #reversing the pointer
            curr.next = prev
            #moving prev forward
            prev = curr
            #moving curr forward to our old next to repeat
            curr = old_next

        #by the end, prev will be the new head
        return prev

        #this is O(n) time and O(1) space